from django.contrib import admin
from .models import Book

admin.site.register(Book)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year') 
    search_fields = ('title', 'author') 
    list_filter = ('publication_year',)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'date_of_birth', 'profile_photo', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)
