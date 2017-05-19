from .models import Pemasukan, Pengeluaran, Rekap
from produk.models import Item, Formula
from django import forms

class PemasukanForm(forms.ModelForm):
	if Pemasukan.objects.count()<=0:
		kd_masuk = forms.CharField(max_length=11, initial='10000000000')
	else:
		kode = Pemasukan.objects.latest('pk').kd_masuk
		kode = int(kode)+1
		kd_masuk = forms.CharField(max_length=11, initial=kode)
	class Meta:
		model = Pemasukan
		#widgets = {'kd_masuk': forms.HiddenInput()}
		fields = '__all__'

class PengeluaranForm(forms.ModelForm):
	class Meta:
		model = Pengeluaran
		fields = '__all__'
