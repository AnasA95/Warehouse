from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class SizeAndWeight(models.Model):
    length = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()

    class Meta:
        abstract = True


class WarehouseType(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Warehouse(models.Model):
    created = models.DateTimeField(editable=False, null=True, blank=True)
    last_modified = models.DateTimeField(editable=False, null=True, blank=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    type = models.ForeignKey(WarehouseType, on_delete=models.CASCADE)
    capacity = models.IntegerField()
    remainingCapacity = models.IntegerField()

    class Meta:
        ordering = ['created']

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.last_modified = timezone.now()
        return super(Warehouse, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id) + ' ' + self.name


class User(AbstractUser):
    USER_CHOICES = (
        ('user', 'User'),
        ('admin', 'Admin'),
        ('super_admin', 'Super Admin'),
    )
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    type = models.CharField(max_length=11, choices=USER_CHOICES, default='user')
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.first_name


class Owner(models.Model):
    id = models.IntegerField(primary_key=True)
    created = models.DateTimeField(editable=False, null=True, blank=True)
    last_modified = models.DateTimeField(null=True, blank=True)
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
    created = models.DateTimeField(editable=False, null=True, blank=True)
    last_modified = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100, default="")

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.last_modified = timezone.now()
        return super(Customer, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.pk) + ' ' + self.name


class Provider(models.Model):
    id = models.IntegerField(primary_key=True)
    created = models.DateTimeField(editable=False, null=True, blank=True)
    last_modified = models.DateTimeField(null=True, blank=True)
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
    created = models.DateTimeField(editable=False, null=True, blank=True)
    last_modified = models.DateTimeField(editable=False, null=True, blank=True)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    providerId = models.ForeignKey(Provider, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    checkTime = models.DateTimeField(blank=True, null=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    warehouseId = models.ForeignKey(Warehouse, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.last_modified = timezone.now()
        return super(Order, self).save(*args, **kwargs)


class IncomingOrder(Order):
    ownerId = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)


class OutgoingOrder(Order):
    customerId = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)


class Package(models.Model):
    id = models.IntegerField(primary_key=True)
    created = models.DateTimeField(editable=False, null=True, blank=True)
    last_modified = models.DateTimeField(null=True, blank=True)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    type = models.ForeignKey(WarehouseType, on_delete=models.CASCADE)
    isFragile = models.BooleanField(default=False)
    warehouseId = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    isChecked = models.BooleanField()
    orderId = models.ForeignKey(IncomingOrder, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.last_modified = timezone.now()
        return super(Package, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.pk)


class Box(SizeAndWeight):
    id = models.IntegerField(primary_key=True)
    created = models.DateTimeField(editable=False, null=True, blank=True)
    last_modified = models.DateTimeField(null=True, blank=True)
    packageId = models.ForeignKey(Package, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Boxes'

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.last_modified = timezone.now()
        return super(Box, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.pk)


class Item(SizeAndWeight):
    id = models.IntegerField(primary_key=True)
    created = models.DateTimeField(editable=False, null=True, blank=True)
    last_modified = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=50)
    qty = models.IntegerField(default=0)
    price = models.IntegerField()
    isExist = models.BooleanField(default=False)
    isChecked = models.BooleanField()
    boxId = models.ForeignKey(Box, on_delete=models.CASCADE)
    orderId = models.ForeignKey(OutgoingOrder, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.last_modified = timezone.now()
        return super(Item, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
