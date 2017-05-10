# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 11:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produk', '0003_auto_20170503_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='bahan',
            field=models.ForeignKey(default=1000, on_delete=django.db.models.deletion.CASCADE, related_name='item_bahan', to='produk.Formula'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bahan',
            name='item',
            field=models.ManyToManyField(related_name='bahan_item', to='produk.Item'),
        ),
    ]
