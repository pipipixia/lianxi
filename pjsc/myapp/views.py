from django.http import HttpResponse

from django.shortcuts import render


# Create your views here.
def hello(request):
    return HttpResponse("<h3 style ='color:red'>欢迎，Django！</h3>")


def introduce(request, name, home):
    return HttpResponse("<h3 >我叫<span style='color:blue'>" + name + "，家在" + home + "</span></h3>")


#


def welcome(request, stuname, money):
    return HttpResponse("<h3 style='color:green'>欢迎" + stuname + "学习Django!" + money + "亿</h3>")


def convertor_view(request, name, age, uid, info):
    print('uid:', uid, type(uid))
    age += 1
    result = '我叫' + str(name) + '今年' + str(age) + '岁了；uuid是：' + str(uid) + 'Path转换器得参数是' + str(info)
    return HttpResponse(result)


def slug_view(request, explanation):
    print('explanation:', type(explanation))
    return HttpResponse(explanation)


def hehe_view(request):
    return HttpResponse('hehe')


'''作业
水果列表
'''


def foot_view(request):
    fruits = ['苹果', '香蕉', '橙子', '菠萝']
    return render(request, 'home/fruits.html', {'fruits': fruits})


'''运动'''


def sport_view(request, info):
    sports = []
    if info == 'allsports':
        sports.extend(['足球', '篮球', '跑步'])
    return render(request, 'home/sport.html', {'sports': sports})


def pass_dict(request, key):
    data = {
        'color': '黄色',
        'country': '中国'
    }
    return render(request, 'home/filter.html', locals())
