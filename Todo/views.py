from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        task.title = request.POST.get("title")
        task.description = request.POST.get("description")
        task.save()
        return redirect('home')  # или куда надо

    return render(request, 'update_task.html', {'task': task})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)  # Получаем задачу по ID
    if request.method == 'POST':
        task.delete()
        return redirect('home')  # Перенаправляем на главную страницу после удаления
    return render(request, 'delete_task.html', {'task': task})  # Передаем задачу в шаблон для подтверждения удаления

def get_task(request):
    tasks = Task.objects.all()
    return render(request, 'task.html', {'tasks': tasks})

@csrf_exempt
def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Task.objects.create(title=title, description=description)
        return redirect('home')
    return render(request, 'create_task.html')

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_detail.html', {'task': task})
