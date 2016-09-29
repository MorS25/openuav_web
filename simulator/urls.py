from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #Page URLs
    url(r'^$', views.index, name='info'),
    url(r'^$', views.index, name='run'),
    ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)