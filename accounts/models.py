from django.db import models
from django.contrib.auth.models import (
    AdstractBaseUser, BaseUserManager, AbstractUser, models
)

class User(AdstractBaseUser):
    email = models.EmailField(max_length=255, unique = True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=True) #로그인 할 수 있나?(휴먼계정이 아닌가?)
    staff = models.BooleanField(default=False) #superuser가 아닌 staff(김현준x 박하영o)
    admin = models.BooleanField(default=False) #superuser(김현준, 주영민)

USERNAME_FIELD = 'email'
REQUIRED_FIELDS = []

def __str__(self):
    return self.email

@property
def is_staff(self):
    return self.staff

@property
def is_superuser(self):
    return self.admin


