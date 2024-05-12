from django.urls import path, re_path

from .views import *

urlpatterns=[
    path('', docker),
    path('categ/', categ), # http://127.0.0.1:8000/ansible/categ
    re_path(r'^arhiv/(?P<year>[0-9]{4})/', arhiv),
]