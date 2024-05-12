from django.shortcuts import render

from django.http import HttpResponse

def kubernetes (request):
    return HttpResponse("страница приложения blogkubernetes")
