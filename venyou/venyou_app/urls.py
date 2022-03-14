from django.urls import path
from venyou_app import views
from django.urls import include

from django.conf import settings
from django.conf.urls.static import static

app_name = 'venyou_app'

urlpatterns = [
    path('rate/', views.rate, name='rate'),
    path('', views.home, name='home'),
    path('map/', views.map, name='map'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)