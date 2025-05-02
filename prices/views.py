from rest_framework import viewsets
from .models import BitcoinPrice
from .serializers import BitcoinPriceSerializer

class BitcoinPriceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BitcoinPrice.objects.all().order_by('-timestamp')
    serializer_class = BitcoinPriceSerializer