# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-06 09:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produk', '0005_auto_20170503_1216'),
        ('inventory', '0005_auto_20170506_0808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pemasukan',
            name='item',
        ),
        migrations.AddField(
            model_name='pemasukan',
            name='item',
            field=models.ForeignKey(default=1009, on_delete=django.db.models.deletion.CASCADE, to='produk.Item'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='pengeluaran',
            name='bahan',
        ),
        migrations.AddField(
            model_name='pengeluaran',
            name='bahan',
            field=models.ForeignKey(default=1000, on_delete=django.db.models.deletion.CASCADE, to='produk.Bahan'),
            preserve_default=False,
        ),
    ]
