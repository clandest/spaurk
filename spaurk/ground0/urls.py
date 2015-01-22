from django.conf.urls import patterns, url

from ground0 import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
)
