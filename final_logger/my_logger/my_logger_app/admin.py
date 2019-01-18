from django.contrib import admin
from .models import Items, Property ,Variant
from django.contrib.auth.models import User


admin.site.register(Items)
admin.site.register(Variant)
admin.site.register(Property)
