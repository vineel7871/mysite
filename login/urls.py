from django.urls import path

from . import views

app_name = 'login'
urlpatterns = [
    path('', views.index, name='login_index'),
    path('login/', views.login, name='try_login'),
    path('create/', views.create_home, name="create_home"),
    path('create_account/', views.create_account, name="create_account")
]