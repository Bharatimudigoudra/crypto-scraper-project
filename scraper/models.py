# scraper/models.py

from django.db import models

class CryptoCoin(models.Model):
    name = models.CharField(max_length=100)
    acronym = models.CharField(max_length=10, unique=True)
    price = models.DecimalField(max_digits=20, decimal_places=10)
    price_change = models.DecimalField(max_digits=20, decimal_places=10)
    market_cap = models.BigIntegerField()
    market_cap_rank = models.IntegerField()
    volume = models.BigIntegerField()
    volume_rank = models.IntegerField()
    volume_change = models.DecimalField(max_digits=10, decimal_places=2)
    circulating_supply = models.BigIntegerField()
    total_supply = models.BigIntegerField()
    diluted_market_cap = models.BigIntegerField()

    def __str__(self):
        return self.name
