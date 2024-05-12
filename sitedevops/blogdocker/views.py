from django.shortcuts import render

from django.http import HttpResponse

def docker(request):
    return HttpResponse("страница приложения blogdocker")

def categ(request):
    return HttpResponse("<h1>категории blogdockerCATEG</h1>")

def arhiv(requestn, year):
    return HttpResponse(f"<h1>АРХИВ blogarhiv</h1><p>{year}</p>")