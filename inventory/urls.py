from django.urls import path,include
from .views import inventorytableview,inventoryadditemview

app_name='inventory'

urlpatterns=[
    path('', inventorytableview ),
    path('additem',inventoryadditemview)
]