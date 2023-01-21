from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'reason')
    search_fields = ('name', 'email', 'created_on')

    def approve_contact(self, request, queryset):
        queryset.update(approved=True)
