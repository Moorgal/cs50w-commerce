from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

class User(AbstractUser):
    pass

class Categories(models.Model):
    title = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title


class Listing(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.ManyToManyField('Categories', blank=True)
    watchlist = models.ManyToManyField('User', blank=True, related_name="watchlist")
    listing_price = models.IntegerField(default=0, null=True, blank=True)
    image_link = models.CharField(max_length=2000)
    is_available = models.BooleanField(default=True)
    bid_amount = models.IntegerField(default=0, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user")
    date = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title
    

class Bids(models.Model):
   listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE)
   amount = models.IntegerField(default=0)
   user_id = models.ForeignKey(User, on_delete=models.CASCADE)
   date = models.DateTimeField(auto_now_add=True)
   id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)



class Comments(models.Model):
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='commentListing')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commentUser')
    body = models.TextField(max_length=500, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)



