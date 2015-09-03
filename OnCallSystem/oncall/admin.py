from django.contrib import admin
from .models import Teacher, Slot, Course, Period, OncallRequest


# Register your models here.


class SlotAdmin(admin.ModelAdmin):
    
    #inlines = [TeacherInLine]
    
    list_display = ('slot_id',)
        
    list_filter = ['slot_id']
    search_fields = ['slot_id']
    
class OnCallRequestAdmin(admin.ModelAdmin):
    list_display = ('date', 'slot', 'course', 'request_teacher', 'coverage_teacher', 'has_been_recived', 'expired',)
    
    list_filter = ['date', 'expired']
    search_fields = ['date']

    
admin.site.register(Slot, SlotAdmin)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Period)
admin.site.register(OncallRequest, OnCallRequestAdmin) 
    
    
    



