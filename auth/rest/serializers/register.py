from rest_framework import serializers

from core.models import User, UserProfile
from core.choices import RoleChoices 

from core.utils.email import send_welcome_email



class UserRegisterSerializer(serializers.ModelSerializer):
    """Serializer for user registration"""

    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "confirm_password",
            "role",
        ]

    def validate_password(self, value):
        """Validate the password"""
        # Check length of password
        if len(value) < 6:
            raise serializers.ValidationError(
                "Password must be at least 6 characters long"
            )
        # Check password match with confirm password
        if value != self.initial_data.get("confirm_password"):
            raise serializers.ValidationError(
                "Password and confirm password don't match"
            )
        return value

    def create(self, validated_data):
        validated_data.pop('confirm_password', None)
        user = super().create(validated_data)
        
        # Send welcome email
        try:
            send_welcome_email(user)
        except Exception as e:
            print(f"Failed to send welcome email: {e}")
        
        return user
