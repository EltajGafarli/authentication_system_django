from django.urls import path
from . import views

app_name = "auth"

urlpatterns = [
    path('register/',views.register, name = "register"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.log_out, name="logout"),
]
