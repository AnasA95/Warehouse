from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^warehouseType/$', views.WarehouseTypeList.as_view(), name='warehousetype-list'),
    url(r'^warehouseType/(?P<pk>[0-9]+)/$', views.WarehouseTypeDetail.as_view()),
    url(r'^warehouse/$', views.WarehouseList.as_view()),
    url(r'^warehouse/(?P<pk>[0-9]+)/$', views.WarehouseDetail.as_view()),
    url(r'^user/$', views.UserList.as_view(), name='user-list'),
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^owner/$', views.OwnerList.as_view()),
    url(r'^owner/(?P<pk>[0-9]+)/$', views.OwnerDetail.as_view()),
    url(r'^customer/$', views.CustomerList.as_view()),
    url(r'^customer/(?P<pk>[0-9]+)/$', views.CustomerDetail.as_view()),
    url(r'^provider/$', views.ProviderList.as_view()),
    url(r'^provider/(?P<pk>[0-9]+)/$', views.ProviderDetail.as_view()),
    url(r'^incomingOrder/$', views.IncomingOrderList.as_view()),
    url(r'^incomingOrder/(?P<pk>[0-9]+)/$', views.IncomingOrderDetail.as_view()),
    url(r'^outgoingOrder/$', views.OutgoingOrderList.as_view()),
    url(r'^outgoingOrder/(?P<pk>[0-9]+)/$', views.OutgoingOrderDetail.as_view()),
    url(r'^package/$', views.PackageList.as_view()),
    url(r'^package/(?P<pk>[0-9]+)/$', views.PackageDetail.as_view()),
    url(r'^box/$', views.BoxList.as_view()),
    url(r'^box/(?P<pk>[0-9]+)/$', views.BoxDetail.as_view()),
    url(r'^item/$', views.ItemList.as_view()),
    url(r'^item/(?P<pk>[0-9]+)/$', views.ItemDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
