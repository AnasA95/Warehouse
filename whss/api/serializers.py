from rest_framework import serializers
from whss.models import *


class WarehouseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarehouseType
        fields = [
            'name'
        ]


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = [
            'pk',
            'created',
            'last_modified',
            'name',
            'location',
            'type',
            'capacity',
            'remainingCapacity'
        ]
        read_only_fields = ['created', 'last_modified', 'pk']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'pk',
            # 'user',
            'created',
            'last_modified',
            'fname',
            'lname',
            'type',
            'warehouseId',
            'password',
        ]
        read_only_fields = ['created', 'last_modified', 'pk']

        """def validate_fname(self, value):
            user = User.objects.filter(fname__iexact=value)
            if self.model:
                user = user.exclude(pk=self.model.pk)
            if user.exists():
                raise serializers.ValidationError(str(self.read_only_fields) + "field must be unique")
            return value"""


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = [
            'pk',
            'created',
            'last_modified',
            # 'user',
            'type',
            'wantedWarehouseType',
            'isFragile',
            'warehouseId',
        ]
        read_only_fields = ['created', 'last_modified', 'pk']


class IncomingPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomingPackage
        fields = [
            'pk',
            'checkInTime',
            'userId',
        ]
        read_only_fields = ['pk']


class OutgoingPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutgoingPackage
        fields = [
            'pk',
            'checkOutTime',
            'userId',
        ]
        read_only_fields = ['pk']


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


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'pk',
            'created',
            'last_modified',
            # 'user',
            'providerId',
            'packageId',
        ]
        read_only_fields = ['created', 'last_modified', 'pk']


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


class IncomingOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomingOrder
        fields = [
            'pk',
            'pkgQty',
            'ownerId',
        ]
        read_only_fields = ['pk']


class OutgoingOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutgoingOrder
        fields = [
            'pk',
            'pkgQty',
            'customerId',
        ]
        read_only_fields = ['pk']
