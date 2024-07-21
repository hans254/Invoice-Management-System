from django.contrib import admin
#from django.apps import apps
from .models import Invoice
from .forms import InvoiceAdmin

# Register your models here.

admin.site.register(Invoice)
#Customizing Admin Page
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('name','invoice_number', 'invoice_date', 'phone_number')
    form = InvoiceForm
    list_filter = ['name']
    search_fields = ['name', 'invoice_number']