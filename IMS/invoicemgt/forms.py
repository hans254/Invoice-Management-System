from django import forms
from .models import *
from .forms import *

required = 'This field is Required'
class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            'name', 'phone_number', 'invoice_date', 'invoice_number',
            'line_one','line_one_quantity', 'line_one_unit_price', 'line_one_total_price',
            'line_two','line_two_quantity', 'line_two_unit_price', 'line_two_total_price',
            
            'total','paid', 'invoice_type'
        ]
    def clean_invoice_number(self):
        invoice_number = self.cleaned_data.get('invoice_number')
        if not invoice_number:
            raise forms.ValidationError(required)
            return invoice_number

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError(required)
        return name

    def clean_line_one(self):
        line_one = self.cleaned_data.get('line_one')
        if not line_one:
            raise forms.ValidationError(required)
            return line_one

class InvoiceSearchForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            'name', 'invoice_number',
        ]

class InvoiceUpdateForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            'name', 'phone_number', 'invoice_date', 'invoice_number',
            'line_one','line_one_quantity', 'line_one_unit_price', 'line_one_total_price',
            'line_two','line_two_quantity', 'line_two_unit_price', 'line_two_total_price',
            
            'total','paid', 'invoice_type'
        ]
    def clean_invoice_number(self):
        invoice_number = self.cleaned_data.get('invoice_number')
        if not invoice_number:
            raise forms.ValidationError(required)
            return invoice_number

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError(required)
        return name

    def clean_line_one(self):
        line_one = self.cleaned_data.get('line_one')
        if not line_one:
            raise forms.ValidationError(required)
            return line_one