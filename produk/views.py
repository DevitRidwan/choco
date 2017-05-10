from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Formula
from django.http import HttpResponseRedirect
from django.forms import ModelForm
from django.urls import reverse
import sys
sys.path.append("choco/libs")
from calc_produk import view_stok

"""data item"""

class ItemForm(ModelForm):
	class Meta:
		model = Item
		fields = '__all__'

def ItemView(request):
	items = Item.objects.order_by('nama')
	view = zip(items, view_stok(items))
	return render(request, 'item/item.html', {'items':items, 'view':view})

def ItemDetail(request, pk):
	item = get_object_or_404(Item, pk=pk)
	return render(request, 'item/item-detail.html', {'item':item})

def ItemEdit(request, pk):
	item = get_object_or_404(Item, pk=pk)
	form = ItemForm(request.POST or None, instance=item)
	if form.is_valid():
		form.save()
		return redirect(reverse('item-detail', args=(item.kd_item,)))
	return render(request, 'item/item-edit.html', {'form':form})

def ItemDelete(request, id):
	item = get_object_or_404(Item, pk=pk)
	if request.method=='POST':
		item.delete()
		return redirect(Item)
	return render(request, 'item/item-delete,html', {'object':item})

def ItemTambah(request):
	form = ItemForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect(ItemView)
	return render(request, 'item/item-tambah.html', {'form':form})

"""data bahan"""

class BahanForm(ModelForm):
	class Meta:
		model = Formula
		fields = '__all__'

def BahanView(request):
	bahan = Formula.objects.order_by('nama')
	return render(request, 'bahan/bahan.html', {'bahan':bahan})

def BahanDetail(request, pk):
	bahan = get_object_or_404(Formula, pk=pk)
	return render(request, 'bahan/bahan-detail.html', {'bahan':bahan})

def BahanEdit(request, pk):
	form = BahanForm(request.POST or None, instance=bahan)
	if form.is_valid():
		form.save()
		return redirect(reverse('bahan-detail', args=(bahan.kd_bahan,)))
	return render(request, 'bahan/bahan-edit.html', {'form':form})

def BahanDelete(request, id):
	bahan = get_object_or_404(Formula, id=id)
	if request.method=='POST':
		bahan.delete()
		return redirect(BahanView)
	return render(request, 'bahan/bahan-delete.html', {'object':bahan})

def BahanTambah(request):
	form = BahanForm(request.POST or None)
	if form.is_valid():
		pk = form.cleaned_data['kd_bahan']
		form.save()
		return redirect(BahanView)
	return render(request, 'bahan/bahan-tambah.html', {'form':form})