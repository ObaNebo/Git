from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied


def is_admin_user(user):

    if user.is_superuser or user.groups.filter(name='admin').exists():
        return True
    raise PermissionDenied("Доступ запрещен")  # Возвращает ошибку 403

admin_required = user_passes_test(is_admin_user)


@admin_required
def index(request):
   
   search_query = request.GET.get('search', '')
   if search_query:
        tasks = Task.objects.filter(title__icontains=search_query) | Task.objects.filter(task__icontains=search_query)
   else:
        tasks = Task.objects.all()
   return render(request, 'blog/index.html', {'title': 'Панель управления', 'tasks': tasks})

def custom_permission_denied_view(request, exception=None):
     return render(request, 'errors/403.html', status=403)

def custom_page_not_found_view(request, exception=None):
    return render(request, 'errors/404.html', status=404)


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
