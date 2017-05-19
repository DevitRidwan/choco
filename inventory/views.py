from django.shortcuts import render, get_object_or_404, redirect
from .models import Pemasukan, Pengeluaran, Rekap
from produk.models import Item, Formula
from django.urls import reverse
from django.utils import timezone
from .inventory_detail import InventoryView
from .forms import PemasukanForm, PengeluaranForm
from copy import deepcopy
import sys
sys.path.append("choco/libs")
import calc_produk

def Overview(request):
	view_pemasukan = InventoryView.pemasukan
	view_pengeluaran = InventoryView.pengeluaran
	tanggal_masuk = view_pemasukan.filter(tanggal__month=timezone.now().month)
	tanggal_keluar = view_pengeluaran.filter(tanggal__month=timezone.now().month)
	return render(request, 'inventory.html')

def PemasukanView(request):
	pemasukan = Pemasukan.objects.order_by('tanggal')
	return render(request, 'pemasukan/pemasukan.html', {'pemasukan':pemasukan})

def PemasukanDetail(request, pk):
	pemasukan = get_object_or_404(Pemasukan, pk=pk)
	return render(request, 'pemasukan/pemasukan-detail.html', {'pemasukan':pemasukan})

def PemasukanEdit(request, pk):
	pemasukan = get_object_or_404(Pemasukan, pk=pk)
	cache = deepcopy(pemasukan)
	form = PemasukanForm(request.POST or None, instance=pemasukan)
	if form.is_valid():
		jumlah = form.cleaned_data['jumlah']
		form.save()
		calc_produk.update_stok("in","edit",cache,jumlah)
		return redirect(reverse('pemasukan-detail', args=(pemasukan.pk,)))
	extra_context = {
		'form':form,
		'pemasukan':pemasukan
	}
	return render(request, 'pemasukan/pemasukan-edit.html', extra_context)

def PemasukanTambah(request):
	form = PemasukanForm(request.POST or None)
	if form.is_valid():
		masuk = form.cleaned_data['kd_masuk']
		jumlah = form.cleaned_data['jumlah']
		item = form.cleaned_data['item']
		if calc_produk.check_stok(item) >= jumlah:
			form.save()
			pemasukan = Pemasukan.objects.get(pk=masuk)
			calc_produk.update_stok("in","tambah",pemasukan,jumlah)
			return redirect(PemasukanView)
	return render(request, 'pemasukan/pemasukan-tambah.html', {'form':form})

def PemasukanDelete(request, pk):
	pemasukan = get_object_or_404(Pemasukan, pk=pk)
	if request.method=='POST':
		jumlah = pemasukan.jumlah
		calc_produk.update_stok("in","delete",pemasukan,jumlah)
		pemasukan.delete()
		return redirect(PemasukanView)
	return render(request, 'pemasukan/pemasukan-delete.html', {'object':pemasukan})

def PengeluaranView(request):
	pengeluaran = Pengeluaran.objects.order_by('tanggal')
	return render(request, 'pengeluaran/pengeluaran.html', {'pengeluaran':pengeluaran})

def PengeluaranDetail(request, pk):
	pengeluaran = get_object_or_404(Pengeluaran, pk=pk)
	return render(request, 'pengeluaran/pengeluaran-detail.html', {'pengeluaran':pengeluaran})

def PengeluaranEdit(request, pk):
	pengeluaran = Pengeluaran.objects.get(pk=pk)
	cache = deepcopy(pengeluaran)
	form = PengeluaranForm(request.POST or None, instance=pengeluaran)
	if form.is_valid():
		jumlah = form.cleaned_data['jumlah']
		calc_produk.update_stok("out","edit",cache,jumlah)
		form.save()
		return redirect(reverse('pengeluaran-detail', args=(pengeluaran.pk,)))
	extra_context = {
		'form':form,
		'pengeluaran':pengeluaran
	}
	return render(request, 'pengeluaran/pengeluaran-edit.html', extra_context)

def PengeluaranTambah(request):
	form = PengeluaranForm(request.POST or None)
	if form.is_valid():
		keluar = form.cleaned_data['kd_keluar']
		jumlah = form.cleaned_data['jumlah']
		form.save()
		pengeluaran = Pengeluaran.objects.get(pk=keluar)
		calc_produk.update_stok("out","tambah",pengeluaran,jumlah,harga)
		return redirect(PengeluaranView)
	return render(request, 'pengeluaran/pengeluaran-tambah.html', {'form':form})

def PengeluaranDelete(request, pk):
	pengeluaran = get_object_or_404(Pengeluaran, pk=pk)
	if request.method=='POST':
		jumlah = pengeluaran.jumlah
		pengeluaran.delete()
		calc_produk.update_stok("out","delete",pengeluaran,jumlah)
		return redirect(PengeluaranView)
	return render(request, 'pengeluaran/pengeluaran-delete.html', {'object':pengeluaran})