from django.contrib import admin
from todo.models import Task, CompletedTask, ArchivedTask

# Register your models here.
admin.site.register(Task)
admin.site.register(CompletedTask)
admin.site.register(ArchivedTask)