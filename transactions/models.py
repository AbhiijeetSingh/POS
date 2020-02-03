from django.db import models


class paymentdetails(models.Model):
    customer_phoneno = models.IntegerField(blank=False)
    payment_date = models.DateTimeField(auto_now_add=True)
    cash = models.BooleanField(blank=True, default=True)
    card = models.BooleanField(blank=True)
    amount = models.DecimalField(
        blank=True, decimal_places=2, max_digits=10000, null=True)


# Create your models here.
