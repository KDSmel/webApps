# Generated by Django 5.1.3 on 2024-11-09 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Alert",
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
                ("vehicle_id", models.CharField(max_length=20)),
                ("timestamp", models.DateTimeField()),
                ("alert_type", models.CharField(max_length=100)),
                ("location", models.CharField(max_length=50)),
                ("severity", models.CharField(max_length=10)),
            ],
        ),
    ]