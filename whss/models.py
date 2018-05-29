from django.db import models
from datetime import datetime
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


class User(models.Model):
    USER_CHOICES = (
        ('user', 'User'),
        ('admin', 'Admin'),
        ('super_admin', 'Super Admin'),
    )
    id = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    type = models.CharField(max_length=11, choices=USER_CHOICES, default='user')
    warehouseId = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    password = models.CharField(max_length=300)
    password = make_password(password)

    def __str__(self):
        return self.fname


class Package(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=30)
    warehouseType = models.ForeignKey(WarehouseType, on_delete=models.CASCADE)
    isFragile = models.BooleanField(default=False)
    warehouseId = models.ForeignKey(Warehouse, on_delete=models.CASCADE)


class PackageIn(models.Model):
    packageId = models.ForeignKey(Package, on_delete=models.CASCADE, blank=True, null=True)
    checkInTime = models.DateTimeField(default=datetime.now)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)


class PackageOut(models.Model):
    packageId = models.ForeignKey(Package, on_delete=models.CASCADE, blank=True, null=True)
    checkOutTime = models.DateTimeField(default=datetime.now)
    userId = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


class Provider(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)


class Order(models.Model):
    id = models.IntegerField(primary_key=True)
    providerId = models.ForeignKey(Provider, on_delete=models.CASCADE)
    packageId = models.ForeignKey(Package, on_delete=models.CASCADE)


class IncomingOrder(models.Model):
    id = models.ForeignKey(Order, on_delete=models.CASCADE, primary_key=True)
    pkgQty = models.IntegerField()


class OutgoingOrder(models.Model):
    id = models.ForeignKey(Order, on_delete=models.CASCADE, primary_key=True)
    pkgQty = models.IntegerField()


class Owner(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    orderId = models.ForeignKey(IncomingOrder, on_delete=models.CASCADE)


class Customer(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    orderId = models.ForeignKey(OutgoingOrder, on_delete=models.CASCADE)

