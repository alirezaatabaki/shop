from rest_framework import serializers

from .models import User

class UserCreateSerializer(serializers.ModelSerializer):
    # Serializer for create user from API
    class Meta:
        model = User
        fields = ['email', 'password']