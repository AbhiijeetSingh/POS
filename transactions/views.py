from django.shortcuts import render, redirect
from .form import paymentform
from .models import paymentdetails
from inventory.models import inventoryreq

global items_added
items_added=[]

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
        last_instance=paymentdetails.objects.last()
        last_instance.amount=amount
        last_instance.save()

    transdetail=paymentdetails.objects.last()
    context={
        'items_added': items_added ,
        'tcol': inventorytablecolumn,
        'transdetail':transdetail,
        'amount':amount
    }
    return render(request, 'transadditem.html', context)

def payment_confirmed(request):
    items_added.clear()
    return render(request, 'paymentconfirmed.html')

def cancel(request):
    items_added.clear()
    paymentdetails.objects.last().delete()
    return render(request, "cancelled.html")

def record(request):
    trans_instance=paymentdetails.objects.all()
    table_columns=["Transaction ID", "Customer Phone No.", "Transaction Date","Cash","Card","Amount"]
    context={
        'tcol':table_columns,
        'record_instance':trans_instance
    }
    return render(request, 'record.html',context)
    


# Create your views here.
