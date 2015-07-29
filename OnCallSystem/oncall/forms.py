from django import forms
from datetime import date
from .models import Slot, Course, Period
import util

 
class LoginForm(forms.Form):
    
    username = forms.CharField(label='User Name', max_length=100)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput())

class OnCallForm(forms.Form):
    
    #NOTE: Date in format of month|day|year
    date = forms.DateField(label='Date: (YYYY-MM-DD)', input_formats=['%Y-%m-%d'], initial=date.today)
    week_id = forms.ChoiceField(choices=util.WEEK_CHOICE)
    period = forms.ChoiceField(choices=util.PERIOD_LIST)
    course_code = forms.ChoiceField(choices=util.COURSE_LIST)
    slot = forms.ChoiceField(choices=util.SLOT_LIST)
    description = forms.CharField(widget=forms.Textarea)
    
    