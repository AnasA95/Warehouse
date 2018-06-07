from django.contrib import admin
from .models import *


admin.site.register(User)
admin.site.register(Owner)
admin.site.register(Provider)
admin.site.register(Customer)
admin.site.register(Warehouse)
admin.site.register(WarehouseType)
admin.site.register(Package)
admin.site.register(IncomingPackage)
admin.site.register(OutgoingPackage)
admin.site.register(Order)
admin.site.register(IncomingOrder)
admin.site.register(OutgoingOrder)
