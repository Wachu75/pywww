from django.contrib import admin

# Register your models here.
from main.models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass