from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import ProductModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name',
                  'last_name', 'username', 'is_active')
        extra_kwargs = {
            'password': {'write_only': True},
            'username': {'write_only': True, 'validators': []}
        }

    def validate_password(self, value):
        if value:
            return make_password(value)
        return value


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'
