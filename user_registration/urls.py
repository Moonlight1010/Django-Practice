from .views import *
from django.urls import path
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordResetDoneView

urlpatterns = [
    path('', register, name='register-page'),
    path('login/', login_view, name='login-page'),
    path('logout/', logout_view, name='logout-page'),
    path('password_reset/', PasswordResetView.as_view(template_name='user_registration/password_reset.html'), name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='user_registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(template_name='user_registration/password_reset_complete.html'), name='password_reset_complete'),
    path('password_reset_done/', PasswordResetDoneView.as_view(template_name='user_registration/password_reset_done.html'), name='password_reset_done'),



]
