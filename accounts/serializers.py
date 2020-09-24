from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode
from django.core.mail import EmailMessage

from rest_framework import serializers

from .models import User, ActivationToken
from . tokens import account_activation_token


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
        user.is_active = False
        user.save()
        token = account_activation_token.make_token(user)
        ActivationToken.objects.create(user=user,token=token)
        mail_subject = 'فعال سازی اکانت'
        message = f'your token is {token}'
        to_email = email
        email = EmailMessage(
            subject= mail_subject, body= message, to= [to_email]
        )
        email.send()
        return validated_data
