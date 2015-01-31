# Django imports
from django.conf.urls import patterns, url

# App imports
from gi_by_as import views

urlpatterns = patterns('',
        url(r'^$', views.home, name='home'),
        url(r'^home/$', views.home, name='home'),
        url(r'^aboutus/$', views.aboutus, name='aboutus'),
        url(r'^services/$', views.services, name='services'),
        url(r'^clients/$', views.clients, name='clients'),
        url(r'^contactus/$', views.contact, name='contact'),
)


