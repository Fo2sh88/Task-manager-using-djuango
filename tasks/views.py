from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def task_list(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tasks:list")
    else:
        form = TaskForm()
    tasks = Task.objects.order_by("-created_at")
    return render(request, "tasks/task_list.html", {"tasks": tasks, "form": form})

def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("tasks:list")
    else:
        form = TaskForm(instance=task)
    return render(request, "tasks/task_edit.html", {"form": form, "task": task})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.delete()
        return redirect("tasks:list")
    return render(request, "tasks/task_confirm_delete.html", {"task": task})

def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect("tasks:list")