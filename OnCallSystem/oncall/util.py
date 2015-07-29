from .models import Slot, Course, Period
from django.contrib.auth import models as admin_models

#This module is used for utility purposes


#create a new week relationship
week_relation = ["WEEK A", "WEEK B"]

#
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

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


def get_notified_admin_email_list():
    
    email_list = []
    
    group = admin_models.Group.objects.get(name='Notified_Admins')
    notified_admins = group.user_set.all()
    
    for admin in notified_admins:
        email_list.append(admin.email)

    return email_list

#---USED FOR FORM INITIALIZATION---
WEEK_CHOICE = format_choice(week_relation)
COURSE_LIST = format_choice(Course.objects.all())
SLOT_LIST = format_choice(Slot.objects.all())
PERIOD_LIST = format_choice(Period.objects.all())
