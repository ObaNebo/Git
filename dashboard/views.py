from django.shortcuts import render
from blog.models import Task  # Импортируем модель Task из другого приложения


def dashboard_view(request):
    tasks = Task.objects.all()
    return render(request, 'dashboard.html', {'title': 'Главная страница', 'tasks': tasks})

def about_view(request):
    return render(request, 'about.html', {'about': 'О нас'})

def autor_view(request):
    return render(request, 'autor.html', {'autor': 'Автор'})

# def blog_view(request):

