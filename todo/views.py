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

def task_edit_view(request, pk):
    task = get_object_or_404(TaskModel, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo/task_form.html', {'form': form, 'task': task})


def task_delete_view(request, pk):
    task = get_object_or_404(TaskModel, pk=pk)
    if request.method == "POST":
        task.delete()
        return redirect('/')
    return render(request, 'todo/task_confirm_delete.html', {'task': task})
