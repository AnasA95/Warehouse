from django.shortcuts import render
# from django.http import HttpResponse
from .models import User


def index(request):
    # return HttpResponse('Hello world')
    users = User.objects.all()  # [:10] first 10 users
    context = {
        'title': 'Warehouse System',
        'users': users
    }
    return render(request, 'whss/index.html', context)


def details(request, id):
    user = User.objects.get(id=id)

    context = {
        'user': user
    }

    return render(request, 'whss/details.html', context)
