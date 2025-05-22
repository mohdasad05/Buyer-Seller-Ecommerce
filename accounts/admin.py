from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('id', 'email', 'username', 'is_buyer', 'is_seller', 'is_staff', 'is_superuser')
    list_filter = ('is_buyer', 'is_seller', 'is_staff', 'is_superuser')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_buyer', 'is_seller')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('is_buyer', 'is_seller')}),
    )
    search_fields = ('email', 'username')
    ordering = ('id',)

admin.site.register(CustomUser, CustomUserAdmin)
