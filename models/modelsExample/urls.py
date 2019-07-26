from django.conf.urls import url
from django.views.generic.base import RedirectView
from . import views
# from . import api_views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    # url(r'^login/$', views.login_submit, name='login'),
    # url(r'^user/$', views.get_auth_user, name='auth_user'),
    # url(r'^foodie/$', views.get_auth_foodie, name='auth_foodie'),
    # url(r'^logout/$', views.logout, name='logout')
]
