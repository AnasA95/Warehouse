from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^warehouseType/$', views.warehouse_type_list),
    url(r'^warehouseType/(?P<pk>[0-9]+)/$', views.warehouse_type_detail),
    url(r'^warehouse/$', views.warehouse_list),
    url(r'^warehouse/(?P<pk>[0-9]+)/$', views.warehouse_detail),
    url(r'^user/$', views.user_list),
    url(r'^user/(?P<pk>[0-9]+)/$', views.user_detail),
    url(r'^owner/$', views.owner_list),
    url(r'^owner/(?P<pk>[0-9]+)/$', views.owner_detail),
    url(r'^customer/$', views.customer_list),
    url(r'^customer/(?P<pk>[0-9]+)/$', views.customer_detail),
    url(r'^provider/$', views.provider_list),
    url(r'^provider/(?P<pk>[0-9]+)/$', views.provider_detail),
    url(r'^incomingOrder/$', views.incoming_order_list),
    url(r'^incomingOrder/(?P<pk>[0-9]+)/$', views.incoming_order_detail),
    url(r'^outgoingOrder/$', views.outgoing_order_list),
    url(r'^outgoingOrder/(?P<pk>[0-9]+)/$', views.outgoing_order_detail),
    url(r'^package/$', views.package_list),
    url(r'^package/(?P<pk>[0-9]+)/$', views.package_detail),
    url(r'^box/$', views.box_list),
    url(r'^box/(?P<pk>[0-9]+)/$', views.box_detail),
    url(r'^item/$', views.item_list),
    url(r'^item/(?P<pk>[0-9]+)/$', views.item_detail),
]
