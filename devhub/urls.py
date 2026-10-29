from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_board, name='project_board'),
    path('register/', views.register, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('journal/', views.journal_list, name='journal_list'),
    path('projects/add/', views.project_create, name='project_create'),
    path('projects/<int:pk>/edit/', views.project_edit, name='project_edit'),
    path('journal/add/', views.journal_create, name='journal_create'),
]
