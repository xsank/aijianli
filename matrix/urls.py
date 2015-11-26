__author__ = 'xsank'

from views import *
from django.conf.urls import patterns

urlpatterns = patterns('',
                       (r'^$', IndexView.as_view()),
                       (r'^account/(?P<id>[\w\d]+)$', UserView.as_view()),
                       (r'^resume/(?P<id>[\w\d]+)$', ResumeView.as_view()),
                       (r'^resume/(?P<id>[\w\d]+)/export$',
                        ExportView.as_view()),
                       (r'^resume/(?P<id>[\w\d]+)/preview$',
                        Preview.as_view()),
                       (r'^sorry$', SorryView.as_view()),
                       )
