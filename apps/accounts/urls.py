from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from . import views
urlpatterns = [
    url(r'^register/$', views.Register.as_view(), name='accounts-register'),
    url(r'^login/$', views.Login.as_view(), name='accounts-login'),
    url(r'^logout/$', views.Logout.as_view(), name='accounts-logout'),
    url(r'^edit/(?P<user_id>\d+)/$', views.edit, name='accounts-edit'),
    url(r'^update/(?P<user_id>\d+)/$', views.update, name='accounts-update'),
    url(r'^delete/(?P<user_id>\d+)/$', views.delete, name='accounts-delete'),
    url(r'^updatepass/(?P<user_id>\d+)/$', views.updatepass, name='accounts-updatepass'),
]
