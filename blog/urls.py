from django.urls import path

from django.contrib import admin
from . import views


urlpatterns = [
   path('', views.blog, name='blog'),
   path('<slug:slug>/', views.post_detail, name='post_detail'),
]
