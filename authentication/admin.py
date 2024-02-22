from django.contrib import admin
from authentication.models import User

# # Register your models here.
# admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'auth_provider', 'is_active')