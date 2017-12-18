from django.conf.urls import url

from managers.api import views

urlpatterns = [
    url(r'^$', views.ManagerListAPIView.as_view(), name='list'),
    url(r'^create/$', views.ManagerCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/detail/$', views.ManagerRetrieveAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', views.ManagerUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', views.ManagerDeleteAPIView.as_view(), name='delete'),
    url(r'^staff/$', views.StaffManagerListAPIView.as_view(), name='staff_list'),
    url(r'^staff/create/$', views.StaffManagerCreateAPIView.as_view(), name='staff_create'),
    url(r'^staff/(?P<pk>\d+)/detail/$', views.StaffManagerRetrieveAPIView.as_view(), name='staff_detail'),
    url(r'^staff/(?P<pk>\d+)/update/$', views.StaffManagerUpdateAPIView.as_view(), name='staff_update'),
    url(r'^staff/(?P<pk>\d+)/delete/$', views.StaffManagerDeleteAPIView.as_view(), name='staff_delete'),
]
