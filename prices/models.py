from django.db import models

class BitcoinPrice(models.Model):
    price_usd = models.DecimalField(max_digits=20, decimal_places=8)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.timestamp}: ${self.price_usd}"