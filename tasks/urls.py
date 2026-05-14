from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('tasks/', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('update/<int:id>/', views.task_update, name='task_update'),
    path('delete/<int:id>/', views.task_delete, name='task_delete'),
    path('status/<int:id>/', views.update_status, name='update_status'),
]