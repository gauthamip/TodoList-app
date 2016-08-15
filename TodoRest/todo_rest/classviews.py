from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from todo_rest.models import *
from rest_framework import viewsets
from todo_rest.Serializers import *

@method_decorator(login_required,name='dispatch')
class LListView(ListView):
    model = Todolist

@method_decorator(login_required,name='dispatch')
class LDetailView(DetailView):
    model=Todolist

    def get_object(self, queryset=None):
        id1 = self.kwargs.get('pk')
        queryset = Todolist.objects.all().get(id=id1)
        return queryset

@method_decorator(login_required,name='dispatch')
class LCreateView(CreateView):
    model = Todolist
    fields =['listid','name']
    def get_success_url(self):
        return reverse('create')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(LCreateView, self).form_valid(form)

@method_decorator(login_required,name='dispatch')
class ICreateView(CreateView):
    model = Todoitem
    fields=['item_list','item_id','name','description','due_date','completed']
    def get_success_url(self):
        return reverse('create_item')
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super(ICreateView,self).form_valid(form)


@method_decorator(login_required,name='dispatch')
class LUpdateView(UpdateView):
    model = Todolist
    fields = ['listid','name']
    def get_success_url(self):
        pk=self.kwargs.get('pk')
        return reverse('update',kwargs={'pk':pk})

@method_decorator(login_required,name='dispatch')
class LDeleteView(DeleteView):
    model=Todolist
    success_url =reverse_lazy('delete')

class TodolistViewset(viewsets.ModelViewSet):
    queryset = Todolist.objects.all().order_by('id')
    serializer_class = TodolistSerializer

class TodoitemViewset(viewsets.ModelViewSet):
    queryset = Todoitem.objects.all().order_by('item_list')
    serializer_class = TodoitemSerializer

