# Generated by Django 4.1.7 on 2023-04-02 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0003_cartitem_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='total_price',
            field=models.FloatField(default=0.0),
        ),
    ]
