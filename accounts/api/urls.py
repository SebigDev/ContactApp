from django.conf.urls import url

from accounts.api import views

urlpatterns = [
    url(r'^register/$', views.ContactAppUserCreateAPIView.as_view(), name='register')
]