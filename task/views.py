from django.shortcuts import render

def get_task(request):
    return render(request, 'task.html')

def task_detail(request):
    return render(request, 'task_detail.html')

def task_update(request):
    return render(request, 'task_update.html')

def task_delete(request):
    return render(request, 'task_delete.html')

def task_create(request):
    return render(request, 'task_create.html')