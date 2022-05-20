from django.contrib import admin

from .models import CustomUser

@admin.register(CustomUser)
class CustomUserModelAdmin(admin.ModelAdmin):
    list_display = ['identifier', 'nickname','date_joined','last_login']
    readonly_fields= ['password',]
    pass