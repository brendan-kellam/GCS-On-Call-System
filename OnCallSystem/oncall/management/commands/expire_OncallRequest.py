from django.core.management.base import BaseCommand
from datetime import date, timedelta
from ...models import OncallRequest


class Command(BaseCommand):

    help = 'Expires OncallRequest objects which are out-of-date'

    #handles expired oncall requests. NOTE: the oncall_request date MUST be within 5 days of the past of the current date, or else it will not be marked as expired
    def handle(self, *args, **options):
        
        #set the buffer time
        buffer_time = 5
        start = date.today() - timedelta(days=buffer_time)
        end = date.today()
        
        #get the expired requests (that have not already been marked as expired)
        expired_requests = OncallRequest.objects.filter(
            date__range=[start, end]
        ).filter(
            #filter any requests that already are expired (reduces redundancy)
            expired=False
        )

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
            
            #set request expired boolean to true
            request.expired = True
            request.save()

        
