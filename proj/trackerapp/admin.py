# Register your models here.
from django.contrib import admin
from .models import AppUser
from .models import UserLocation
from django.contrib.auth.admin import UserAdmin

APP_USER_FIELDS = (
    ('Additional Info', {'fields': ('gender','dob',)}),
)

class AppUserAdmin(UserAdmin):
    model = AppUser
    fieldsets = UserAdmin.fieldsets + APP_USER_FIELDS

admin.site.register(AppUser, AppUserAdmin)
admin.site.register(UserLocation)