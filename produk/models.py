from __future__ import unicode_literals

from django.db import models
from datetime import date
from decimal import Decimal
from django.core.urlresolvers import reverse
#from .formula import pembuatan

class Bahan(models.Model):
	kd_bahan = models.CharField(max_length=11, primary_key=True)
	nama = models.CharField(max_length=25)
	item = models.ManyToManyField('Item')
	stok = models.IntegerField(default=0)

	def __str__(self):
		return self.nama

class Formula(Bahan):
	jumlah = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, help_text='dalam gram')
	
	def get_items(self):
		return "\n".join([p.item for p in self.item.all()])

class Item(models.Model):
	#image = 
	kd_item = models.CharField(max_length=11, primary_key=True)
	nama = models.CharField(max_length=25)
	harga = models.DecimalField(max_digits=9, decimal_places=2)
	stok = models.IntegerField(default=0)

	def __str__(self):
		return self.nama