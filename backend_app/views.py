import datetime

from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import ProductModel
from .serializers import ProductSerializer

# Create your views here.


class Signin(generics.CreateAPIView):
    permission_classes = (AllowAny,)

    def post(self, request, **kwargs):
        user = auth.authenticate(username=request.data['email'], password=request.data['password'])
        if not user:
            return Response(status=status.HTTP_404_NOT_FOUND, data="Invalid Credentials, try again")
        jwt_token = RefreshToken.for_user(user)
        return Response(status=status.HTTP_200_OK, data={
            'id': user.pk,
            'email': user.email,
            'username': user.username,
            'refresh': str(jwt_token),
            'access': str(jwt_token.access_token),
        })


class ProductView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        pname = request.query_params.get('product_name')
        if not pname:
            return Response(status=status.HTTP_404_NOT_FOUND, data="No data Found")
        qs = ProductModel.objects.filter(name__icontains=pname)
        return Response(status=status.HTTP_200_OK, data=ProductSerializer(qs, many=True).data)
