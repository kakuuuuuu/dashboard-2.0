from django.conf.urls import include, url, patterns
from . import views
urlpatterns=[
    url(r'^post/(?P<user_id>\d+)/$', views.makePost, name='posts-post'),
    url(r'^comment/(?P<user_id>\d+)/(?P<post_id>\d+)/$', views.makeComment, name='posts-comment'),
    url(r'^delete/post/(?P<user_id>\d+)/(?P<post_id>\d+)/$', views.deletePost, name='post-delpost'),
    url(r'^delete/comment/(?P<user_id>\d+)/(?P<comment_id>\d+)/$', views.deleteComment, name='post-delcomment'),

]
