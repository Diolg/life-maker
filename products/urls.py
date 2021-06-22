from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_sessions, name='products'),
    path('<product_id>', views.session_detail, name='session_detail'),
]