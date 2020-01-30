from django.urls import path
from .views import transchoice,makepayment, addtransitem,record, payment_confirmed

app_name='transactions'

urlpatterns=[
    path('',transchoice),
    path('makepayment',makepayment),
    path('makepayment/transadditem',addtransitem ),
    path('makepayment/paymentconfirmed', payment_confirmed),
    path('records',record),
]