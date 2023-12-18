from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password


class Direction(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    full_name = models.CharField(max_length = 255)
    username = models.CharField(
        max_length=150,
        unique=True,
        help_text=(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        error_messages={
            "unique": ("A user with that username already exists."),
        },
    )
    phone = models.CharField(max_length = 13)
    direction = models.ForeignKey(Direction, on_delete = models.PROTECT, null = True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["full_name", "phone"]

    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_sha256'):
            self.password = make_password(self.password)

        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.full_name