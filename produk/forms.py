from .models import Item, Formula
from django.forms import ModelForm

class ItemForm(ModelForm):
	class Meta:
		model = Item
		fields = '__all__'

class BahanForm(ModelForm):
	class Meta:
		model = Formula
		fields = '__all__'