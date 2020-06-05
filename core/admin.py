from django.contrib import admin
from core.models import Event #remeber to import
# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ('title','date_event', 'date_creation')
    list_filter = ('user','date_event',) #creating a filter

admin.site.register(Event,EventAdmin) #call