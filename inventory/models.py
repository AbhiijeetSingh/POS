from django.db import models


class inventoryreq(models.Model):
    item_name = models.CharField(max_length=100, blank=False)
    quantity = models.IntegerField(blank=False)
    bought_price = models.DecimalField(
        max_digits=100000, decimal_places=2, blank=False)
    retail_price = models.DecimalField(
        max_digits=100000, decimal_places=2, blank=False)
    bought_date = models.DateField(blank=False, auto_now=True)
    expire_date = models.DateField(auto_now=False, null=True, blank=True)

# Create your models here.
