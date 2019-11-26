from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path("", views.index, name="blog_index"),
    path("<int:blog_id>/", views.blog_page, name="blog_page")
]