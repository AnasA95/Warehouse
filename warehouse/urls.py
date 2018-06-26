from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'', include('whss.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^whss/', include('whss.urls')),
    url(r'^api/auth/login/$', obtain_jwt_token, name='api-login'),
    url(r'^api/whss/', include(('whss.api.urls', 'whss'), namespace='api-whss')),
]
