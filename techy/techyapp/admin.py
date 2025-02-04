from django.contrib import admin
from django.contrib.auth.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined')
    search_fields = ('username', 'email')  # Allows searching users
    list_filter = ('is_staff', 'is_active')  # Adds filter options

# Unregister the default User model and register the customized version
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

