from django.http import HttpResponse


def add_sesssion_data(request):
    request.session['username'] = 'tom'
    request.session['pwd'] = '123456'
    return HttpResponse('session设置成功')


def get_session_data(request, name):
    data = request.session.get(name, '该回话中不存在该属性' + name + '的值')  # 获取回话中对应属性名的值
    session_id = request.session.session_key
    return HttpResponse('获取到的session值为'+data+';sessionid是'+session_id)


def session_delete(request):
    request.session.flush()
    return HttpResponse('session删除了')