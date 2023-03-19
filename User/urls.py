from django.urls import path
from .views import CustomLoginView, CustomLogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLoginView.as_view(), name='logout'),
]
