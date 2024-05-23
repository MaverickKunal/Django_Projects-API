from django.contrib import admin
from django.urls import path, include
from homeapp import views

urlpatterns = [
    path('',views.index, name="homeapp"),
    path('login',views.loginuser, name="login"),
    path('logout',views.logoutuser, name="logout"),
    path('active',views.activeuserslist, name="active_users")
]
