from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ManagerListView.as_view(), name='list'),
    url(r'^create/$', views.ManagerCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/detail/$', views.ManagerDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', views.ManagerUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', views.ManagerDeleteView.as_view(), name='delete'),
    url(r'^staff/$', views.StaffManagerListView.as_view(), name='staff_list'),
    url(r'^staff/create/$', views.StaffManagerCreateView.as_view(), name='staff_create'),
    url(r'^staff/(?P<pk>\d+)/detail/$', views.StaffManagerDetailView.as_view(), name='staff_detail'),
    url(r'^staff/(?P<pk>\d+)/update/$', views.StaffManagerUpdateView.as_view(), name='staff_update'),
    url(r'^staff/(?P<pk>\d+)/delete/$', views.StaffManagerDeleteView.as_view(), name='staff_delete'),
    ]