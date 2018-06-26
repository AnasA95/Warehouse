# from django.conf import settings
from django.db import models
from django.contrib.auth.hashers import make_password
from django.utils import timezone


class WarehouseType(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Warehouse(models.Model):
    id = models.IntegerField(primary_key=True)
    created = models.DateTimeField(editable=False, null=True)
    last_modified = models.DateTimeField(editable=False, null=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    type = models.ForeignKey(WarehouseType, on_delete=models.CASCADE)
    capacity = models.IntegerField()
    remainingCapacity = models.IntegerField()

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.last_modified = timezone.now()
        return super(Warehouse, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id) + ' ' + self.name


class User(models.Model):
    USER_CHOICES = (
        ('user', 'User'),
        ('admin', 'Admin'),
        ('super_admin', 'Super Admin'),
    )
    id = models.IntegerField(primary_key=True)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(editable=False)
    last_modified = models.DateTimeField()
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    type = models.CharField(max_length=11, choices=USER_CHOICES, default='user')
    warehouseId = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    password = models.CharField(max_length=300)
    make_password(password)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.last_modified = timezone.now()
        return super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.fname


class Package(models.Model):
    id = models.IntegerField(primary_key=True)
    created = models.DateTimeField(editable=False, null=True)
    last_modified = models.DateTimeField()
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    type = models.CharField(max_length=30)
    wantedWarehouseType = models.ForeignKey(WarehouseType, on_delete=models.CASCADE)
    isFragile = models.BooleanField(default=False)
    warehouseId = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.last_modified = timezone.now()
        return super(Package, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.pk)


class IncomingPackage(models.Model):
    packageId = models.OneToOneField(Package, on_delete=models.CASCADE, primary_key=True)
    checkInTime = models.DateTimeField()
    userId = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)


class OutgoingPackage(models.Model):
    packageId = models.OneToOneField(Package, on_delete=models.CASCADE, primary_key=True)
    checkOutTime = models.DateTimeField(auto_now_add=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)


class Provider(models.Model):
    id = models.IntegerField(primary_key=True)
    created = models.DateTimeField(editable=False)
    last_modified = models.DateTimeField()
    name = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.last_modified = timezone.now()
        return super(Provider, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.pk) + ' ' + self.name


class Order(models.Model):
    id = models.IntegerField(primary_key=True)
    created = models.DateTimeField(editable=False)
    last_modified = models.DateTimeField()
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    providerId = models.ForeignKey(Provider, on_delete=models.CASCADE)
    packageId = models.ForeignKey(Package, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.last_modified = timezone.now()
        return super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.pk)


class Owner(models.Model):
    id = models.IntegerField(primary_key=True)
    created = models.DateTimeField(editable=False)
    last_modified = models.DateTimeField()
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.last_modified = timezone.now()
        return super(Owner, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.pk) + ' ' + self.name


class Customer(models.Model):
    id = models.IntegerField(primary_key=True)
    created = models.DateTimeField(editable=False)
    last_modified = models.DateTimeField()
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100, default="")

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.last_modified = timezone.now()
        return super(Customer, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.pk) + ' ' + self.name


class IncomingOrder(models.Model):
    id = models.OneToOneField(Order, on_delete=models.CASCADE, primary_key=True)
    pkgQty = models.IntegerField()
    ownerId = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)


class OutgoingOrder(models.Model):
    id = models.OneToOneField(Order, on_delete=models.CASCADE, primary_key=True)
    pkgQty = models.IntegerField()
    customerId = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)
