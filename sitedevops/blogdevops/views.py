from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("страница приложения blogdevops")

def categ(request, catid):
    return HttpResponse(f"<h1>категории blogdevops</h1><p>{catid}</p>")

def arhiv(requestn, year):
    return HttpResponse(f"<h1>АРХИВ blogarhiv</h1><p>{year}</p>")