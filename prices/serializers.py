from rest_framework import serializers
from .models import BitcoinPrice

class BitcoinPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BitcoinPrice
        fields = ['id', 'price_usd', 'timestamp']