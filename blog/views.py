from django.shortcuts import render , redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all()[:5]
    return render(request, 'blog/index.html', {'title': 'Главная страница', 'tasks': tasks})

def about(request):
    return render(request, 'blog/about.html', {'about': 'О нас'})

def autor(request):
    return render(request, 'blog/autor.html', {'autor': 'Автор'})

def create(request):
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
    return render(request, 'blog/create.html', context)
