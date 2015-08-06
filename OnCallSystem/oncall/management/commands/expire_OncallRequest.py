from django.core.management.base import BaseCommand
from datetime import date
from ...models import OncallRequest


class Command(BaseCommand):

    help = 'Expires OncallRequest objects which are out-of-date'

    #handles expired oncall requests
    def handle(self, *args, **options):
        
        #set the now time and get the expired requests
        now = date.today()
        expired_requests = OncallRequest.objects.filter(date=now)

        #if no expired requests exist, return
        if(len(expired_requests) == 0):
            return

        #loop each expired request
        for request in expired_requests:
            
            #get the coverage teacher and increment the oncall number for each patron by one
            teacher = request.coverage_teacher
            teacher.oncall_count += 1
            
            #save to the database
            teacher.save()

        #delete the expired requests
        OncallRequest.objects.filter(date=now).delete()
        
        
        
