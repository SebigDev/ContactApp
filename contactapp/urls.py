
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/managers/', include('managers.api.urls')),
    url(r'^managers/', include('managers.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^api/accounts/', include('accounts.api.urls')),
]
