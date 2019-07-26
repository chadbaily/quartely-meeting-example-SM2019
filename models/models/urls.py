"""models URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from modelsExample import views
# from modelsExample import api_views, views

# View sets have default methods for handling GET/POST/etc, so this is explicitly overriding that
request_override_map = {
    'get': 'get',
    'post': 'post',
    'put': 'put',
    'delete': 'delete'
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('modelsExample/', include('modelsExample.urls')),
    # url(r'^api/foodie/(?P<pk>[0-9]+)', foodie_list, name='foodie-detail'),
]
