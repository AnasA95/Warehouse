from rest_framework import generics
from .serializers import *
from .permissions import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
# from rest_framework import renderers


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'warehousetypes': reverse('warehousetype-list', request=request, format=format),
        'warehouses': reverse('warehouse-list', request=request, format=format),
        'users': reverse('user-list', request=request, format=format),
        'owners': reverse('owner-list', request=request, format=format),
        'customers': reverse('customer-list', request=request, format=format),
        'providers': reverse('provider-list', request=request, format=format),
        'incomingOrders': reverse('incomingorder-list', request=request, format=format),
        'outgoingOrders': reverse('outgoingorder-list', request=request, format=format),
        'packages': reverse('package-list', request=request, format=format),
        'boxes': reverse('box-list', request=request, format=format),
        'items': reverse('item-list', request=request, format=format),
    })


class WarehouseTypeList(generics.ListCreateAPIView):
    queryset = WarehouseType.objects.all()
    serializer_class = WarehouseTypeSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WarehouseTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WarehouseType.objects.all()
    serializer_class = WarehouseTypeSerializer
    permission_classes = (permissions.IsAuthenticated,)


class WarehouseList(generics.ListCreateAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    permission_classes = (permissions.IsAuthenticated,)


class WarehouseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)


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
