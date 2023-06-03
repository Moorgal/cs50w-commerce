from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

class User(AbstractUser):
    pass

class Categories(models.Model):
    title = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


class Listing(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    link = models.CharField(max_length=2000)
    is_available = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user")
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, blank=True, null=True, related_name="category")
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)