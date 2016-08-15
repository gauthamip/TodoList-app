"""TodoRest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url,include
from rest_framework import routers
from todo_rest import classviews
from todo_rest import views

router=routers.DefaultRouter()
router.register(r'item_set',classviews.TodoitemViewset)
router.register(r'list_set',classviews.TodolistViewset)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^todo_rest/',include("todo_rest.urls")),
    url(r'',include("django.contrib.auth.urls")),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
