from django.urls import path, include
from .views import inventorytableview, inventoryadditemview

app_name = 'inventory'

urlpatterns = [
    path('', inventorytableview, name='inven_home'),
    path('additem', inventoryadditemview, name='inventory_additem')
]
