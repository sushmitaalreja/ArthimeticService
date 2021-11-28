from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.api_root, name='api_root'),
    url(r'^add/?$', views.add, name='add'),
    url(r'^subtract/?$', views.subtract, name='subtract'),
    url(r'^multiply/?$', views.multiply, name='multiply'),
    url(r'^divide/?$', views.divide, name='divide')
]