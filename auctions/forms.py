from django.forms import ModelForm
from .models import Listing, Comments

class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'category', 'listing_price', 'image_link']

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['user_id','listing_id','body']








