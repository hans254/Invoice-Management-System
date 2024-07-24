from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import *

# Create your views here.
def home(request):
    title = 'Welcome: This is the Home page'
    context = {
        'title': title,
    }
    return render(request, 'home.html', context)

def add_invoice(request):
    form = InvoiceForm(request.POST or None)
    total_invoice = Invoice.objects.count()
    queryset = Invoice.objects.order_by('-invoice_date')[:6]
    if form.is_valid(): 
        form.save()
        messages.success(request, 'Saved Successfully')
        return redirect('/list_invoice')
    context = {
        'form': form,
        'title': 'New Invoice',
        'total_invoice': total_invoice,
        'queryset': queryset,
    }
    return render(request, 'entry.html', context)

def list_invoice(request):
    title = 'List of Invoices'
    queryset = Invoice.objects.all()
    form = InvoiceSearchForm(request.POST or None)
    if request.method == 'POST':
        queryset = Invoice.objects.filter(invoice_number__icontains=form['invoice_number'].value(),
        name__icontains=form['name'].value(),)
    context = {
        'title': title,
        'queryset': queryset,
        'form': form,
    }
    return render(request, 'list_invoice.html', context)

def update_invoice(request, pk):
    queryset = Invoice.objects.get(id=pk)
    form = InvoiceUpdateForm(instance = queryset)
    if request.method == 'POST':
        form = InvoiceUpdateForm(request.POST, instance = queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully')
            return redirect('/list_invoice')
    context = {
        'form': form,
    }
    return render(request, 'entry.html', context)

def delete_invoice(request, pk):
    queryset = Invoice.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect('/list_invoice')
    return render(request, 'delete_invoice.html')