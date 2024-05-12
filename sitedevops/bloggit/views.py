from django.shortcuts import render

from django.http import HttpResponse

def git(request):
    return HttpResponse("страница приложения bloggit")

def categ(request):
    return HttpResponse("<h1>категории bloggitCATEG</h1>")

def arhiv(requestn, year):
    return HttpResponse(f"<h1>АРХИВ blogarhiv</h1><p>{year}</p>")