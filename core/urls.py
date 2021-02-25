from django.urls import path
from . import views


app_name='core'
urlpatterns = [
    path('', views.index, name='index'),
    path('api-document/', views.api_doc, name='api_doc')
]