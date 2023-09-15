from django.db import migrations, models


def create_initial_currency(apps):
    Currency = apps.get_model("usdrub", "Currency")
    Currency.objects.create(currency_name="USD", currency_rate=1.0)


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Currency",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("currency_name", models.CharField(max_length=20)),
                (
                    "currency_rate",
                    models.FloatField(default=0.0),
                ),
            ],
        ),
        migrations.RunPython(create_initial_currency),
    ]
