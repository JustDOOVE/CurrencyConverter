from django.db import models


class Currency(models.Model):
    currency_name = models.CharField(max_length=20)
    currency_rate = models.FloatField(default=0.0)
