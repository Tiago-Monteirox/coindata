from rest_framework.routers import DefaultRouter
from .views import BitcoinPriceViewSet

router = DefaultRouter()
router.register(r'prices', BitcoinPriceViewSet, basename='bitcoinprice')

urlpatterns = router.urls

# Assim, vamos obter automaticamente os endpoints:

# GET /api/prices/ → lista de preços
# GET /api/prices/<id>/ → detalhe de um registro de preço