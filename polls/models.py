from django.db import models
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    question_text = models.TextField(max_length=200)
    pub_date = models.DateTimeField(timezone.now)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

