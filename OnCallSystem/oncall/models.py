import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model): #inherits from models.Model
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    #set a string representation for the model
    def __str__(self):
        return self.question_text
    
    def was_recently_published(self):
        return self.pub_date > timezone.now() - datetime.timedelta(days=1)
    
    #sets admin properties
    was_recently_published.admin_order_field = 'pub_date'
    was_recently_published.boolean = True
    was_recently_published.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    #set a string representation for the model
    def __str__(self):
        return self.choice_text

#-----    
    
class Period(models.Model):
    period_number = models.IntegerField(default = 1)
    
    def __str__(self):
        return "Period_" + str(self.period_number)
    

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
    
    #denotes if the teacher is already assigned to a oncall
    #NOTE: THIS FIELD WILL BE FALSE IF A GIVEN TEACHER HAS REQUESTED A ONCALL
    #available_for_oncall = models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

    
class Slot(models.Model): #https://docs.djangoproject.com/en/1.8/topics/db/examples/many_to_many/
    slot_id = models.IntegerField(default = 1)
    teachers = models.ManyToManyField(Teacher)
    
    def __str__(self):
        out = "Slot_" + str(self.slot_id)
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
    
    def __str__(self):
        return str(self.date)
    

        
    