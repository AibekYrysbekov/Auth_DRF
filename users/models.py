from django.db import models
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError({'Error: email обязательное поле'})
        if not username:
            raise ValueError({'Error: username обязательное поле'})
        if not password:
            raise ValueError({'Error: password обязательное поле'})

        user = self.model(username=username, email=email, **extra_fields)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(username, password, **extra_fields)


class UserModel(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField('email address', unique=True)
    code = models.PositiveIntegerField(null=True, blank=True)
    is_verify = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return f'email {self.email} username {self.username}'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

