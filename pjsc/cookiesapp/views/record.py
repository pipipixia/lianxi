from django.http import HttpResponse
from django.shortcuts import render


def go_index(request):
    return render(request, 'record/index.html')


def prouct(request, tag):
    if tag == 'cloth':
        response = HttpResponse('查询到衣服的数据...')
    elif tag == 'book':
        response = HttpResponse('查询书记数据')
    elif tag == 'computer':
        response = HttpResponse('查询电脑数据')

    response.set_cookie('favorite', tag, max_age=30)  # 记录用户浏览历史
    return response


def product_view(request):
    favorite = request.COOKIES.get('favorite')
    if favorite == 'cloth':
        recommend_dist = ['上衣', '品牌上衣','媳妇']
    elif favorite == 'book':
        recommend_list = ['三国演义', '西游记', '水浒传']
    elif favorite == 'computer':
        recommend_list = ['戴尔', '联想', '华硕']
    else:
        recommend_list = ['随便点', '果粒橙']
    return render(request, 'record/recommend_product.html', locals())