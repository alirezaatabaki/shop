from rest_framework import serializers

from .models import User


class UserCreateSerializer(serializers.ModelSerializer):
    # Serializer for create user from API
    confirmation_email = serializers.EmailField(label='تایید ایمیل')
    class Meta:
        model = User
        fields = ['email', 'confirmation_email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        email = data['email']
        email2 = data['confirmation_email']
        if email != email2:
            raise serializers.ValidationError('Emails must match')
        return data

    def create(self, validated_data):
        print(validated_data)
        email = validated_data['email']
        password = validated_data['password']
        user = User(email=email)
        user.set_password(password)
        user.save()
        return validated_data
