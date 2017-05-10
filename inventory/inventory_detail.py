from .models import Pemasukan, Pengeluaran
from datetime import date

class InventoryView:
	pemasukan = Pemasukan.objects.all()
	pengeluaran = Pengeluaran.objects.all()

	def __init__(self, tahun, bulan):
		self.tahun = tahun
		self.bulan = bulan

	def Inventory(self):
		return self.pemasukan, self.pengeluaran

	def jual(self):
		pemasukan = self.pemasukan.filter(tanggal__year=self.tahun, tanggal__month=self.bulan)
		masuk=0
		tot_item=0
		tot_harga_item=0
		while masuk < pemasukan.count():
			tot_item += tot_item + pemasukan[masuk].jumlah
			tot_harga_item += tot_harga_item + pemasukan[masuk].item.harga
			masuk += 1
		return tot_item, tot_harga_item

	def beli(self):
		pembelian = self.pengeluaran.filter(tanggal__year=self.tahun, tanggal__month=self.bulan)
		beli=0
		tot_beli=0
		tot_harga_beli=0
		while beli < pengeluaran.count():
			tot_beli += tot_beli + pengeluaran[beli].jumlah
			tot_harga_beli += tot_harga_beli + pengeluaran[beli].bahan.harga
			masuk += 1
		return tot_beli, tot_harga_beli