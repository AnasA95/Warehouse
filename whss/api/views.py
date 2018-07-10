from rest_framework import generics
from .serializers import *


class WarehouseTypeList(generics.ListCreateAPIView):
    queryset = WarehouseType.objects.all()
    serializer_class = WarehouseTypeSerializer


class WarehouseTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WarehouseType.objects.all()
    serializer_class = WarehouseTypeSerializer


class WarehouseList(generics.ListCreateAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class WarehouseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class OwnerList(generics.ListCreateAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class OwnerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ProviderList(generics.ListCreateAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ProviderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class IncomingOrderList(generics.ListCreateAPIView):
    queryset = IncomingOrder.objects.all()
    serializer_class = IncomingOrderSerializer


class IncomingOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = IncomingOrder.objects.all()
    serializer_class = IncomingOrderSerializer


class OutgoingOrderList(generics.ListCreateAPIView):
    queryset = OutgoingOrder.objects.all()
    serializer_class = OutgoingOrderSerializer


class OutgoingOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OutgoingOrder.objects.all()
    serializer_class = OutgoingOrderSerializer


class PackageList(generics.ListCreateAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer


class PackageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer


class BoxList(generics.ListCreateAPIView):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer


class BoxDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer


class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
