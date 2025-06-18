from django.urls import path
from .views import RegisterView, LoginUser

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
]