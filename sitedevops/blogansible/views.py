from django.shortcuts import render

from django.http import HttpResponse

def ansible(request):
    return HttpResponse("страница приложения blogansible")

def categ(request):
    return HttpResponse("<h1>категории blogansibleCATEG</h1>")

def arhiv(requestn, year):
    return HttpResponse(f"<h1>АРХИВ blogarhiv</h1><p>{year}</p>")