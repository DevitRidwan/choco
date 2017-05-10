# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-06 08:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produk', '0005_auto_20170503_1216'),
        ('inventory', '0004_pengeluaran_keterangan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pemasukan',
            name='item',
        ),
        migrations.AddField(
            model_name='pemasukan',
            name='item',
            field=models.ManyToManyField(to='produk.Item'),
        ),
        migrations.RemoveField(
            model_name='pengeluaran',
            name='bahan',
        ),
        migrations.AddField(
            model_name='pengeluaran',
            name='bahan',
            field=models.ManyToManyField(to='produk.Bahan'),
        ),
    ]
