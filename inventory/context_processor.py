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

#---------main---------
def all(request):
	return {'view':estimasi_stok(), 'inven_all':grand_total(), 'inven_bulan':per_bulan(), 'total_thn':total_tahun(), 'total_bln':total_bulan()}

#--------estimasi stok---------
def estimasi_stok():
	views = zip(items, view_stok(items))
	return views

#--------abstrak inventory--------
def inventory_all(tahun):
	tot_in = 0
	tot_out = 0
	for pemasukan in incomes.filter(tanggal__year=tahun):
		tot_in = tot_in + pemasukan.total_harga
	for pengeluaran in expenses.filter(tanggal__year=tahun):
		tot_out = tot_out + (pengeluaran.jumlah * pengeluaran.harga)
	return tot_in, tot_out

def inventory_tahun(tahun, bulan):
	tot_in = 0
	tot_out = 0
	for pemasukan in incomes.filter(tanggal__year=tahun, tanggal__month=bulan):
		tot_in = tot_in + pemasukan.total_harga
	for pengeluaran in expenses.filter(tanggal__year=tahun, tanggal__month=bulan):
		tot_out = tot_out + (pengeluaran.jumlah * pengeluaran.harga)
	return tot_in, tot_out

#---------benefit cost-----------
def grand_total():
	lists = []
	x = 0
	for masuk in incomes:
		lists_inven = []
		#if not ((inventory_all(masuk.tanggal.year)[0]==0) and (inventory_all(masuk.tanggal.year)[1]==0)):
		tot_inven_tahun = inventory_all(masuk.tanggal.year)[0]-inventory_all(masuk.tanggal.year)[1]
		if x==0:
			lists_inven.extend((masuk.tanggal.year, inventory_all(masuk.tanggal.year)[0], inventory_all(masuk.tanggal.year)[1], tot_inven_tahun))
			lists.append(lists_inven)
		else:
			if not masuk.tanggal.year == incomes[x-1].tanggal.year:
				lists_inven.extend((masuk.tanggal.year, inventory_all(masuk.tanggal.year)[0], inventory_all(masuk.tanggal.year)[1], tot_inven_tahun))
				lists.append(lists_inven)
		x+=1
	return lists

def per_bulan():
	bulan = ['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember']
	lists = []
	x = 1
	in_tahun = incomes.filter(tanggal__year=date.today().year)
	while x <= date.today().month:
		lists_inven = []
		inven_tahun = inventory_tahun(date.today().year, x)
		tot_inven_bulan = inven_tahun[0]-inven_tahun[1]
		lists_inven.extend((bulan[x-1], inven_tahun[0], inven_tahun[1], tot_inven_bulan))
		lists.append(lists_inven)
		x+=1
	return lists

#---------total benefit cost---------
def benfcos():
	#total_in = modal[modal.count()-1].modal
	total_in=0
	for pemasukan in incomes:
		total_in = total_in + pemasukan.total_harga
	total_out = 0
	for pengeluaran in expenses:
		total_out = total_out + (pengeluaran.harga * pengeluaran.jumlah)
	return total_in - total_out

#----------counting----------
def total_tahun():
	total_in=0
	for pemasukan in incomes:
		total_in = total_in + pemasukan.total_harga
	total_out = 0
	for pengeluaran in expenses:
		total_out = total_out + (pengeluaran.harga * pengeluaran.jumlah)
	return total_in - total_out

def total_bulan():
	total_in=0
	for pemasukan in incomes.filter(tanggal__year=date.today().year):
		total_in = total_in + pemasukan.total_harga
	total_out = 0
	for pengeluaran in expenses.filter(tanggal__year=date.today().year):
		total_out = total_out + (pengeluaran.harga * pengeluaran.jumlah)
	return total_in - total_out