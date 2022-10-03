from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def main_page(request):
    return render(request, 'base/base.html')


@login_required(login_url='auth:register')
def users_page(request):
    users = User.objects.all()
    return render(request, 'base/users.html', {"users" : users})