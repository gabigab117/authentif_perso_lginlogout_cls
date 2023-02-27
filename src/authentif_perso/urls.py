"""authentif_perso URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts.views import signup
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    # https://docs.djangoproject.com/fr/4.1/topics/auth/default/ voir vues d'authentification
    # dans ce cas on concatène compte avec login, logout...etc
    path('compte/', include('django.contrib.auth.urls')),
    path('', home, name="home"),
    path('compte/nouveau/', signup, name="signup"),
]

# il faut penser à creer un dossier registration avec login.html dedans.

# urlpatterns = [
#     path("login/", views.LoginView.as_view(), name="login"),
#     path("logout/", views.LogoutView.as_view(), name="logout"),
#     path(
#         "password_change/", views.PasswordChangeView.as_view(), name="password_change"
#     ),
#     path(
#         "password_change/done/",
#         views.PasswordChangeDoneView.as_view(),
#         name="password_change_done",
#     ),
#     path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
#     path(
#         "password_reset/done/",
#         views.PasswordResetDoneView.as_view(),
#         name="password_reset_done",
#     ),
#     path(
#         "reset/<uidb64>/<token>/",
#         views.PasswordResetConfirmView.as_view(),
#         name="password_reset_confirm",
#     ),
#     path(
#         "reset/done/",
#         views.PasswordResetCompleteView.as_view(),
#         name="password_reset_complete",
#     ),
# ]