from django.core.management.base import BaseCommand
from ...models import Teacher, OncallRequest

#handles reseting teacher and oncall request data
class Command(BaseCommand):

    help = 'This command resets all teacher oncall_count data (I.E the number of times they covered) aswell as all oncall requests'

    #handles expired oncall requests
    def handle(self, *args, **options):
        
        #reply string
        reply = ""
        
        #handle invalid replies
        try:
            reply = raw_input("WARNING. THIS COMMAND WILL DELETE ALL ONCALL COUNT DATA AND ONCALL REQUEST DATA\nAre you sure?(y)/(n)")                
        except:
            print "invalid input"
            return
        
        #if the reply if yes, continue
        if reply == "y":
            print "\nInitiating reset process.."
            
            #get all teachers
            teachers = Teacher.objects.all()
            
            #loop teachers and set their oncall_count to zero
            for teacher in teachers:
                teacher.oncall_count = 0
                teacher.save()
               
            #delete all oncall_request data 
            OncallRequest.objects.all().delete()
    
        
        #if the reply is no, abort
        elif reply == "n":
            print "\nAborting.."
            return
        
        #if non-valid
        else:
            print "invalid input"
            return
            
        #done!
        print "Done!"