from django.contrib import admin
from django.urls import path, include
from accounts.views import signup
from .views import home

urlpatterns = [
    path('', home, name="home"),
    path('admin/', admin.site.urls),
    # https://docs.djangoproject.com/fr/4.1/topics/auth/default/ voir vues d'authentification
    # dans ce cas on concatène compte avec login, logout...etc
    path('compte/', include('django.contrib.auth.urls')),
    # path('accounts/profile/', profile),

    path('compte/nouveau/', signup, name="signup"),
]

# import django.contrib.auth.urls
# on peut modifier la page quand on est logué, dans settings LOGIN_REDIRECT_URL
# pareil avec logout LOGOUT_REDIRECT_URL

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