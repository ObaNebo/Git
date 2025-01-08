from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('about', views.about_view, name='about'),
    path('autor', views.autor_view, name='autor'),
    # path('', views.blog_view, name='blog'),
]