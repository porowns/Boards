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

# Posts
urlpatterns += {
    url(r'^view-post/(?P<pk>\d+)/$', views.viewPost, name='view-post'),
    url(r'^create-post', views.createPost, name='create-post'),
    url(r'^modify-post/(?P<pk>\d+)/$', views.modifyPost, name='modify-post'),
    url(r'^remove-post/(?P<pk>\d+)/$', views.removePost, name='remove-post'),
}

# Profile
urlpatterns += {
    url(r'^change-password/$', views.changePassword, name='change-password'),
    url(r'^change-username/$', views.changeUsername, name='change-username'),
    url(r'^delete-account/$', views.deleteAccount, name='delete-account'),
}

# Misc
urlpatterns += {
    url(r'^favorite/(?P<pk>\d+)/$', views.favorite, name='favorite'),
}
