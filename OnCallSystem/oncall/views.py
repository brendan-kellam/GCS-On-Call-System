from .models import Teacher, Slot, Course, Period, OncallRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth import models as admin_models
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import logout as logout_auth
from django.contrib.auth import login as login_auth
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .forms import OnCallForm
from .forms import LoginForm
from datetime import date
import thread
import time
from . import util
from django.db.models.signals import post_save

#context association for each url
urls = {
        "index" : "/oncall/",
        "oncall_request" : "/oncall/oncall_request/",
        "oncall_success" : "/oncall/oncall_request/success/",
        "login" : "/oncall/login/",
        "logout" : "/oncall/logout/",
        }

@login_required
def oncall_success(request):
    
    context = {
     'urls': urls,
    }
    
    return render(request, 'oncall/oncall_success.html', context)
   
#sends confirmed oncall request's data to required patrons.
#Accepts: all information relating to oncall request
def email_members(request_user, coverage_user, date, 
                  week_id, period, course, slot, description):
    
    #set the subject line
    subject = "Oncall request: " + str(date)
    
    #set the message
    message = "A oncall request has been generated with the following information:"    
    message += "\n Date: " + str(date)
    message += "\n Week: " + util.week_relation[week_id]
    message += "\n Day of Week: " + date.strftime("%A")
    message += "\n Period: " + str(period)
    message += "\n Course Code: " + str(course)
    message += "\n Slot: " + str(slot)
    message += "\n Request Teacher: " + request_user.first_name + " " + request_user.last_name
    message += "\n Coverage Teacher: " + coverage_user.first_name + " " + coverage_user.last_name
    message += "\n\nDescription:\n " + description
    
    #TODO: Remove on completion
    #--ADD TEST SUBSCRIPT---
    message += "\n\nTHIS IS A TEST EMAIL FOR THE GCS ONCALL SYSTEM. IF YOU GOT THIS ACCEDENTLY, PLEASE IGNORE."
    
    #--EMAIL COVERAGE AND REQUEST TEACHER--
    #verify and congregate request and coverage user's email
    email_list = util.get_user_email_list([request_user, coverage_user])

    #send system email to request and coverage user's
    send_mail(subject, message, None, email_list, fail_silently=False)
    
    
    #--ADMIN COPY--
    #add admin subscript
    message += "\n\n(admin copy)" 
    
    #get the notified admin group (NOTE: This group can be configured on the admin portal)
    group = admin_models.Group.objects.get(name='Notified_Administrators')
    notified_admins = util.get_group_email_list(group)
    
    #send system email to notified admin's
    send_mail(subject, message, None, notified_admins, fail_silently=False)
    
    print "COMPLETE" #TODO: Remove on completion

        
#returns a instance of the coverage teacher

def generate_coverage_teacher(request_user, oncall_date, slot_obj):    
        
    #get the teachers available for oncall on this specific slot
    teachers = slot_obj.teachers.all()
    
    #order the teacher list by the number of oncalls
    teachers = teachers.order_by('oncall_count')
    
    #if the requesting teacher is already available,
    #then a oncall request is not required!
    if(request_user.teacher in teachers):
        return False


    #get the list of oncall's on the date and slot of this request
    oncall_request_list = OncallRequest.objects.filter(
        slot=slot_obj
    ).filter(
        date=oncall_date
    ).filter(
        expired=False
    )
    
    print oncall_request_list
    
    
    coverage_teacher = None
    
    #loop the available teachers
    for teacher in teachers:  
        
        print teacher.user.first_name
        
        #checks if the current teacher is the requesting teacher
        if(teacher.user == request_user):
            
            print "----HANDLING A TEACHER THAT HAS COVERAGE AT THIS SLOT---"
            return None
            
            #if so, "continue" loop
            continue
        
        
        #set a reset boolean
        reset_loop = False
        
        #loop through ALL oncall requests that are at the same SLOT and DATE as this request
        for oncall_request in oncall_request_list:
            
            #check if the current iterated teacher has:
                #-ALREADY REQUESTED A ONCALL FOR THIS SPECIFIC SLOT AND DATE
                #-ALREADY BEEN ASSIGNED TO THIS SLOT AND DATE FOR A ONCALL
            if(oncall_request.request_teacher == teacher 
               or oncall_request.coverage_teacher == teacher):
                
                #teacher is un-eligible for oncall, so reset loop
                reset_loop = True
                break
        
        #if the teacher is un-eligible, continue with new iterator
        if(reset_loop): continue
        
        #At this point, a eligible coverage teacher has been determined 
        coverage_teacher = teacher
        
        #break out of the loop
        break
    
    #return the coverage teacher
    return coverage_teacher
 
#generates a new oncall request

