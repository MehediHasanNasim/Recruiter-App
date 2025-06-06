from rest_framework import serializers
from django_rest_passwordreset.serializers import PasswordTokenSerializer

class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()

class CustomPasswordTokenSerializer(PasswordTokenSerializer):
    new_password = serializers.CharField(min_length=6)
    confirm_password = serializers.CharField(min_length=6)

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords don't match")
        return data