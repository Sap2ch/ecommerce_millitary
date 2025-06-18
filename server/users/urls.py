from django.urls import path
from django.contrib.auth import views as auth_views
from .views import logout_user, ProfileView, UsersView, FFLView

urlpatterns = [
    path('profile/<slug:slug>/', ProfileView.as_view(), name='profile'),
    path('logout/', logout_user, name='logout'),
    path('users/', UsersView.as_view(), name='users'),
    path('ffl-verifed/', FFLView.as_view(), name='ffl')
]