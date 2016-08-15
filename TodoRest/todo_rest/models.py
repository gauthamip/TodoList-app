from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todolist(models.Model):
    user=models.ForeignKey(User)
    listid=models.IntegerField()
    name=models.CharField(max_length=40)
    # created=models.CharField(max_length=20)

class Todoitem(models.Model):
    item_list=models.ForeignKey(Todolist)
    item_id=models.IntegerField()
    name=models.CharField(max_length=40)
    description=models.CharField(max_length=40)
    due_date=models.CharField(max_length=20)
    completed=models.BooleanField()