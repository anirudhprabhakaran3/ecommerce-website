# Generated by Django 4.1.7 on 2023-04-01 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0002_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='total_price',
            field=models.FloatField(default=0.0),
        ),
    ]
