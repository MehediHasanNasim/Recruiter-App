from django.urls import path
from auth.rest.views.password_reset import (
    ForgotPasswordView,
    ResetPasswordView,
    ResetPasswordValidateToken
)

urlpatterns = [
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('reset-password/validate-token/', ResetPasswordValidateToken.as_view(), name='reset-password-validate-token'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),
]