@login_required
def generate_oncall(request, form):
    
    #get the current user
    user = request.user
    
    #get the date of oncall and convert to a datetime.date format
    oncall_date = str(request.POST['date'])
    oncall_date = time.strptime(oncall_date, "%Y-%m-%d")
    oncall_date = date(oncall_date.tm_year, oncall_date.tm_mon, oncall_date.tm_mday)
    #print "WEEEK", calendar.day_name[oncall_date.weekday()]
            
    #get the date now
    now = date.today()
    #calculate the change in time
    delta_time = oncall_date-now
    
    #check time validity 
    #NOTE: Oncalls cannot be filed on the same day of coverage
    if(delta_time.days <= 0):
        error = "Date " + str(oncall_date) + " is invalid. Enter date later than: " + str(now)
        form.add_error(None, error)
        return form, False
        
                
    #get the week id (I.E: Week A/ Week B)
    week_id = int(request.POST['week_id'])-1
    
    #get the period of coverag from form and create new period object
    period = int(request.POST['period'])
    period_obj = get_object_or_404(Period, pk=period)

    
    #get course related to oncall and create new course object
    course_code = int(request.POST['course_code'])
    course_obj = get_object_or_404(Course, pk=course_code)

    
    #get slot related to oncall and create new slot object
    slot = int(request.POST['slot'])
    slot_obj = get_object_or_404(Slot, slot_id=slot)
    
    
    #get description of oncall
    oncall_description = request.POST['description']
    
    #check if the description fits database constraints
    if(len(oncall_description) > 500):
        form.add_error(None, "Description exceeds 500 characters!")
        return form, False
    
    
    #generate a new coverage teacher.
    #Accepts: request-user, date-of-oncall and slot-of-oncall
    teacher_on_coverage = generate_coverage_teacher(user, oncall_date, slot_obj)   
    
    #if a coverage teacher could not be generated
    if(teacher_on_coverage == None):
        form.add_error(None, "Could not find coverage teacher")
        return form, False
    
    if(teacher_on_coverage == False):
        form.add_error(None, "You seem to have this slot free. Please contact IT if this is not the case.")
        return form, False
    
    
     
    try:       
        #if the coverage_teacher has been generated               
        #generate a new oncall request
        oncall = OncallRequest(
            date=oncall_date,
            week=week_id,
            period=period_obj,
            course=course_obj,
            slot=slot_obj,
            request_teacher=user.teacher,
            coverage_teacher=teacher_on_coverage,
            description=oncall_description,
            has_been_recived=False,
            expired=False
        )
            
        #save oncall request to database
        oncall.save() 
    
    except:
        form.add_error(None, "Unable to create request! Try again later.")
        return form, False
    
    #if the request was valid, start a new thread 
    #process for mailing members
    thread.start_new(
        #set properties for the thread
        email_members, 
        (user, teacher_on_coverage.user, oncall_date, week_id, period_obj, course_obj, slot_obj, oncall_description)
    )
    
    return form, True


@login_required  
def oncall_request(request):
    #get the current user that is signed in
    user = request.user
    
    if request.method == 'POST':
        
        #create a new populated form
        form = OnCallForm(request.POST)        
        
        #if the form is valie, continue
        if form.is_valid():
            
            #generate a new oncall request
            form, success = generate_oncall(request, form)            
            
            if(success):
                return HttpResponseRedirect(urls["oncall_success"])
    else:
        form = OnCallForm()
        
    
    #dictionary association for the html file
    context = {
    'user': user,
    'urls': urls,
    'form': form,
    'get_object_or_404' : get_object_or_404,
    'request' : OncallRequest,
    }
    
    
    return render(request, 'oncall/oncall_request.html', context)

@login_required
def index(request):

    #dictionary association for the html file
    context = {
    'urls': urls,
    }
    
    
    return render(request, 'oncall/index.html', context)

def login(request):
    
    print "Request Type:", request.method
    
    #if the user is already loged in
    if request.user.is_authenticated():
        return HttpResponseRedirect(urls["index"])
    
    #given a POST request
    if request.method == 'POST':
        
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # redirect to a new URL:
            
            #get the username and password
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            
            #if the user authentication is successful
            if user is not None:
                
                #if the user is still active
                if user.is_active:
                    
                    #log the user in
                    login_auth(request, user)
                    print "sucsess!"
                    
                    #redirect the user
                    return HttpResponseRedirect(urls["index"])
                
                
                #handle inactive account
                else:
                    form.add_error(None, "Inactive account!")
        
            #handle invalid login
            else:
                form.add_error(None, "Invalid Login!")
                
            
    #if the request is NOT POST (I.E GET)
    else:
        #create a blank login form
        form = LoginForm()
        
    #create a new context handler
    context = {
        'form': form,
    }
    
    #add related urls to context
    context.update(urls)
        
    #render the page
    return render(request, 'oncall/login.html', context)

@login_required
def logout(request):
    logout_auth(request)
    return HttpResponseRedirect(urls["login"])


#handle creating a Teacher instance when a corresponding User instance is created
#Note: This code is creating post_save (I.E after a user is created)
def on_user_creation(sender, instance, created, **kwargs):
    
    #if a user is created, create a new Teacher instance
    if created:
        Teacher.objects.create(user=instance)
   
#handle post_save connection
post_save.connect(on_user_creation, sender=User, dispatch_uid="create_teacher_instance")
    