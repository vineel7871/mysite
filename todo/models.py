from django.db import models


# Create your models here.
class Task(models.Model):
    task = models.TextField(max_length=150)
    task_date = models.DateTimeField()

    def __str__(self):
        return self.task


class CompletedTask(models.Model):
    task = models.TextField(max_length=150)
    task_date = models.DateTimeField()
    complete_date = models.DateTimeField()

    def __str__(self):
        return self.task


class ArchivedTask(models.Model):
    task = models.TextField(max_length=150)
    task_date = models.DateTimeField()
    complete_date = models.DateTimeField()

    def __str__(self):
        return self.task