from django import forms
from .models import paymentdetails,recordmodel

class paymentform(forms.ModelForm):
    class Meta:
        model=paymentdetails
        fields=[
            'customer_phoneno',
            'cash',
            'card',
            
        ]
class recordform(forms.ModelForm):
    class Meta:
        model=recordmodel
        fields=[
            'payment_id',
            'amount',
        ]