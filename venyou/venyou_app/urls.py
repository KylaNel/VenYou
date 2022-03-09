from django.urls import path
from venyou_app import views

app_name = 'venyou_app'

urlpatterns = [
    path('', views.index, name='index'),
]