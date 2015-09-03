from django.conf.urls import url
from . import views

#NOTE: $ states end of string
urlpatterns = [
               
    #NOTE: <pk> is used for GENERIC VIEWS ONLY
    
    url(r'^$', views.index, name='index'),
    url(r'^oncall_request/$', views.oncall_request, name='oncall_request'),
    url(r'^oncall_request/success/$', views.oncall_success, name='oncall_success'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
]