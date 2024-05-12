from django.shortcuts import render

from django.http import HttpResponse

def docker(request):
    return HttpResponse("страница приложения blogdocker")