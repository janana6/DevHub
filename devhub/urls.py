from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_board, name='project_board'),
    path('journal/', views.journal_list, name='journal_list'),
    path('projects/add/', views.project_create, name='project_create'),
    path('journal/add/', views.journal_create, name='journal_create'),
]
