from django.conf.urls import include, url
from django.contrib import admin
import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^boards', views.boards, name='boards'),
    url(r'^profile', views.profile, name='profile'),
    url(r'^register', views.register, name='register'),
    url(r'^login', views.loginUser, name='login'),
    url(r'^logout', views.logoutUser, name='logout'),
]

# Boards
urlpatterns += {
    url(r'^view-board/(?P<pk>\d+)/$', views.viewBoard, name='view-board'),
    url(r'^create-board/', views.createBoard, name='create-board'),
    url(r'^modify-board/(?P<pk>\d+)/$', views.modifyBoard, name='modify-board'),
    url(r'^remove-board/(?P<pk>\d+)/$', views.removeBoard, name='remove-board'),
}
