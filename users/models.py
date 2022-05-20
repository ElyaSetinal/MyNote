from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as DjangoUserManager

# Create your models here.
class UserManager(DjangoUserManager): #DB로 Query를 날릴때 사용하는
    def _create_user(self, identifier, email, password, **extra_fields): #제일 앞 언더바는 대외비라 생각
        user = self.model(identifier=identifier, email=email, **extra_fields)
        user.set_password(password) # https://docs.djangoproject.com/en/4.0/topics/auth/customizing/ set_password
        user.save(using=self._db)
        return user

    def create_user(self, identifier, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(identifier, email, password, **extra_fields)

    def create_superuser(self, identifier, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(identifier, email, password, **extra_fields)

class CustomUser(AbstractUser):
    identifier = models.CharField(verbose_name='ID', max_length=20, unique=True)
    phone = models.CharField(verbose_name='전화번호', max_length=11,)
    nickname = models.CharField(verbose_name='별명', max_length=20,)

    USERNAME_FIELD = 'identifier' # 아이디를 로그인에 사용할 것
    REQUIRED_FIELDS = ['phone', 'nickname','email']
    
    objects = UserManager()