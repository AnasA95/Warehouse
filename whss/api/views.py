from django.db.models import Q
from rest_framework import generics, mixins
from whss.models import User
from .serializers import UserSerializer
from .permissions import IsOwnerOrReadOnly


class UserAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        user = User.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            user = user.filter(Q(fname__icontains=query) | Q(lname__icontains=query)).distinct()
        return user

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.patch(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.put(request, *args, **kwargs)

class UserRudAPIView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()
