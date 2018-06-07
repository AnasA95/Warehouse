from django.conf import settings
from django.db import models
from django.contrib.auth.hashers import make_password


class WarehouseType(models.Model):
    name = models.CharField(max_length=10)


class Warehouse(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    type = models.ForeignKey(WarehouseType, on_delete=models.CASCADE)
    capacity = models.IntegerField()
    remainingCapacity = models.IntegerField()

    def __str__(self):
        return str(self.id)


class User(models.Model):
    USER_CHOICES = (
        ('user', 'User'),
        ('admin', 'Admin'),
        ('super_admin', 'Super Admin'),
    )
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    type = models.CharField(max_length=11, choices=USER_CHOICES, default='user')
    warehouseId = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    password = models.CharField(max_length=300)
    make_password(password)

    def __str__(self):
        return self.fname


class Package(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=30)
    warehouseType = models.ForeignKey(WarehouseType, on_delete=models.CASCADE)
    isFragile = models.BooleanField(default=False)
    warehouseId = models.ForeignKey(Warehouse, on_delete=models.CASCADE)


class IncomingPackage(models.Model):
    packageId = models.OneToOneField(Package, on_delete=models.CASCADE, primary_key=True)
    checkInTime = models.DateTimeField(auto_now_add=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)


class OutgoingPackage(models.Model):
    packageId = models.OneToOneField(Package, on_delete=models.CASCADE, primary_key=True)
    checkOutTime = models.DateTimeField(auto_now_add=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)


class Provider(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)


class Order(models.Model):
    id = models.IntegerField(primary_key=True)
    providerId = models.ForeignKey(Provider, on_delete=models.CASCADE)
    packageId = models.ForeignKey(Package, on_delete=models.CASCADE)


class IncomingOrder(models.Model):
    id = models.OneToOneField(Order, on_delete=models.CASCADE, primary_key=True)
    pkgQty = models.IntegerField()


class OutgoingOrder(models.Model):
    id = models.OneToOneField(Order, on_delete=models.CASCADE, primary_key=True)
    pkgQty = models.IntegerField()


class Owner(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    orderId = models.ForeignKey(IncomingOrder, on_delete=models.CASCADE)


class Customer(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    orderId = models.ForeignKey(OutgoingOrder, on_delete=models.CASCADE)
