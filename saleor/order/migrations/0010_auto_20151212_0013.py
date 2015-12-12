# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_prices.models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_auto_20151201_0820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_net',
            field=django_prices.models.PriceField(currency='USD', decimal_places=2, null=True, blank=True, max_digits=12, verbose_name='total'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_tax',
            field=django_prices.models.PriceField(currency='USD', decimal_places=2, null=True, blank=True, max_digits=12, verbose_name='total'),
        ),
    ]
