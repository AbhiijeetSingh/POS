from django import forms
from .models import inventoryreq


class additemform(forms.ModelForm):
    class Meta:
        model = inventoryreq
        fields = [
            'item_name',
            'quantity',
            'bought_price',
            'retail_price',
            'expire_date'
        ]
