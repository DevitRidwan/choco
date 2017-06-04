from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from profil.decorators import group_required
from .models import Item, Formula
from .forms import BahanForm, ItemForm
import sys
sys.path.append("choco/libs")
import calc_produk

"""Items"""
"""@group_required('Dev-It', 'Is-User')
def Item(request):
	items = Item.objects.all()
	return render(request, 'items.html')"""

"""data produk"""
@group_required('Dev-It', 'Is-User')
def ProdukView(request):
	return render(request, 'produk/produk.html')

@group_required('Dev-It', 'Is-User')
def ProdukDetail(request, pk):
	item = get_object_or_404(Item, pk=pk)
	return render(request, 'produk/produk-detail.html', {'item':item})

@group_required('Dev-It', 'Is-User')
def ProdukTambah(request):
	form = ItemForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect(ProdukView)
	return render(request, 'produk/produk-tambah.html', {'form':form})

@group_required('Dev-It', 'Is-User')
def ProdukEdit(request, pk):
	item = get_object_or_404(Item, pk=pk)
	form = ItemForm(request.POST or None, instance=item)
	if form.is_valid():
		form.save()
		return redirect(reverse('produk-detail', args=(item.kd_item,)))
	return render(request, 'produk/produk-edit.html', {'form':form})

@group_required('Dev-It', 'Is-User')
def ProdukDelete(request, id):
	item = get_object_or_404(Item, pk=pk)
	if request.method=='POST':
		item.delete()
		return redirect(ProdukView)
	return render(request, 'produk/produk-delete,html', {'object':item})

"""data bahan"""
@group_required('Dev-It', 'Is-User')
def BahanView(request):
	bahan = Formula.objects.order_by('nama')
	return render(request, 'bahan/bahan.html', {'bahan':bahan})

@group_required('Dev-It', 'Is-User')
def BahanDetail(request, pk):
	bahan = get_object_or_404(Formula, pk=pk)
	return render(request, 'bahan/bahan-detail.html', {'bahan':bahan})

@group_required('Dev-It', 'Is-User')
def BahanEdit(request, pk):
	form = BahanForm(request.POST or None, instance=bahan)
	if form.is_valid():
		form.save()
		return redirect(reverse('bahan-detail', args=(bahan.kd_bahan,)))
	return render(request, 'bahan/bahan-edit.html', {'form':form})

@group_required('Dev-It', 'Is-User')
def BahanDelete(request, id):
	bahan = get_object_or_404(Formula, id=id)
	if request.method=='POST':
		bahan.delete()
		return redirect(BahanView)
	return render(request, 'bahan/bahan-delete.html', {'object':bahan})

@group_required('Dev-It', 'Is-User')
def BahanTambah(request):
	form = BahanForm(request.POST or None)
	if form.is_valid():
		pk = form.cleaned_data['kd_bahan']
		form.save()
		return redirect(BahanView)
	return render(request, 'bahan/bahan-tambah.html', {'form':form})