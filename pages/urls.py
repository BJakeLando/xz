from django.urls import path
from .views import (
    HomeView,
    AboutView,
    DonateView,

)

urlpatterns = [
    path('home/', HomeView.as_view(), name = 'home'),
    path('about/', AboutView.as_view(), name = 'about'),
    path('donate/', DonateView.as_view(), name = 'donate'),
]