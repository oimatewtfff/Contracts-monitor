from django.db import models


class Contracts(models.Model):
    id = models.IntegerField(primary_key=True)
    contract = models.IntegerField(null=True)
    price_usd = models.IntegerField(null=True)
    price_rub = models.IntegerField(null=True)
    date = models.DateField(null=True)
