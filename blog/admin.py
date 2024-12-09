from django.contrib import admin
from .models import MyModel

@adnin.register(MyModel)
class MyModelAdmin(admin.MyModel):
    list.display = ('id', 'name', 'created_at')
    list.filter = ('created_at',)
    search_fields = ('name',)
    ordering = ('-created_at',)
