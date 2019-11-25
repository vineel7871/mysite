from django.shortcuts import render
from todo.models import Task, CompletedTask, ArchivedTask
from django.utils import timezone


# Create your views here.
def index(request):
    context = {
        "tasks": Task.objects.all(),
        "completed_tasks": CompletedTask.objects.all()
    }
    return render(request, 'todo/index.html', context)


def add_task(request):
    Task.objects.create(task=request.POST['task_text'], task_date=timezone.now())
    context = {
        "tasks": Task.objects.all(),
        "completed_tasks": CompletedTask.objects.all()
    }
    return render(request, 'todo/index.html', context)


def complete_post(request):
    import pdb
    # pdb.set_trace()
    for task_id in request.POST:
        try:
            task_id = int(task_id)
            t = Task.objects.get(pk=task_id)
            CompletedTask.objects.create(task=t.task, task_date=t.task_date, complete_date=timezone.now())
            Task.objects.get(pk=task_id).delete()
        except (ValueError, Exception):
            pass

    context = {
        "tasks": Task.objects.all(),
        "completed_tasks": CompletedTask.objects.all()
    }
    return render(request, 'todo/index.html', context)


def complete_task(request, task_id):
    t = Task.objects.get(pk=task_id)
    CompletedTask.objects.create(task=t.task, task_date=t.task_date, complete_date=timezone.now())
    Task.objects.get(pk=task_id).delete()
    context = {
        "tasks": Task.objects.all(),
        "completed_tasks": CompletedTask.objects.all()
    }
    return render(request, 'todo/index.html', context)


def archive_post(request):
    for task_id in request.POST:
        try:
            task_id = int(task_id)
            t = CompletedTask.objects.get(pk=task_id)
            ArchivedTask.objects.create(task=t.task, task_date=t.task_date, complete_date=t.complete_date)
            CompletedTask.objects.get(pk=task_id).delete()
        except (ValueError,Exception):
            pass
    context = {
        "tasks": Task.objects.all(),
        "completed_tasks": CompletedTask.objects.all()
    }
    return render(request, 'todo/index.html', context)


def archive_task(request, task_id):
    t = CompletedTask.objects.get(pk=task_id)
    ArchivedTask.objects.create(task = t.task, task_date=t.task_date, complete_date = t.complete_date)
    CompletedTask.objects.get(pk=task_id).delete()
    context = {
        "tasks": Task.objects.all(),
        "completed_tasks": CompletedTask.objects.all()
    }
    return render(request, 'todo/index.html', context)