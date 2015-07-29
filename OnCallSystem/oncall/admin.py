from django.contrib import admin
from .models import Choice, Question, Teacher, Slot, Course, Period, OncallRequest


# Register your models here.

#Create a new stacked inline set of choices
class ChoiceInline(admin.TabularInline):
    
    #set the model
    model = Choice
    
    #set the original count (NOTE: These cannot be removed)
    extra = 3

#A model admin object for the Question model
class QuestionAdmin(admin.ModelAdmin):
    
    #create a new field
    fieldsets = [
                 
        #index 0 of each tuple is the title of the field
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}), #uses collapse to hide/show information
    ]
    
    inlines = [ChoiceInline];
    
    #adds a new list display
    list_display = ('question_text', 'pub_date', 'was_recently_published')
    
    #adds a new list display filter
    list_filter = ['pub_date']
    
    #add a new search bar
    search_fields = ['question_text']


class SlotAdmin(admin.ModelAdmin):
    
    #inlines = [TeacherInLine]
    
    list_display = ('slot_id',)
        
    list_filter = ['slot_id']
    search_fields = ['slot_id']
    
class OnCallRequestAdmin(admin.ModelAdmin):
    list_display = ('date', 'slot', 'course', 'request_teacher', 'coverage_teacher', 'has_been_recived',)
    
    list_filter = ['date']
    search_fields = ['date']
    
    
admin.site.register(Question, QuestionAdmin);
admin.site.register(Slot, SlotAdmin)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Period)
admin.site.register(OncallRequest, OnCallRequestAdmin)


