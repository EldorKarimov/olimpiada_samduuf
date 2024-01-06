from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Direction, CustomUser

class DirectionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', )

admin.site.register(Direction, DirectionAdmin)

class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'full_name', 'phone', 'direction')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('full_name', 'phone', 'direction')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'full_name', 'phone', 'direction', 'password1', 'password2'),
        }),
    )
    search_fields = ('username', 'full_name', 'phone')
    ordering = ('-date_joined',)

admin.site.register(CustomUser, CustomUserAdmin)