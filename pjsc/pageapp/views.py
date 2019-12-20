from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

from pageapp.models import Xues

page_size = 3  # 指定每一页显示数据的条数


def student_view(request, pagenum=1):  # 分页函数，pagenum为页码数
    students = Xues.objects.all()  # 查询所有学生
    paginator = Paginator(students, page_size)  # 实例话分页器对象
    page = paginator.page(pagenum)  # 调用分页器对象的page方法，返回Page对象，该Page对象封装了当前学生模型的对象
    return render(request, 'page/index.html', {'page': page, 'pagintor': paginator})


def beauty_view(request):
    count = request.visit_count  # 获取中间件中设置的动态属性值（当前访问次数）
    return HttpResponse('<h3>第'+str(count)+'次访问了')