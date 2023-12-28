from django.urls import path
from .views import register, logout_for_cubgame, login_for_cubgame


urlpatterns = [
    path("register/", register, name="register"),
    path("logout/", logout_for_cubgame, name="logout"),
    path("login/", login_for_cubgame, name="login")
]
