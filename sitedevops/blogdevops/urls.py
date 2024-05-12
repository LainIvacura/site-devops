from django.urls import path, re_path

from .views import *

urlpatterns=[
    path('', index),  #http://127.0.0.1:8000/devops/
    path('categ/<int:catid>/', categ), # http://127.0.0.1:8000/devops/categ
    re_path(r'^arhiv/(?P<year>[0-9]{4})/', arhiv),
]