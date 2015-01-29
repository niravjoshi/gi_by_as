# Django imports
from django.conf.urls import patterns, url

# App imports
from gi_by_as import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
)


