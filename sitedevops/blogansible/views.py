from django.shortcuts import render

from django.http import HttpResponse

def ansible(request):
    return HttpResponse("страница приложения blogansible")