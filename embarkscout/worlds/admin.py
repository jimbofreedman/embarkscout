from django.contrib import admin

# Register your models here.
from .models import WorldGenParams, World

admin.site.register(WorldGenParams)
admin.site.register(World)