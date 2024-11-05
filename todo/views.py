from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from . models import TaskModel
from . forms import TaskForm


# Create your views here. 
def task_list_view(request):
    tasks = TaskModel.objects.all() 
    if search_q := request.GET.get("q"):
        tasks = tasks.filter(title__icontains=search_q)
    return render(request, 'todo/task_list.html', context={'tasks': tasks})

def task_create_view(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TaskForm()
    return render(request, 'todo/task_form.html', {'form': form})