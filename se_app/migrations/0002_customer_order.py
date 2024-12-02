# Generated by Django 5.1.2 on 2024-11-06 11:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("se_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=50)),
                ("address", models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("date", models.DateField()),
                ("status", models.CharField(max_length=30)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="se_app.customer",
                    ),
                ),
                ("products", models.ManyToManyField(to="se_app.product")),
            ],
        ),
    ]