import os

from django.http import HttpResponse
from django.shortcuts import render


def upload_form(request):
    if request.method == 'GET':
        return render(request, 'sc.html')
    elif request.method == 'POST':
        moto = request.POST.get('moto')  # 接受请求体中的参数
        image = request.FILES.get('image')  # 接受上传文件,返回上传文件对象
        # print('upload_file类型是什么:', type(image))
        UPLOADPP_DIR = os.path.dirname(os.path.join(__file__))
        print(UPLOADPP_DIR)
        dest_path = os.path.join(UPLOADPP_DIR, 'images', image.name)  # 拼接文件上传文件路径
        print(dest_path)
        with open(dest_path, 'wb') as f:
            for chunk in image.chunks():  # 对上传的文件进行分块写入
                f.write(chunk)
        return HttpResponse('上传成功! 你的格言是：' + moto)
