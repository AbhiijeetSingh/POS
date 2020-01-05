from django.shortcuts import render
from .form import paymentform
from .models import paymentdetails, recordmodel
from inventory.models import inventoryreq

global invenobj, itemids, itemquantity
inveninstance=inventoryreq.objects.all()
itemids=[]
itemquantity=[]

def transchoice(request):
    return render(request, 'transchoice.html', {})


def makepayment(request):
    form=paymentform(request.POST or None)
    if form.is_valid():
        form.save()
    context={
        'form':form
    }
    return render(request, 'payment.html',context)


def addtransitem(request):
    amount=0
    items_added=[]
    inventorytablecolumn=["ID",'Item Name','Selling Price (Per Unit)', 'Expiry Date',"Quantity"]
    
    if request.POST.get('item_id')!=None:
        itemids.append(int(request.POST.get("item_id")))
        itemquantity.append(int(request.POST.get('item_quantity')))

    items_added=itemlistadder()
        
    for value in range(len(items_added)):
        amount=amount+(items_added[value][2]*items_added[value][4])

    transdetail=paymentdetails.objects.all()
    context={
        'items_added': items_added ,
        'tcol': inventorytablecolumn,
        'itemquantity':itemquantity,
        'transdetail':transdetail,
        'amount':amount
    }
    return render(request, 'transadditem.html', context)

def record(request):
    trans=paymentdetails.objects.all()
    recordmodel.items
    context={
        'transaction':trans
    }
    return render(request, 'record.html', context)
    
def itemlistadder():
    items_list=[]
    for index in range(len(inveninstance)):
            if inveninstance[index].id in itemids:
                items_list.append([inveninstance[index].id,
                                    inveninstance[index].item_name,
                                    inveninstance[index].retail_price,
                                    inveninstance[index].expire_date,
                                    itemquantity[index]]
                                    )
    return items_list


# Create your views here.
