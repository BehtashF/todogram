from django.shortcuts import render,redirect, get_object_or_404
from .forms import TaskForm
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='accounts:login')
def create_task(request):
    tasks = Task.objects.all()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.user = request.user
            form.save()
            messages.success(request, 'your new task added to list', 'success')
            return redirect("todo:create_task")
    else:
        form = TaskForm()

    context = {
        'form' : form,
        'tasks' : tasks,
    }
    return render(request, 'todo/create_task.html', context)


@login_required(login_url='accounts:login')
def update_task(request, id=None):
    tasks = Task.objects.all()
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'your task has been updated', 'success')
            return redirect("todo:create_task")

    else:
        form = TaskForm(instance=task)

    context = {
        'form' : form,
        'tasks' : tasks,
    }
    return render(request, 'todo/update_task.html', context)


# ‌show all trash tasks + function for move task to trash and restore from there

@login_required(login_url='accounts:login')
def trash_tasks(request):
    trash = Trash.objects.all()
    context = {
        'trash':trash,
    }
    return render(request, 'todo/trash.html', context)

@login_required(login_url='accounts:login')
def delete_task(request, id=None):
    task = get_object_or_404(Task, id=id)
    Trash.objects.create(user=request.user, title=task.title, description=task.description)
    task.delete()
    messages.success(request, 'task deleted and move to trash', 'success')
    return redirect("todo:create_task")


@login_required(login_url='accounts:login')
def restore_task(request, id=None):
    trash_task = get_object_or_404(Trash, id=id)
    Task.objects.create(user=request.user, title=trash_task.title, description=trash_task.description)
    trash_task.delete()
    messages.success(request, 'task restored' , 'success')
    return redirect("todo:trash_tasks")

def complete_remove(request, id=None):
    trash_task = get_object_or_404(Trash, id=id)
    trash_task.delete()
    messages.success(request, f'"{trash_task.title}" completely removed' , 'success')
    return redirect("todo:trash_tasks")

# show all archive tasks + ‌function for move task to archive and restore from there

@login_required(login_url='accounts:login')
def archive_tasks(request):
    archives = Archive.objects.all()
    context = {
        'archives':archives,
    }
    return render(request, 'todo/archive.html', context)

def archive_task(request, id=None):
    task = get_object_or_404(Task, id=id)
    Archive.objects.create(user=request.user, title=task.title, description=task.description)
    task.delete()
    messages.success(request, 'task moved to archive section', 'success')
    return redirect("todo:create_task")

@login_required(login_url='accounts:login')
def archive_restore_tasks(request, id=None):
    archive_task = get_object_or_404(Archive, id=id)
    Task.objects.create(user=request.user, title=archive_task.title, description=archive_task.description)
    archive_task.delete()
    messages.success(request, 'task restored' , 'success')
    return redirect("todo:archive_tasks")
