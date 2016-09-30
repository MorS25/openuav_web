from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #Page URLs
    url(r'^$', views.index, name='info'),
    url(r'^land$', views.land, name='land'),
    url(r'^takeoff$', views.takeoff, name='takeoff'),
    url(r'^offboard$', views.offboard, name='offboard'),
    url(r'^arm$', views.arm, name='arm'),
    url(r'^disarm$', views.disarm, name='arm'),
    url(r'^mission$', views.mission, name='arm'),
    url(r'^rtl$', views.rtl, name='arm'),

              ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)