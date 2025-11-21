from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('create/', views.ProjectCreate.as_view(), name='create'),
    path('<int:pk>/', views.ProjectDetail.as_view(), name='detail'),
    path('<int:pk>/join/', views.join_project, name='join'),
    path('<int:pk>/edit/', views.ProjectUpdate.as_view(), name='edit'),
    path('<int:pk>/delete/', views.ProjectDelete.as_view(), name='delete'),
]