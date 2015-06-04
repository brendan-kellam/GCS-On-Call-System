import datetime
from django.db import models
from django.utils import timezone

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