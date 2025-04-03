from django.urls import path

from . import views

urlpatterns = [
  path('register', views.register, name='register'),
  path('admin/register', views.admin_register, name='admin_register'),
  path('login', views.login, name='login'),
  path('logout', views.logout, name='logout'),
  path('dashboard', views.dashboard, name='dashboard')
]
