from django.contrib import admin
from .models import UserProfile, ModelAdmin
# Register your models here.
admin.site.register(UserProfile, ModelAdmin)
