from django.shortcuts import render

# Create your views here.
from todo_rest.models import *
from django.template import loader
from django.http import HttpResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from todo_rest.Serializers import *

class JSONResponse(HttpResponse):
    def __init__(self,data,**kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type']='application/json'
        super(JSONResponse,self).__init__(content,**kwargs)

def lists(request):
    list1 = Todolist.objects.all()
    template = loader.get_template("todolist_list.html")
    result = template.render(context={"list1": list1})
    return HttpResponse(result)

def item(request,name):
    items=Todoitem.objects.all().filter(item_list=name)
    template=loader.get_template("todoitem.html")
    result=template.render(context={"item":items})
    return HttpResponse(result)

@csrf_exempt
def list_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Todolist.objects.all()
        serializer = TodolistSerializer(snippets, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TodolistSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def list_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Todolist.objects.get(pk=pk)
    except Todolist.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TodolistSerializer(snippet)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TodolistSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)