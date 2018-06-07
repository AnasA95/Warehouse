from .views import UserRudAPIView, UserAPIView
from django.conf.urls import url

urlpatterns = [
    url(r'^$', UserAPIView.as_view(), name='user-create'),
    url(r'^(?P<pk>\d+)/$', UserRudAPIView.as_view(), name='user-rud'),
]
