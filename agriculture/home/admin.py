from django.contrib import admin
from .models import User, Cold_storage, Retailer, Farmer
# Register your models here.

admin.site.register(User)
admin.site.register(Cold_storage)
admin.site.register(Retailer)
admin.site.register(Farmer)
