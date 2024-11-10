from django.contrib import admin
from .models import Driver

# Register your models here.
#admin.site.register(Driver)

@admin.register(Driver)
class driverAdmin(admin.ModelAdmin):
    # List Disply on edit drivers page
    list_display = ("truckNumber", "lastName", "firstName")
