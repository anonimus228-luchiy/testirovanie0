from django.contrib import admin
from django.urls import path
from Todo.views import get_task, task_create, task_update, task_detail, task_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', get_task, name='home'),
    path('tasks/create/', task_create, name='task_create'),
    path('task/<int:pk>/', task_detail, name='task_detail'),  # Страница для просмотра задачи
    path('task/<int:pk>/update/', task_update, name='task_update'),  # Страница для обновления задачи
    path('task/<int:pk>/delete/', task_delete, name='task_delete'),  # Страница для удаления задачи
]
