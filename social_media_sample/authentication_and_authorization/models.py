from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models
from django.core import validators


class UserManager(BaseUserManager):
    def create_user(self, email, username, is_active=True, password=None):
        if not email:
            raise ValueError('Users must have an email address.')
        if not username:
            raise ValueError('Users must have an username.')

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            is_active=is_active
        )

        user.set_password(password)
        user.save(self._db)

        return user

    def create_superuser(self, email, username, password):
        if not email:
            raise ValueError('Users must have an email address.')
        if not username:
            raise ValueError('Users must have an username.')

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
        )
        user.set_password(password)
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.save(self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255)
    email = models.EmailField(validators=[validators.validate_email], unique=True, blank=False)
    registration_date = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    objects = UserManager()

    def __str__(self):
        return f"{self.username} ({self.email})"
