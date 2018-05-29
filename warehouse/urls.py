from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url(r'', include('whss.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^whss/', include('whss.urls')),
]
