from django.contrib import admin
from .models import Table, Booking
from django_summernote.admin import SummernoteModelAdmin

class TableAdmin(admin.ModelAdmin):
    # Customize the admin behavior for the Table model
    list_display = ('code', 'capacity', 'is_available')
    search_fields = ('code',)
    list_filter = ('is_available',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    # Customize the admin behavior for the Booking model
    list_display = ('date', 'start_time', 'end_time', 'table', 'customer_name', 'customer_email')
    search_fields = ('customer_name', 'customer_email')
    list_filter = ('date', 'table')

admin.site.register(Table, TableAdmin)


