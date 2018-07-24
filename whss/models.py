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


class Info(models.Model):
    created = models.DateTimeField(editable=False, null=True, blank=True)
    last_modified = models.DateTimeField(editable=False, null=True, blank=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)

    class Meta:
        abstract = True
        ordering = ['created']


class WarehouseType(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Warehouse(Info):
    type = models.ForeignKey(WarehouseType, on_delete=models.CASCADE)
    capacity = models.IntegerField()
    remaining_capacity = models.IntegerField()

    def __str__(self):
        return str(self.id) + ' ' + self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.last_modified = timezone.now()
        return super(Warehouse, self).save(*args, **kwargs)


class User(AbstractUser):
    USER_CHOICES = (
        ('user', 'User'),
        ('admin', 'Admin'),
        ('super_admin', 'Super Admin'),
    )
    type = models.CharField(max_length=11, choices=USER_CHOICES, default='user')
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.first_name


class Owner(Info):
    username = models.CharField(max_length=10)

    def __str__(self):
        return str(self.pk) + ' ' + self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.last_modified = timezone.now()
        return super(Owner, self).save(*args, **kwargs)


class Customer(Info):
    username = models.CharField(max_length=10)

    def __str__(self):
        return str(self.pk) + ' ' + self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.last_modified = timezone.now()
        return super(Customer, self).save(*args, **kwargs)


class Provider(Info):
    username = models.CharField(max_length=10)

    def __str__(self):
        return str(self.pk) + ' ' + self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.last_modified = timezone.now()
        return super(Provider, self).save(*args, **kwargs)


class Order(models.Model):
    tracking_number = models.CharField(max_length=10)
    created = models.DateTimeField(editable=False, null=True, blank=True)
    last_modified = models.DateTimeField(editable=False, null=True, blank=True)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    check_time = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.last_modified = timezone.now()
        return super(Order, self).save(*args, **kwargs)


class IncomingOrder(Order):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)


class OutgoingOrder(Order):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)


class Package(models.Model):
    tracking_number = models.CharField(max_length=10)
    created = models.DateTimeField(editable=False, null=True, blank=True)
    last_modified = models.DateTimeField(editable=False, null=True, blank=True)
    type = models.ForeignKey(WarehouseType, on_delete=models.CASCADE)
    is_fragile = models.BooleanField(default=False)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    is_checked = models.BooleanField()
    order = models.ForeignKey(IncomingOrder, related_name='packages', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.last_modified = timezone.now()
        return super(Package, self).save(*args, **kwargs)


class Box(SizeAndWeight):
    tracking_number = models.CharField(max_length=10)
    created = models.DateTimeField(editable=False, null=True, blank=True)
    last_modified = models.DateTimeField(editable=False, null=True, blank=True)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Boxes'

    def __str__(self):
        return str(self.pk)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.last_modified = timezone.now()
        return super(Box, self).save(*args, **kwargs)


class Item(SizeAndWeight):
    tracking_number = models.CharField(max_length=10)
    created = models.DateTimeField(editable=False, null=True, blank=True)
    last_modified = models.DateTimeField(editable=False, null=True, blank=True)
    name = models.CharField(max_length=50)
    qty = models.IntegerField(default=0)
    price = models.IntegerField()
    is_exist = models.BooleanField(default=False)
    is_checked = models.BooleanField()
    box = models.ForeignKey(Box, on_delete=models.CASCADE)
    order = models.ForeignKey(OutgoingOrder, related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.last_modified = timezone.now()
        return super(Item, self).save(*args, **kwargs)
