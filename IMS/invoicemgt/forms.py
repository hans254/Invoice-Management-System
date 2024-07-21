from django import forms
from .models import *
from .forms import *

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            'name', 'phone_number', 'invoice_date',

            
            'total','paid', 'invoice_type'
        ]