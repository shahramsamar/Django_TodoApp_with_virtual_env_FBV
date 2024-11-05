from django.contrib import admin
from todo.models import TaskModel

@admin.register(TaskModel)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id','title','is_done']