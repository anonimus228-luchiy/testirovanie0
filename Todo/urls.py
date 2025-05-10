from django.urls import path
from .views import TaskListCreateView, TaskDetailUpdateDeleteView

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task_list_create'),
    path('tasks/<int:pk>/', TaskDetailUpdateDeleteView.as_view(), name='task_detail_update_delete'),
]
