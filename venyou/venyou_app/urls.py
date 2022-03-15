from django.urls import path
from venyou_app import views
from django.urls import include

from django.conf import settings
from django.conf.urls.static import static

app_name = 'venyou_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('rate/', views.rate, name='rate'),
    path('map/', views.map, name='map'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('myaccount/', views.myaccount, name='myaccount'),
    path('add_venue/', views.add_venue, name='add_venue'),
    path('create_account/', views.create_account, name='create_account'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)