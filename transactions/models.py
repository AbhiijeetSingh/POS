from django.db import models

class paymentdetails(models.Model):
    customer_phoneno=models.IntegerField(blank=False)
    payment_date=models.DateTimeField(auto_now=True)
    cash=models.BooleanField(blank=True, default=True)
    card=models.BooleanField(blank=True)

class recordmodel(models.Model):
    trans_id=models.IntegerField(blank=False)
    items_ids=models.TextField()
    items_quantity=models.TextField()
    amount=models.DecimalField(blank=False, decimal_places=2, max_digits=10000)


# Create your models here.
