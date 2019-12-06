from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse


def go_show_link(request, stu_name, stu_age):
    return render(request, 'reverse/show_link.html', locals())


def show_me(request, name, age):
    return HttpResponse(name + '果然点我了···' + str(age) + '岁了')


def show_reverse_view(request):
    url = reverse('rev:离散', args=('jack', 25))
    # 在视图函数中通过reverse()函数反向解析url并通过args传递参数顺序给路由捕获
    # 或者通过kwargs传递字典参数给路由
    # reverse()中间bicultural有参数
    # 在视图函数中reverse()函数解析URL
    # URL反向解析动态获取URL的一种方式，使用反向解析可以避免在模板和视图函数中
    # 硬编码路径，易于扩展和维护
    url2 = reverse('rev:离散', kwargs={'age': 29, 'name': 'toms'})
    print("通过kwargs传参反向解析的URL：", url2)
    print('通过args传参反向解析的URL：', url2)
    return HttpResponse('视图函数中反向解析的URL是：' + url2)


def register(request):
    if request.method == 'GET':
        return render(request, 'redicrect/reguster.html')
    elif request.method == 'POST':
        rename = request.POST.get('rename')
        password = request.POST.get('repasswd')
        print('注册的用户名:'+rename)
        return redirect(reverse('rev:succ'))


def go_success(request):
    return render(request, 'redicrect/success.html')
