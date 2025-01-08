# from django.shortcuts import render , redirect
# from .models import Task
# from .forms import TaskForm
from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all()[:5]
    return render(request, 'blog/index.html', {'title': 'Панель управления', 'tasks': tasks})

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Форма была неверной'

    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'blog/create/create_task.html', context)

def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm(instance=task)
    return render(request, 'blog/edit/edit_task.html', {'form': form, 'task': task})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('index')
    return render(request, 'blog/delete/delete_task.html', {'task': task})
