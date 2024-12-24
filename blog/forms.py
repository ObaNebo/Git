from .models import Task
from django.forms import ModelForm
from django import forms


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'task']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название задачи'}),
            'task': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание задачи'}),
        }