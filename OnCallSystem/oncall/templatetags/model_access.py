from django import template
from datetime import date, timedelta
from ..models import OncallRequest
import time

register = template.Library()

#Handles complete connection to admin index.
#See: templates/admin/index.html
@register.assignment_tag(takes_context=True)
def get_oncall_count_data(context):

    #get the request instance
    request = context['request']
    
    #get query options time_filter and custom_time_filter
    time_filter = request.GET.get('time', None)
    custom_time_filter = request.GET.get('custom_time', None)
    
    #set start and end times
    start = None
    end = date.today()
    
    #--handle custom_time_filters--
    #if the custom time filter is not None
    if(custom_time_filter != None):
        
        #use try except to catch any invalid date errors
        #gross solution yes, but cannot expect all unexpected conditions
        try:
            custom_time_filter = custom_time_filter.encode('ascii')
            data = custom_time_filter.split(",")
            
            start_date = time.strptime(data[0], "%Y-%m-%d")
            start_date = date(start_date.tm_year, start_date.tm_mon, start_date.tm_mday)
            
            end_date = time.strptime(data[1], "%Y-%m-%d")
            end_date = date(end_date.tm_year, end_date.tm_mon, end_date.tm_mday)
            
            start = start_date
            end = end_date
        
        #except and do nothing
        except:
            pass
            
        
    #--handle time_filters--
    #go through possible query options and set time delta accordingly 
    if(time_filter == 'any' or time_filter == None):
        pass 
    elif(time_filter == 'today'):
        start = date.today()
    elif(time_filter == 'week'):
        start = date.today() - timedelta(days=7)
    elif(time_filter == 'month'):
        start = date.today() - timedelta(days=30)
    elif(time_filter == 'year'):
        start = date.today() - timedelta(days=365)
    else:
        pass


    #if no start time is specified, no date filter will be applied
    if start == None: 
        requests = OncallRequest.objects.filter(expired = True)
        
    #apply range filters
    else:
        requests = OncallRequest.objects.filter(
            expired = True, date__range=[start, end]
        )
    
    #create data list. Data list is comprised of dictionaries holding individual coverage teachers data.
    #Ex: [{'name':'Brendan Kellam', 'y':10}, ...]
    data = []
        
    #Poll the oncall_request list to determine oncall count data
    #NOTE: Oncall request data is used over individual oncall_count data for Teacher models due to requests holding completetion dates.
    #These dates allow for a filter of oncall_count data
    for request in requests:
        
        #get the coverage teacher from the given request
        coverage_teacher = request.coverage_teacher
        
        #get coverage teacher id
        coverage_teacher_id = coverage_teacher.id
        
        #get coverage teacher name
        name = coverage_teacher.user.first_name + " " + coverage_teacher.user.last_name
        name = name.encode('ascii')
        
        #create found boolean to hold if a teacher's dictionary has been located
        found = False
                
        #loop the data list for each teacher dictionary
        for dic in data:
            
            #get the coverage teacher cache id from the dictionary
            cached_id = dic["id"]
            
            #determine if it is equal to the current coverage teacher's id
            if(cached_id == coverage_teacher_id):
                
                #increment oncall count and set found to true
                dic["y"]+=1
                found = True
                
        #if the dictionary is not found, create a new entry        
        if not found:
            data.append({'name' : name, 'y' : 1, 'id' : coverage_teacher_id})
    
    #following processing, remove all coverage_teacher id's from the data list
    for dic in data:
        del dic['id']
        
    #sort the data by oncall_count and reverse
    data = sorted(data, key=lambda k: k['y'])
    data.reverse()
    
    #return the formated data
    return data