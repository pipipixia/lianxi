from django.http import HttpResponse
from django.shortcuts import render


def add_cookies(request):
    response = HttpResponse("<h3>Cookie添加成功！</h3>")
    response.set_cookie("fruit", "苹果".encode("utf-8"))  # 设置Cookie，在Django中中文必须编码
    response.set_cookie("sport", "pingpong", max_age=30)
    response.set_signed_cookie("account", "tom123", salt="abcde", max_age=30)  # 加盐Cookie
    return response


def show_cookies(request):
    fruit = request.COOKIES.get("fruit")  # 获取未加密的Cookie
    sport = request.COOKIES.get("sport")
    try:
        account = request.get_signed_cookie("account", salt="abcde")  # 解密Cookie必须使用request的get_signed_cookie()方法
        print('account=', account)
    except:
        print("account已经过期")
    print("fruit=", fruit, "；sport=", sport)
    return HttpResponse("请查看后台打印的Cookie")
