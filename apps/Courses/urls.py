from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^show/(?P<id>\d+)$', views.show),
    url(r'^addcourse$', views.addcourse),
    url(r'^show/delete/(?P<id>\d+)$', views.delete)
]