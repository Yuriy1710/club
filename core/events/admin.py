from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(MyClubUser)


class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')
    ordering = ('name',)
    search_fields = ('name', 'address')
    
admin.site.register(Venue, VenueAdmin)


class EventAdmin(admin.ModelAdmin):
    fields = (('name', 'venue'), 'event_date', 'description', 'manager', 'attendee')
    list_display = ('name', 'event_date', 'venue')
    list_filter = ('event_date', 'venue')
    ordering = ('event_date',)
    
admin.site.register(Event, EventAdmin)