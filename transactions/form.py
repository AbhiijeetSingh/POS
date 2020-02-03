from django import forms
from .models import paymentdetails


class paymentform(forms.ModelForm):
    class Meta:
        model = paymentdetails
        fields = [
            'customer_phoneno',
            'cash',
            'card',
        ]
