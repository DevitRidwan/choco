from __future__ import unicode_literals

from django.db import models
from datetime import date
from decimal import Decimal
from produk import models as produk

class Pemasukan(models.Model):
	kd_masuk = models.CharField(max_length=11, primary_key=True)
	tanggal = models.DateField(default=date.today)
	item = models.ForeignKey('produk.Item')
	jumlah = models.IntegerField(default=1)
	keterangan = models.CharField(max_length=50)
	total_harga = models.IntegerField(default=0)

	class Meta:
		ordering = ['tanggal']

	def __unicode__(self):
		return str(self.tanggal)

class Pengeluaran(models.Model):
	kd_keluar = models.CharField(max_length=11, primary_key=True)
	tanggal = models.DateField(default=date.today)
	item = models.ForeignKey('produk.Bahan')
	harga = models.IntegerField()
	keterangan = models.CharField(max_length=75, blank=True, help_text="jika pembelian tidak ada di kolom bahan")
	jumlah = models.IntegerField(default=1)

	class Meta:
		ordering = ['tanggal']

	def __unicode__(self):
		return str(self.tanggal)

class Rekap(models.Model):
	tanggal = models.DateField(default=date.today)
	pemasukan = models.ForeignKey(Pemasukan)
	tot_masuk = models.DecimalField(max_digits=9, decimal_places=2, help_text='Total Pemasukan')
	pengeluaran = models.ForeignKey(Pengeluaran)
	tot_keluar = models.DecimalField(max_digits=9, decimal_places=2, help_text='Total Pengeluaran')

class ModalAwal(models.Model):
	modal = models.IntegerField()