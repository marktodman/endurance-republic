from django.contrib import admin
from .models import Activity, Event


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):

    list_display = ('type', 'published_status')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    list_display = ('name', 'date', 'published_status')
