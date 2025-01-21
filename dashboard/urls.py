from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('about', views.about_view, name='about'),
    path('autor', views.autor_view, name='autor'),
    # path('others/katalog', views.katalog_view, name='katalog'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]