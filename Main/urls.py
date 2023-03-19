from django.contrib import admin
from django.urls import path, include
from .views import SobreView

from Main.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('sobre/', SobreView.as_view(), name='sobre'),
]
