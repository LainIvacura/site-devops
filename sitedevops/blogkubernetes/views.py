from django.shortcuts import render

from django.http import HttpResponse

def kubernetes (request):
    return HttpResponse("страница приложения blogkubernetes")

def categ(request):
    return HttpResponse("<h1>категории blogkubernetesCATEG</h1>")

def arhiv(requestn, year):
    return HttpResponse(f"<h1>АРХИВ blogarhiv</h1><p>{year}</p>")