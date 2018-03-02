from django.conf.urls import url

from . import views
from projects import views as projects_views


urlpatterns = [
#    url(r'^$', projects_views.projects_index, name='projects_index'),
    url(r'^(?P<project_id>[0-9]+)/$', projects_views.project, name='project_list'),
    url(r'^thankyou/', projects_views.thankyou, name='thankyou'),
#    url(r'^donate/', projects_views.donate, name='donatename'),
]
