from django.contrib import admin
from .models import Destination

# Register your models here
class Destinationadmin(admin.ModelAdmin):
    list_display=('name','image','description')

def description(self, obj):
        return obj.description()

admin.site.register(Destination)
