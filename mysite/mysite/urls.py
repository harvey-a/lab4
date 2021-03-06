"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
'''
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from shop import views
urlpatterns = [
url(r'^$', views.user_list.as_view(), name='user_list'),
url(r'^new$', views.user_create.as_view(), name='user_new'),
url(r'^edit/(?P<pk>\d+)$', views.user_update.as_view(), name='user_edit'),
url(r'^delete/(?P<pk>\d+)$', views.user_delete.as_view(), name='user_delete'),
#url(r'^servers/', include('servers.urls')),
'''

from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from business import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', views.UserList.as_view()),
    re_path(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    path('products/', views.ProductList.as_view()),
    re_path(r'^products/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view()),
    path('carts/', views.CartList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)