from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(request, 'login/index.html')


def login(request):
    pass


def create_home(request):
    return render(request, 'login/create.html')


def create_account(request):
    if request.POST['password'] != request.POST['password_1']:
        context = {
            'error_message': "passwords doesnot match"
        }
        return render(request, 'login/create.html', context)
    else:
        user = User.objects.create_user(request.POST['user_name'], request.POST['emai_id'], request.POST['password'])
        user.first_name = request.POST["first_name"]
        user.last_name = request.POST['last_name']
