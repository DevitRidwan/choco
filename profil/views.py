# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import ProfileForm, AddUSerForm
from .models import Profile
from .main_profile import AddUser
from .decorators import group_required

@group_required('Dev-It')
def ProfileView(request):
	profiles = Profile.objects.all()
	return render(request, 'profiles.html', {'profiles':profiles})

@group_required('Dev-It')
def ProfileDetail(request, pk):
	profile = Profile.objects.get(pk=pk)
	return render(request, 'profile-detail.html', {'profile':profile})

@group_required('Dev-It')
def ProfileCreate(request):
	form = ProfileForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect(ProfileView)
	return render(request, 'profile-tambah.html', {'form':form})

@group_required('Dev-It')
def ProfileEdit(request, pk):
	profile = get_object_or_404(Profile, pk=pk)
	form = ProfileForm(request.POST or None, instance=profile)
	if form.is_valid():
		form.save()
		return redirect(reverse('profile-detail', args=(profile.pk,)))
	return render(request, 'profile-edit.html', {'form':form, 'profile':profile})

@group_required('Dev-It')
def ProfileDelete(request, pk):
	profile = get_object_or_404(Profile, pk=pk)
	if request.method=='POST':
		profile.delete()
		return redirect(ProfileView)
	return render(request, 'profile-delete.html', {'object':profile})

@group_required('Dev-It')
def TambahUSer(request,	pk):
	profile = Profile.objects.get(pk=pk)
	if profile.status_user == False:
		nama = str(profile.nama)
		name = nama[0]
		hari = str(profile.tgl_lahir.day)
		if len(hari) < 2:
			hari="0"+hari
		bulan = str(profile.tgl_lahir.month)
		if len(bulan) < 2:
			bulan="0"+bulan
		tahun = str(profile.tgl_lahir.year)[2] + str(profile.tgl_lahir.year)[3]
		get_nama = [pos for pos, nchar in enumerate(nama) if nchar == ' ']
		get_tgl = hari+bulan+tahun
		for user in get_nama:
			name += nama[user+1]
		from django.contrib.auth.models import User
		username = name + str(profile.pk) + get_tgl
		password = User.objects.make_random_password()

		#create User
		profile.username = username
		profile.status_user = True
		profile.save()
		user_create = User(username=username)
		user_create.save()
		user_create.set_password(password)
		user_create.save()

		return render(request, 'add-user.html', {'username':username, 'password':password})
	else:
		message = str(profile.nama) + ' sudah terdaftar'
		return render(request, 'add-user.html', {'message':message})