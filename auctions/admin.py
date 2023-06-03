from django.contrib import admin

# Register your models here.
from .models import User, Categories, Listing

admin.site.register(User)
admin.site.register(Categories)
admin.site.register(Listing)