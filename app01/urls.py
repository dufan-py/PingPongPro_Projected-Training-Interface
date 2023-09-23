from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^get_coordinates/$', views.get_coordinates, name='get_coordinates'),
]

#【URL->函数】