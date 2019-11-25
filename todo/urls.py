from django.urls import path
from . import views

app_name = "todo"
urlpatterns = [
    path("", views.index, name="todo_index"),
    path("add/", views.add_task, name="add_task"),
    path("complete/<int:task_id>/", views.complete_task, name="complete_task"),
    path("complete/post/", views.complete_post, name="complete_post"),
    path("archive/<int:task_id>/", views.archive_task, name="archive_task"),
    path("archive/post/", views.archive_post, name="archive_post")
]