from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('settings/', views.user_settings, name = 'settings'),
    path('remove_avatar/', views.remove_avatar, name = 'remove_avatar'),
    path('signin/', views.user_login, name = 'login'),
    path('signup/', views.user_register, name = 'register'),
    path('signout/', views.user_logout, name = 'logout'),
    path('refresh_token/', views.user_refresh_token, name = 'refresh_token'),
]