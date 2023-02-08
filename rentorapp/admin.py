from django.contrib import admin

from .models import LandLord,Location,Propertycategory,Property

# Register your models here.

admin.site.register(LandLord),
admin.site.register(Location),
admin.site.register(Propertycategory),
admin.site.register(Property),
