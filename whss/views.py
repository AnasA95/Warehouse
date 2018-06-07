from django.shortcuts import render
from .models import User


def index(request):
    users = User.objects.all()  # [:10] first 10 users
    context = {
        'title': 'Warehouse System',
        'users': users
    }
    return render(request, 'whss/index.html', context)


def details(request, id):
    user = User.objects.get(id=id)
    return render(request, 'whss/details.html', {'user': user})
