from django import forms
from datetime import date
from django.contrib.auth.models import User
from .models import Slot, Course, Period
from django.contrib.auth.forms import UserCreationForm

import util

 
class LoginForm(forms.Form):
    
    _class = "form-control"
    user_attrs = util.get_attrs(_class, "username")
    pass_attrs = util.get_attrs(_class, "password")
    
    username = forms.CharField(label='User Name', max_length=100, widget=forms.TextInput(attrs=user_attrs))
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput(attrs=pass_attrs))

class OnCallForm(forms.Form):
    
    _class = "form-control"
    
    #NOTE: Date in format of month|day|year
    date = forms.DateField(label='Date: (YYYY-MM-DD)', input_formats=['%Y-%m-%d'], initial=date.today, widget=forms.DateInput(attrs=util.get_attrs(_class, "date")))
    week_id = forms.ChoiceField(choices=util.WEEK_CHOICE, widget=forms.Select(attrs=util.get_attrs(_class, "week_id")))
    period = forms.ChoiceField(choices=util.PERIOD_LIST, widget=forms.Select(attrs=util.get_attrs(_class, "period")))
    course_code = forms.ChoiceField(choices=util.COURSE_LIST, widget=forms.Select(attrs=util.get_attrs(_class, "course_code")))
    slot = forms.ChoiceField(choices=util.SLOT_LIST, widget=forms.Select(attrs=util.get_attrs(_class, "slot")))
    description = forms.CharField(widget=forms.Textarea(attrs=util.get_attrs(_class, "description")))
    
class MyUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['email'].required = True