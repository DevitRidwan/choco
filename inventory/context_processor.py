import sys
sys.path.append("choco/libs")
from calc_produk import view_stok
from produk.models import Item, Formula
from .models import Pengeluaran, Pemasukan, ModalAwal
from datetime import date

items = Item.objects.all()
formulas = Formula.objects.all()
incomes = Pemasukan.objects.all()
expenses = Pengeluaran.objects.all()
modal = ModalAwal.objects.all()

def all(request):
	return {'view':estimasi_stok(), 'all_tahun':per_tahun(), 'bencos':benfcos()}

def estimasi_stok():
	views = zip(items, view_stok(items))
	return views

def inventory_all(tahun):
	tot_in = 0
	tot_out = 0
	for pemasukan in incomes.filter(tanggal__year=tahun):
		tot_in += tot_in + pemasukan.total_harga
	for pengeluaran in expenses.filter(tanggal__year=tahun):
		tot_out += tot_out + (pengeluaran.jumlah * pengeluaran.harga)
	return tot_in, tot_out

def per_tahun():
	lists = {}
	if incomes.count() > 1:
		for x, masuk in incomes:
			if not masuk.tanggal.year == incomes[x-1].tanggal.year:
				lists[incomes[x-1].tanggal.year]=inventory_all(masuk.tanggal.year)
				if (not incomes[x+1].exists()) and masuk.tanggal.year == incomes[x-1].tanggal.year:
					lists[masuk.tanggal.year]=inventory_all((masuk.tanggal.year))
	else:
		lists[incomes[0].tanggal.year]=inventory_all(incomes[0].tanggal.year)
	return lists

def benfcos():
	total_in = modal[modal.count()-1].modal
	for pemasukan in incomes:
		total_in += pemasukan.total_harga
	total_out = 0
	for pengeluaran in expenses:
		total_out += (pengeluaran.harga * pengeluaran.jumlah)
	return total_in - total_out