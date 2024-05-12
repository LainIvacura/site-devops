"""
URL configuration for sitedevops project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # дописан импорт инклуда 

from blogdevops.views import *
from blogansible.views import *
from blogdocker.views import *
from bloggit.views import *
from blogkubernetes.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogdevops.urls')), #  вставлять внтри приложения другие страницы (функции)
    path('ansible/', include ('blogansible.urls')),
    path('docker/', include ('blogdocker.urls')),
    path('git/', include ('bloggit.urls')), 
    path('kubernetes/', include ('blogkubernetes.urls')),
]
