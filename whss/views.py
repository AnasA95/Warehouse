from django.shortcuts import render
from .models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer


class UserList(APIView):

    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self):
        pass


def index(request):
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
