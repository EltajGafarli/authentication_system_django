from django.urls import path
from . import views

app_name='base'

urlpatterns = [
    path('', views.main_page, name="main"),
    path('users/', views.users_page, name="users")
]
