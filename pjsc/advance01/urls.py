"""pjsc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path

from advance01.views import register, go_succ
from myapp.views import hello, introduce, welcome, convertor_view, slug_view, hehe_view, foot_view, sport_view, \
    pass_dict
app_name = 'advance01'
urlpatterns = [
    path('regis/', register, name='reg'),
    path('succ/<regname>', go_succ, name='suc')
    ]
