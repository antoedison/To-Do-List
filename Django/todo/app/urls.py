from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard,name ='dashboard'),
    path('dashboard/add_task/', views.add_task, name = 'add_task'),
    path('dashboard/view_task/', views.view_task,name = 'view_task'),
    path('dashboard/completed_task/', views.completed_task, name = 'completed_task'),
    path('dashboard/edit_task/', views.edit_task,name = 'edit_task'),

]