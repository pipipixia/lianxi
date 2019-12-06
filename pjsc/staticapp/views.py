from django.shortcuts import render


def go_hello(request):
    return render(request, 'hello.html')
