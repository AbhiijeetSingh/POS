from django.db import models

class paymentdetails(models.Model):
    customer_phoneno=models.IntegerField(blank=False)
    payment_date=models.DateTimeField(blank=True)
    cash=models.BooleanField(blank=True, default=True)
    card=models.BooleanField(blank=True)

class recordmodel(models.Model):
    payment_id=models.ForeignKey('paymentdetails',on_delete=models.CASCADE)
    amount=models.DecimalField(blank=False, decimal_places=2, max_digits=10000)


# Create your models here.
