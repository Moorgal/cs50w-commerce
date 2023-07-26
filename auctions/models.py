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
    listing_price = models.FloatField(default=0, null=True, blank=True)
    image_link = models.CharField(max_length=2000)
    is_available = models.BooleanField(default=True)
    bid_amount = models.IntegerField(default=0, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user")
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title
    

#class Bids(models.Model):
   # id
   # listing_id
   # price
   # date
   # user


#class watchlist
#id
#user
#listing_id

#class comments
##id
#listing_id
#User
#body
#date