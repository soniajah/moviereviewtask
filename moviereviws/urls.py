from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^getmovies/$', views.getmovies, name='getmovies'),
    url(r'^getmoviereviews/(?P<question_id>[0-9]+)/$', views.getmoviereviews, name='getmoviereviews'),
    url(r'^addreview/(?P<question_id>[0-9]+)/$', views.addreview, name='addreview'),
]