from django.shortcuts import render

from django.http import HttpResponse

def git(request):
    return HttpResponse("страница приложения bloggit")
