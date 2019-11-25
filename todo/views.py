from django.shortcuts import render
from todo.models import Task, CompletedTask, ArchivedTask
from django.utils import timezone
from django.db import DatabaseError


# Create your views here.
def index(request):
    context = {
        "tasks": Task.objects.all(),
        "completed_tasks": CompletedTask.objects.all()
    }
    return render(request, 'todo/index.html', context)


def add_task(request):
    error_message = None
    try:
        if len(request.POST['task_text']) > 120:
            error_message = "no of characters exceeded max length of 120"
        else:
            Task.objects.create(task=request.POST['task_text'], task_date=timezone.now())
    except DatabaseError:
        error_message = "database is not available please try again after some time"
    context = {
        "tasks": Task.objects.all(),
        "completed_tasks": CompletedTask.objects.all(),
        "error_message": error_message
    }
    return render(request, 'todo/index.html', context)


def complete_post(request):
    error_message = None
    for task_id in request.POST:
        if len(request.POST) < 2:
            error_message = "no tasks selected."
        try:
            task_id = int(task_id)
            t = Task.objects.get(pk=task_id)
            CompletedTask.objects.create(task=t.task, task_date=t.task_date, complete_date=timezone.now())
            Task.objects.get(pk=task_id).delete()
        except DatabaseError:
            error_message = "specified tasks does not exist in database"
        except ValueError:
            pass
    context = {
        "tasks": Task.objects.all(),
        "completed_tasks": CompletedTask.objects.all(),
        "error_message": error_message
    }
    return render(request, 'todo/index.html', context)


def complete_task(request, task_id):
    error_message = None
    try:
        t = Task.objects.get(pk=task_id)
        CompletedTask.objects.create(task=t.task, task_date=t.task_date, complete_date=timezone.now())
        Task.objects.get(pk=task_id).delete()
    except DatabaseError:
        error_message = "specified task does not exist"
    context = {
        "tasks": Task.objects.all(),
        "completed_tasks": CompletedTask.objects.all()
    }
    return render(request, 'todo/index.html', context)


def archive_post(request):
    error_message = None
    if len(request.POST) < 2:
        error_message = "no completed tasks selected to archive"
    for task_id in request.POST:
        try:
            task_id = int(task_id)
            t = CompletedTask.objects.get(pk=task_id)
            ArchivedTask.objects.create(task=t.task, task_date=t.task_date, complete_date=t.complete_date)
            CompletedTask.objects.get(pk=task_id).delete()
        except DatabaseError:
            error_message = "some selected tasks does not exist in database"
        except ValueError:
            pass
    context = {
        "tasks": Task.objects.all(),
        "completed_tasks": CompletedTask.objects.all(),
        "error_message": error_message
    }
    return render(request, 'todo/index.html', context)


def archive_task(request, task_id):
    error_message = None
    try:
        t = CompletedTask.objects.get(pk=task_id)
        ArchivedTask.objects.create(task = t.task, task_date=t.task_date, complete_date = t.complete_date)
        CompletedTask.objects.get(pk=task_id).delete()
    except DatabaseError:
        error_message = "specified task does not exist in completed tasks"
    context = {
        "tasks": Task.objects.all(),
        "completed_tasks": CompletedTask.objects.all(),
        "error_message": error_message
    }
    return render(request, 'todo/index.html', context)