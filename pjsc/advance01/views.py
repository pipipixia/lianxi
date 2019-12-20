from django.shortcuts import render, redirect
from django.urls import reverse


def register(request):
    if request.method == 'GET':
        return render(request, 'regiester.html')
    elif request.method == 'POST':
        regname = request.POST.get('regname')
        return redirect(reverse('advance01:suc', args=(regname,)))


def go_succ(request, regname):
    return render(request, 'success.html', {'regname': regname})
