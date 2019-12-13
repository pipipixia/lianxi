import os
import shutil

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db import connection


def login(request):
    if request.method == 'POST':

        return render(request, 'form_data.html')

def form_data(request):
    if request.method == 'GET':
        return render(request, 'form_data.html')
    elif request.method == 'POST':
        pj = request.FILES.get('pj')
        MYAPP_DIR = os.path.dirname(os.path.abspath(__file__))
        dest_path = os.path.join(MYAPP_DIR, 'ststic','images', pj.name)
        dest_path = shutil.move(dest_path, 'd:/ststic/pj')
        with open(dest_path, 'wb') as f:
            for chunk in pj.chunks():
                f.write(chunk)
        return HttpResponse("<h3 style = 'color:red'>上传成功</h3>")



