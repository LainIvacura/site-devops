from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("страница приложения blogdevops")

def categ(request):
    return HttpResponse("<h1>категории blogdevops</h1>")