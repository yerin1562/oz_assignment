from django.contrib import admin
from .models import Address

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'street', 'city', 'state', 'postal_code', 'country']
    list_filter = ['city', 'state', 'country']
    search_fields = ['user__username', 'street', 'postal_code', 'city', 'state']