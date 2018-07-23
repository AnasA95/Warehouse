from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'', include('whss.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/auth/', include('rest_framework.urls')),
    url(r'^api/whss/', include(('whss.urls', 'whss'), namespace='api-whss')),
]
