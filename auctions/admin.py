from django.contrib import admin

# Register your models here.
from .models import User, Categories, Listing, Bids, Watchlist, Comments

admin.site.register(User)
admin.site.register(Categories)
admin.site.register(Listing)
admin.site.register(Bids)
admin.site.register(Watchlist)
admin.site.register(Comments)