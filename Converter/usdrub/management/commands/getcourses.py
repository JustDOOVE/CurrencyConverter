import time
from ... import utils
from django.core.management.base import BaseCommand

# This is my API key.
# You can use it.
# But I advise you to visit https://currencylayer.com/ and get your own.
API_KEY = "620b8d3b1bc241a49d9a45c8a159e4df"


class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        We update exchange rates once a day.
        The API is limited to 1000 requests.
        However, there is a $10 plan that allows you to run queries about once every 5 minutes for a month.
        """
        while True:
            currencies = utils.get_rates(API_KEY)
            if currencies:
                utils.write_currency(currencies)
            time.sleep(60 * 60 * 24)

