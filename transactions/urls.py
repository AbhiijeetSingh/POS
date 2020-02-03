from django.urls import path
from .views import transchoice, makepayment, addtransitem, record, payment_confirmed, cancel

app_name = 'transactions'

urlpatterns = [
    path('', transchoice, name='trans_home'),
    path('makepayment', makepayment),
    path('makepayment/transadditem', addtransitem),
    path('makepayment/paymentconfirmed', payment_confirmed),
    path('makepayment/cancel', cancel),
    path('records', record),
]
