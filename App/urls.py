
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('projects/', views.ProjectListCreate.as_view(), name='project-list'),
    path('projects/<int:pk>/', views.ProjectDetail.as_view(), name='project-detail'),
    path('tasks/', views.TaskListCreate.as_view(), name='task-list'),
    path('tasks/<int:pk>/', views.TaskDetail.as_view(), name='task-detail'),
    path('members/', views.MemberListCreate.as_view(), name='member-list'),
    path('members/<int:pk>/', views.MemberDetail.as_view(), name='member-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
