from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'oncall/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'oncall/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'oncall/results.html'


def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    
    try:
        
        #get the selected 
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
        print "Choice:", selected_choice;
        
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'oncall/detail.html', {
            'question': p, 
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        
        #redirect to results page
        return HttpResponseRedirect(reverse('oncall:results', args=(p.id,)))
    