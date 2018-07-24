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
    list_display = ('id', 'owner_name', 'status', 'user', 'check_time')
    search_fields = ('id', 'owner_id', 'owner_name')
    list_filter = ('created', 'last_modified', 'status')

    def owner_name(self, obj):
        return obj.owner.name

    def owner_id(self, obj):
        return obj.owner.id


class OutgoingOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'status', 'user', 'check_time')
    search_fields = ('id', 'customer_id', 'customer_name')
    list_filter = ('created', 'last_modified', 'status')

    def customer_name(self, obj):
        return obj.owner.name

    def customer_id(self, obj):
        return obj.owner.id


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
