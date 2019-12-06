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
from django.contrib import admin
from django.urls import path, include

from myapp import urls
from resverapp.views import go_show_link, show_me, show_reverse_view, register, go_success

app_name = 'resverapp'  # 被include()包含的子路由模块应该添加app_name
urlpatterns = [
    path('res/<stu_name>/<stu_age>/', go_show_link),
    path('me/<name>/<age>/', show_me, name='离散'),
    path('viewurl/', show_reverse_view),
    path('reg/', register, name = 'reg'),
    path('succ/', go_success, name='succ')
]
