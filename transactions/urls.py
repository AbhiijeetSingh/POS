from django.urls import path
from .views import transchoice,makepayment, addtransitem

app_name='transactions'

urlpatterns=[
    path('',transchoice),
    path('makepayment',makepayment),
    path('makepayment/transadditem',addtransitem )
]