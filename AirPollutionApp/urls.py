"""AirPollutionApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from core import views as core_views
from projects import views as projects_views

urlpatterns = [
#r'^$', views.index, name='index'
#    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^$', projects_views.index, name='home'),
    url(r'^about/', projects_views.about, name='about'),
    url(r'^admin/', admin.site.urls),
    url(r'^projects/', include('projects.urls')),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--
    url(r'^signup/$', core_views.signup, name='signup'),
]

