from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("login", views.loginview, name="login"),
    path("registered", views.registered, name="registered"),
    path("loginverify", views.loginverify, name="loginverify"),
]
