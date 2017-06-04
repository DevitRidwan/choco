from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.admin import widgets
from django.db.models import Q
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

class UserForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')

class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	email = forms.EmailField(max_length=254, help_text='Gunakan alamat email yang valid')

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class ProfileForm(forms.ModelForm):

	class Meta:
		model = Profile
		fields = ('photo', 'nama', 'tgl_lahir', 'status', 'bio', 'alamat')


class AddUSerForm(forms.Form):
	email = forms.EmailField(max_length=254, help_text='Gunakan alamat email yang valid')

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'
    