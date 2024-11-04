from django.urls import path
from todo.views import task_list_view


app_name = 'todo'


urlpatterns = [
    path('', task_list_view, name='task_list' ),
]
