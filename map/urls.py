from django.urls import path
from . import views

urlpatterns = [
    path('', views.map_view, name='map'),
    path('statue/', views.statue_view, name='statue'),
    path('empire/', views.empire_view, name='empire'),
    path('times/', views.times_view, name='times'),
    path('park/', views.park_view, name='park'),

]
