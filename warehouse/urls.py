from django.contrib import admin
from django.conf.urls import url, include
from whss import views

urlpatterns = [
    url(r'', include('whss.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^whss/', include('whss.urls')),
    url(r'^User/', views.UserList.as_view()),
]
