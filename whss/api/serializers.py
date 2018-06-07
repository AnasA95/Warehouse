from rest_framework import serializers
from whss.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'pk',
            'user',
            'fname',
            'lname',
            'type',
            'warehouseId',
            'password',
        ]
        read_only_fields = ['pk']

        def validate_fname(self, value):
            user = User.objects.filter(fname__iexact=value)
            if self.model:
                user = user.exclude(pk=self.model.pk)
            if user.exists():
                raise serializers.ValidationError(str(self.read_only_fields) + "field must be unique")
            return value
