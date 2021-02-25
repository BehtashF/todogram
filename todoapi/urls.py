from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


app_name = 'todoapi'
urlpatterns = [
    path('api-token-auth/', obtain_auth_token)
]