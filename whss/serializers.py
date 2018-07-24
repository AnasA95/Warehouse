from rest_framework import serializers
from .models import *


class WarehouseTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = WarehouseType
        fields = [
            'pk',
            'name',
        ]
        read_only_fields = ['pk']


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
            'remaining_capacity'
        ]
        read_only_fields = ['created', 'last_modified', 'pk']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'pk',
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
        read_only_fields = ['date_joined', 'last_login', 'pk']


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = [
            'pk',
            'username',
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
            'username',
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
            'username',
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
            'tracking_number',
            'created',
            'last_modified',
            'type',
            'is_fragile',
            'warehouse',
            'is_checked',
            'order',
        ]
        read_only_fields = ['created', 'last_modified', 'pk']


class IncomingOrderSerializer(serializers.ModelSerializer):
    packages = PackageSerializer(many=True)

    class Meta:
        model = IncomingOrder
        fields = [
            'pk',
            'tracking_number',
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
            'tracking_number',
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
            'tracking_number',
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
            'tracking_number',
            'created',
            'last_modified',
            'packageId',
        ]
        read_only_fields = ['created', 'last_modified', 'pk']

