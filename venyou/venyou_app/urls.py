from django.urls import path
from venyou_app import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'venyou_app'

urlpatterns = [
    path('', views.index, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)