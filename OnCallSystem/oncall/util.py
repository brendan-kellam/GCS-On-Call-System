from .models import Slot, Course, Period
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

#---This module is used for utility purposes---

#---VARS: 
#create a new week relationship
week_relation = ["Week A", "Week B"]

#create a table of weeks
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

#---UTILITIES

#determines if a given email address is valid.
def is_email_valid(email):
    
    try:
        #if valid return true
        validate_email(email)
        return True
    
    #handle invalid email addresses
    except ValidationError:
        return False


#returns every user's email in a given GROUP
#Accepts: a group. Returns: list of email addresses (Acii format)
def get_group_email_list(group):
    
    #get the user email list by passing in the group user list
    return get_user_email_list(group.user_set.all())

#returns every user's email in a given list of users
#Accepts: a user list. Returns: list of emails (Ascii format)
def get_user_email_list(users):
    
    #instantiate empty list
    email_list = []
    
    #loop each user in the list
    for user in users:
        
        #append each email
        email_address = user.email
        
        #check validity of each email
        if(not is_email_valid(email_address)): 
            continue #if email is invalid, continue with loop
                
        #append the address to the list
        email_list.append(email_address.encode('ascii'))

    
    #return the list
    return email_list

#generate the widget attributes given a class and name
def get_attrs(_class, name):
    
    #convert the name to a title (IE capitalize first letter)
    title = str(name.capitalize())
    
    #create id (example: inputUsername)
    ident = "input" + title
    
    #attributes
    attrs = {
        "class" : _class,
        "id" : ident,
        "placeholder" : title, 
        "type" : str(name)
    }
    
    return attrs
    

#Formats a given list into a ChoiceField format
def format_choice(data):
    
    #create a list
    CHOICE_DATA = []
    
    #loop the list length of the data list
    for i in range(len(data)):
        
        #set the count and get the current data
        count = i+1
        info = data[i]
        
        #append the count info in a Field format
        #NOTE: format for ChoiceField = (count, (info))
        CHOICE_DATA.append((count, (info)))
      
    #return the formated data
    return CHOICE_DATA

#---USED FOR FORM INITIALIZATION---

WEEK_CHOICE = format_choice(week_relation)
COURSE_LIST = format_choice(Course.objects.all())
SLOT_LIST = format_choice(Slot.objects.all())
PERIOD_LIST = format_choice(Period.objects.all())