from django.contrib.auth.password_validation import validate_password
from rest_framework import  serializers
from rest_framework.permissions import IsAuthenticated
from django.db import models
from .models import Customer
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
# Register serializer
class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name','phone_number','password', 'password2')
        extra_kwargs = {
            'phone_Number': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = Customer.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number=validated_data['phone_number'],
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user