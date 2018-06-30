from django.contrib import admin
from .models import *


admin.site.register(WarehouseType)
admin.site.register(Warehouse)
admin.site.register(User)
admin.site.register(Owner)
admin.site.register(Customer)
admin.site.register(Provider)
admin.site.register(IncomingOrder)
admin.site.register(OutgoingOrder)
admin.site.register(Package)
admin.site.register(Box)
admin.site.register(Item)
