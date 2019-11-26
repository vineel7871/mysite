from django.db import models


# Create your models here.
class BlogPost(models.Model):
    # basic data
    header = models.TextField(max_length=80)
    content = models.TextField()
    author = models.CharField(max_length=40)
    status = models.CharField(max_length=5)
    # meta data
    title = models.TextField(max_length=80, default=header)
    meta_description = models.TextField(max_length=160, default=None)
    meta_keywords = models.TextField(max_length=160, default=None)
    # availability
    pubtime = models.DateTimeField()
    available_from = models.DateTimeField(default=None)
    available_till = models.DateTimeField(default=None)
