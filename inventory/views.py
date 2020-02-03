from django.shortcuts import render, redirect
from .models import inventoryreq
from .form import additemform


def inventorytableview(request):
    obj = inventoryreq.objects.all()
    inventorytablecolumn = ["ID", 'Item Name', 'Quantity',
                            'Original Price (Per Unit)', 'Selling Price (Per Unit)', 'Date Bought', 'Expiry Date']
    context = {
        'obj': obj,
        'tcol': inventorytablecolumn
    }
    return render(request, 'inventorytable.html', context)


def inventoryadditemview(request):
    form = additemform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(".")
    context = {
        'form': form
    }
    return render(request, 'inventoryadditem.html', context)

# Create your views here.
