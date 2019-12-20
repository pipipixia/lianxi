import os
import shutil

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db import connection

from myapp.models import User, Pi_jie


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('yourpassword')
        users = User.objects.get(username=username)

        if users:
            users.first()
            if password == users.password:
                return redirect(reverse('myapp:succ'))  # 登陆成功之后
            else:
                return HttpResponse("<h3 style = 'color:orange'>用户名或密码错误</h3>")
        else:

            return render(request, 'login.html')


#  删除图片
def form_data(request):
    if request.method == 'GET':
        return render(request, 'form_data.html')
    elif request.method == 'POST':
        pj = request.FILES.get('pj')
        pihao = request.POST.get('pihao')
        sp_bh = request.POST.get('sp_bh')
        cursor = connection.cursor()
        user = User.obects.get(username=request.user)
        huoz_id = user.huoz_id
        sql = 'SELECT spid, spbh, spmch, dw, shpgg, shengccj, pizhwh where huo_id = /"' + huoz_id
        cursor.execute(sql)
        result = cursor.fetchall()
        MYAPP_DIR = os.path.dirname(os.path.abspath(__file__))
        dest_path = os.path.join(MYAPP_DIR, 'ststic', 'images', pj.name)
        ext = os.path.split(pj.name)
        dest_path = shutil.move(dest_path, 'd:/ststic/pj')
        new_pj = Pi_jie()
        new_pj.address = dest_path
        new_pj.extend = ext
        new_pj.huozhu = huoz_id
        new_pj.save()
        with open(dest_path, 'wb') as f:
            for chunk in pj.chunks():
                f.write(chunk)
        return HttpResponse("<h3 style = 'color:red'>上传成功</h3>")


#  登陆成功
def go_success(request):
    return render(request, 'success.html')

# 更改图片
# def change(request):
