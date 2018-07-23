from rest_framework import serializers
from .models import *


class WarehouseTypeSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = WarehouseType
        fields = [
            'url',
            'name',
            'user'
        ]


class WarehouseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Warehouse
        fields = [
            'created',
            'last_modified',
            'name',
            'location',
            'type',
            'capacity',
            'remainingCapacity'
        ]
        read_only_fields = ['created', 'last_modified']


class UserSerializer(serializers.ModelSerializer):
    """snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')"""

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'date_joined',
            'last_login',
            'first_name',
            'last_name',
            'type',
            'warehouse',
            'password',
        ]

        """def validate_first_name(self, value):
            user = User.objects.filter(first_name__iexact=value)
            if self.model:
                user = user.exclude(pk=self.model.pk)
            if user.exists():
                raise serializers.ValidationError(str(self.read_only_fields) + "field must be unique")
            return value"""


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = [
            'pk',
            'created',
            'last_modified',
            'name'
            'location',
        ]
        read_only_fields = ['created', 'last_modified', 'pk']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'pk',
            'created',
            'last_modified',
            'name'
            'location',
        ]
        read_only_fields = ['created', 'last_modified', 'pk']


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = [
            'pk',
            'created',
            'last_modified',
            'name',
        ]
        read_only_fields = ['created', 'last_modified', 'pk']


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = [
            'pk',
            'created',
            'last_modified',
            # 'user',
            'type',
            'isFragile',
            'warehouseId',
            'isChecked',
            'orderId',
        ]
        read_only_fields = ['created', 'last_modified', 'pk']


class IncomingOrderSerializer(serializers.ModelSerializer):
    packages = PackageSerializer(many=True)

    class Meta:
        model = IncomingOrder
        fields = [
            'pk',
            'created',
            'last_modified',
            'providerId',
            'ownerId',
            'packages'
        ]
        read_only_fields = ['created', 'last_modified', 'pk']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            'pk',
            'created',
            'last_modified',
            'name',
            'qty',
            'price',
            'isExist',
            'isChecked',
            'boxId',
            'orderId',
        ]
        read_only_fields = ['created', 'last_modified', 'pk']


class OutgoingOrderSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = OutgoingOrder
        fields = [
            'pk',
            'created',
            'last_modified',
            'providerId',
            'customerId',
            'items'
        ]
        read_only_fields = ['created', 'last_modified', 'pk']


class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = [
            'pk',
            'created',
            'last_modified',
            'packageId',
        ]
        read_only_fields = ['created', 'last_modified', 'pk']

