from django.urls import path
from . import views



app_name = 'todo'


urlpatterns = [
    path('', views.task_list_view, name='task_list'),
    path('create/', views.task_create_view, name='task_create'),
    path('edit/<int:pk>/', views.task_edit_view, name='task_edit'),
    path('delete/<int:pk>/', views.task_delete_view, name='task_delete'),

]
