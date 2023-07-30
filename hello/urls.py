from django.urls import path, re_path, include
from hello import views
app_name = 'hello'

urlpatterns = [
    path("listroute/", views.viewroute),
    path("createroute/", views.createroute),
    path("", views.list),
    path("add/", views.add),
    path("create/", views.create),
    path("list/", views.list),
    path("listroute/", views.viewroute),
    path("createroute/", views.createroute),
    path("edit/<int:number>/", views.edit),
    path("delete/<int:number>/", views.delete),
]
