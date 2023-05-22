from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken


# Create your models here.


class User(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.email

    def save(self, **kwargs):
        self.username = self.email
        return super(User, self).save(**kwargs)

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

class ProductModel(models.Model):
    name = models.CharField(max_length=40, null=False)
    description = models.CharField(max_length=128, null=True)
    price = models.IntegerField(null=False)
    stock = models.IntegerField(null=False)
