from django.contrib import admin

# Register your models here.

from todo_rest.models import *
admin.site.register([Todolist,Todoitem])