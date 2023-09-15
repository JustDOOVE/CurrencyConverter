import requests
from . import models
from django.core.exceptions import ObjectDoesNotExist


def get_rates(api_key: str) -> dict | None:
    """
    We get the cost of all available currencies relative to the dollar.
    If you specify specific currencies in the parameters for currencies, then only data will be received for them.
    For example: "currencies": "RUB,EUR,DKK,CZK"
    """
    url = "http://apilayer.net/api/live"
    params = {
        "access_key": api_key,
        "currencies": "",
        "source": "USD",
    }
    response = requests.get(url, params=params)
    data = response.json()
    if "quotes" in data:
        return data["quotes"]
    return None


def write_currency(data: dict) -> None:
    """write down the currency ticker and rate if they are not in the database, otherwise just update the rate"""
    for currency, rate in data.items():
        try:
            db_obj = models.Currency.objects.get(currency_name=currency[3:])
            db_obj.currency_rate = rate
        except ObjectDoesNotExist:
            db_obj = models.Currency(currency_name=currency[3:], currency_rate=rate)
        db_obj.save()
