from django.http import JsonResponse
from .models import Currency
from django.core.exceptions import ObjectDoesNotExist


def convert_currency(request) -> JsonResponse:
    # take form values from the request
    from_currency = request.GET.get("from").upper()
    to_currency = request.GET.get("to").upper()
    try:
        value = float(request.GET.get("value", 1))
    except ValueError:
        return JsonResponse({"error": "value field can only be digit or float"})

    try:
        # checking the presence of a ticker in the database
        from_currency_obj = Currency.objects.get(currency_name=from_currency)
        to_currency_obj = Currency.objects.get(currency_name=to_currency)
    except ObjectDoesNotExist:
        return JsonResponse({"error": "currency ticker not found"})

    # checking various cases of requests regarding USD
    if from_currency == "USD":
        converted_value = to_currency_obj.currency_rate * value
    elif to_currency == "USD":
        converted_value = (1 / from_currency_obj.currency_rate) * value
    else:
        converted_value = (1 / from_currency_obj.currency_rate) * to_currency_obj.currency_rate * value

    return JsonResponse({"result": round(converted_value, 2)})
