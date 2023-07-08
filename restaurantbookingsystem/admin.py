from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

class CustomUserAdmin(BaseUserAdmin):
    # Your customizations go here

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
