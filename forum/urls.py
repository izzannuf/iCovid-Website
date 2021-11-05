from django.urls import path, re_path
from django.conf.urls import url
from .views import *

app_name = 'forum'

urlpatterns = [
    path('', index, name='Forum'),
    path('postToForum/',post_to_forum,name='postToForum'),
    path('<str:slug>/', forum_post_detail, name="detail"),
    path('<str:slug>/postComment', post_comment, name="postComment"),
]
