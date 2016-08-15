from django.contrib.auth.models import *
from rest_framework import serializers
from todo_rest.models import *

class TodolistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Todolist
        fields=('name','listid')


class TodoitemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Todoitem
        fields=('item_list','item_id','name','description','due_date','completed')


