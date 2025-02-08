from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models
from django.core import validators


class UserManager(BaseUserManager):
    def create_user(self, email, username, password):
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
        user.save()

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
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class Follow(models.Model):
    user = models.ForeignKey(to='User', related_name='following', on_delete=models.CASCADE)
    followed_user = models.ForeignKey(to='User', related_name='followed_by', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'followed_user')

    def __str__(self):
        return f"{self.user.username} follows {self.followed_user.username}"


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255)
    email = models.EmailField(validators=[validators.validate_email], unique=True, blank=False)
    registration_date = models.DateTimeField(auto_now_add=True)
    followers = models.ManyToManyField(
        to='self',
        through=Follow,
        symmetrical=False,
        blank=True
    )

    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    objects = UserManager()

    def __str__(self):
        return f"{self.username} ({self.email})"
