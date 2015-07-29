from django.conf.urls import include, url, patterns
from . import views

#NOTE: $ states end of string
urlpatterns = [
               
    #NOTE: <pk> is used for GENERIC VIEWS ONLY
    
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    
    #url(r'^oncall_request/$', views.oncall_request, name='oncall_request'),
    

    
    #url('^', include('django.contrib.auth.urls')),
    

    
   """
   url(r'^$', views.IndexView.as_view(), name='index'),
   url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
   url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
   
   #ex: /oncall/5/vote
   url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
   
   url(r'^(?P<teacher_id>[0-9]+)/teacher/$', views.displayTeacher, name='teacher'),
   """
]