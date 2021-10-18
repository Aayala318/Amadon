from django.urls import path
from . import views

urlpatterns = [
    path('', views.amadon),
    path('purchase', views.purchase),
    path('checkout', views.checkout),
]