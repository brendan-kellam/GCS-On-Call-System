from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 

class Period(models.Model):
    period_number = models.IntegerField(default = 1)

    def __str__(self):
        return "Period " + str(self.period_number)


class Course(models.Model):

    #create a new course_code char field
    course_code = models.CharField(max_length=100)

    def __str__(self):
        return self.course_code


class Teacher(models.Model):

    #the related user
    user = models.OneToOneField(User, default = None)

    #the total number of times a teacher has been ocalled
    oncall_count = models.IntegerField(default = 0)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class Slot(models.Model): #https://docs.djangoproject.com/en/1.8/topics/db/examples/many_to_many/
    slot_id = models.IntegerField(default = 1)
    teachers = models.ManyToManyField(Teacher)

    def __str__(self):
        out = "Slot " + str(self.slot_id)
        return out

class OncallRequest(models.Model):
    date = models.DateField()
    week = models.IntegerField(default = 0)
    period = models.ForeignKey(Period)
    course = models.ForeignKey(Course)
    slot = models.ForeignKey(Slot)
    request_teacher = models.ForeignKey(Teacher, related_name="request_teacher")
    coverage_teacher = models.ForeignKey(Teacher, related_name="coverage_teacher")
    description = models.CharField(max_length=500)
    has_been_recived = models.BooleanField(default=False)
    expired = models.BooleanField(default=False)

    def __str__(self):
        return str(self.date)

class MyUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['email'].required = True
