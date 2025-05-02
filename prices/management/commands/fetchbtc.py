from django.core.management.base import BaseCommand
from prices.cron import fetch_btc_price

class Command(BaseCommand):
    help = 'Fetch the last Bitcoin price and save it to the database.'

    def handle(self, *args, **kwargs):
        fetch_btc_price()
        self.stdout.write(self.style.SUCCESS('Sucessfully fetched the last Bitcoin Price.'))