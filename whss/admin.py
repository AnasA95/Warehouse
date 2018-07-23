from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class WarehouseTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'location')
    search_fields = ('id', 'name')
    list_filter = ('created', 'last_modified')


class OwnerCustomerProviderAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    search_fields = ('id', 'name')
    list_filter = ('created', 'last_modified')


class IncomingOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'ownerId_name', 'status', 'userId', 'checkTime')
    search_fields = ('id', 'ownerId_id', 'ownerId_name')
    list_filter = ('created', 'last_modified', 'status')

    def ownerId_name(self, obj):
        return obj.ownerId.name

    def ownerId_id(self, obj):
        return obj.ownerId.id


class OutgoingOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customerId_name', 'status', 'userId', 'checkTime')
    search_fields = ('id', 'customerId_id', 'customerId_name')
    list_filter = ('created', 'last_modified', 'status')

    def customerId_name(self, obj):
        return obj.ownerId.name

    def customerId_id(self, obj):
        return obj.ownerId.id


admin.site.register(WarehouseType, WarehouseTypeAdmin)
admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(Owner, OwnerCustomerProviderAdmin)
admin.site.register(Customer, OwnerCustomerProviderAdmin)
admin.site.register(Provider, OwnerCustomerProviderAdmin)
admin.site.register(IncomingOrder, IncomingOrderAdmin)
admin.site.register(OutgoingOrder, OutgoingOrderAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Package)
admin.site.register(Box)
admin.site.register(Item)
