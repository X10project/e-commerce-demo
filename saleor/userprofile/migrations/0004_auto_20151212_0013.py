# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_auto_20151104_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city_area',
            field=models.CharField(verbose_name='district', blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='address',
            name='company_name',
            field=models.CharField(verbose_name='company or organization', blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='address',
            name='country_area',
            field=models.CharField(verbose_name='state or province', blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='address',
            name='street_address_1',
            field=models.CharField(verbose_name='address', max_length=256),
        ),
        migrations.AlterField(
            model_name='address',
            name='street_address_2',
            field=models.CharField(verbose_name='address', blank=True, max_length=256),
        ),
    ]
