from django.conf.urls import url
from django.contrib import admin
from todo_rest import views
from todo_rest.classviews import LListView, ICreateView
from todo_rest.classviews import LDetailView
from todo_rest.classviews import LCreateView
from todo_rest.classviews import LUpdateView
from todo_rest.classviews import LDeleteView
from todo_rest import classviews

urlpatterns = [
    url(r'^list/',views.lists),
    url(r'^item/(?P<name>[0-9]+)/$',views.item),
    url(r'^list_list/$',LListView.as_view(template_name='todolist_list.html'),name='create'),
    url(r'^list_list/$',LListView.as_view(template_name='todolist_list.html'),name='delete'),
    url(r'^detail_list/(?P<pk>[0-9]*)/$',LDetailView.as_view(template_name='todolist_detail.html'),name='update'),
    url(r'^create/$',LCreateView.as_view(template_name='todolist_create.html')),
    url(r'^update/(?P<pk>[0-9]*)/$',LUpdateView.as_view(template_name='todolist_create.html')),
    url(r'^delete/(?P<pk>[0-9]*)/$',LDeleteView.as_view(template_name='todolist_confirm_delete.html')),
    url(r'^create/item/$',ICreateView.as_view(template_name='todoitem_create.html')),
    url(r'^list_list/$',LListView.as_view(template_name='todolist_list.html'),name='create_item'),
    url(r'^list_dispaly/$',views.list_list),
    url(r'^list_details/$',views.list_detail)
    #  url(r'list/$',views.list_list),
    #  url(r'list_details/(?P<pk>[0-9]*)/$',views.list_detail)

]