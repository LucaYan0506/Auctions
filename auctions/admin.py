from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(categories)
admin.site.register(Auction)
admin.site.register(Bids)
admin.site.register(Comments)