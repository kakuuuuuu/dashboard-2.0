from django.conf.urls import include, url, patterns
from django.contrib.auth.decorators import login_required
from . import views
urlpatterns = [
    url(r'^$', views.Index.as_view(), name='dash-index'),
    url(r'^dashboard/$', login_required(views.Dashboard.as_view(), login_url='dash-index'), name='dash-dashboard'),
    url(r'^users/(?P<user_id>\d+)/$', views.userpage, name='dash-userpage')
]
