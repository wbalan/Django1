from django.urls import path, re_path, include
from uchet import views
app_name = 'uchet'

urlpatterns = [
    path("", views.journal_list),
    re_path("journal_add", views.journal_add),
    path("journal", views.journal ),
    path("journal_create", views.journal_create),
    path("edit/<int:number>/", views.journal_edit),
    path("journal_delete/<int:number>/", views.journal_delete),


]
