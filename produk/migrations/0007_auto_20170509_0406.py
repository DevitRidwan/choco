# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 04:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produk', '0006_auto_20170509_0306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formula',
            name='jumlah',
            field=models.DecimalField(decimal_places=2, help_text='dalam gram', max_digits=9, null=True),
        ),
    ]
