from rest_framework import generics, status
from rest_framework.response import Response
from core.models import User
from django_rest_passwordreset.models import ResetPasswordToken
from django_rest_passwordreset.views import ResetPasswordValidateToken, ResetPasswordConfirm
from auth.rest.serializers.password_reset import (
    EmailSerializer,
    CustomPasswordTokenSerializer
)
from core.utils.email import send_password_reset_email


class ForgotPasswordView(generics.GenericAPIView):
    serializer_class = EmailSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        email = serializer.validated_data['email']
        
        try:
            user = User.objects.get(email=email)
            token = ResetPasswordToken.objects.create(
                user=user,
                user_agent=request.META.get('HTTP_USER_AGENT', ''),
                ip_address=request.META.get('REMOTE_ADDR', ''),
            )
            send_password_reset_email(user, token)
            
            return Response(
                {"detail": "Password reset email sent if email exists"},
                status=status.HTTP_200_OK
            )
        except User.DoesNotExist:
            # Don't reveal whether user exists
            return Response(
                {"detail": "Password reset email sent if email exists"},
                status=status.HTTP_200_OK
            )


class ResetPasswordView(ResetPasswordConfirm):
    serializer_class = CustomPasswordTokenSerializer