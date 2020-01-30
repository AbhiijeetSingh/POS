from django.shortcuts import render, redirect
from .form import paymentform,recordform
from .models import paymentdetails, recordmodel
from inventory.models import inventoryreq

global items_added,record_instance,transdetail
items_added,transdetail=[],[]

def transchoice(request):
    return render(request, 'transchoice.html', {})


def makepayment(request):
    form=paymentform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("makepayment/transadditem")
    context={
        'form':form
    }
    return render(request, 'payment.html',context)


def addtransitem(request):
    amount=0
    inventorytablecolumn=["ID",'Item Name','Selling Price (Per Unit)', 'Expiry Date',"Quantity"]
    
    if request.POST.get('item_id')!=None:
        item_id=int(request.POST.get("item_id"))
        item_instance_quantity=int(request.POST.get('item_quantity'))
        item_instance=inventoryreq.objects.get(id=item_id)
        items_added.append([item_instance.id,
                            item_instance.item_name,
                            item_instance.retail_price,
                            item_instance.expire_date,
                            item_instance_quantity
                            ]
                                    )
        print(items_added)

        
    for value in range(len(items_added)):
        amount=amount+(items_added[value][2]*items_added[value][4])

    transdetail=paymentdetails.objects.last()
    context={
        'items_added': items_added ,
        'tcol': inventorytablecolumn,
        'transdetail':transdetail,
        'amount':amount
    }
    return render(request, 'transadditem.html', context)

def record(request):
    context={
        'record_instance':transdetail
    }
    print(context)
    return render(request, 'record.html',context)
    


# Create your views here.
