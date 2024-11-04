from django.shortcuts import render
from todo.models import TaskModel

# Create your views here.
def task_list_view(request):
    tasks = TaskModel.objects.all() 
    if search_q := request.GET.get("q"):
        #  task = task.filter(title=search_q )
        task = task.filter(title__icontains=search_q )
    return render(request,'todo/Task_list.html',context={'tasks':tasks})
