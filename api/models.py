from xml.dom import ValidationErr
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class KarangueManager(BaseUserManager):
    def create_user(self, first_name, last_name, phone_number, password=None):
        if not first_name:
            raise ValidationErr("Custom must have a firtsname")
        if not last_name:
            raise ValidationErr("Custom must have a lastname")
        if not phone_number:
            raise ValidationErr("Please give a active phone number")

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number
        )

        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, first_name, last_name, phone_number, password):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            password=password
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)

class Customer(AbstractBaseUser):
    # email = models.EmailField(max_length=150) 
    first_name = models.CharField(max_length = 150)
    last_name = models.CharField(max_length = 150)
    phone_number = models.CharField(max_length = 150, unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    USERNAME_FIELD = 'phone_number'

    REQUIRED_FIELDS = ['last_name','first_name']

    objects = KarangueManager()


    def __str__(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True