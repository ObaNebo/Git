from django.shortcuts import render
from blog.models import Task  # Импортируем модель Task из другого приложения


def dashboard_view(request):
    tasks = Task.objects.all()
    return render(request, 'dashboard.html', {'title': 'Главная страница', 'tasks': tasks})

# def blog_view(request):

