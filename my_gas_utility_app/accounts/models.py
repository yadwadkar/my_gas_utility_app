from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

# Custom User model that extends Django's AbstractUser
class User(AbstractUser):
    # We can add additional fields specific to the user if needed
    is_customer = models.BooleanField(default=False)
    is_support_rep = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Change related_name here
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',  # Change related_name here
        blank=True,
        help_text='Specific permissions for this user.'
    )

# Customer profile linked to the User model
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username

# Support Representative profile linked to the User model
class SupportRepresentative(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
