from django.conf.urls import include, url
from django.contrib import admin
import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^boards', views.boards, name='boards'),
    url(r'^profile', views.profile, name='profile'),
]
