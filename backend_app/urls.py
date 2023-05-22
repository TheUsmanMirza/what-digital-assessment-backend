from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import Signin, ProductView

urlpatterns = [
    path('signin/', Signin.as_view(), name='signin'),
    path('product/', ProductView.as_view(), name='product'),
]