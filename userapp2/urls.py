from django.urls import path

from userapp2 import views

urlpatterns = [
    path('', views.intro, name='intro'),
    path('', views.call, name='call'),
]