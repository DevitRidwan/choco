from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

from .models import Profile
from .forms import UserForm, SignUpForm
from .decorators import group_required

from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			karyawan = User.objects.all()
			return redirect('home')
	else:
		form = SignUpForm()
	return render(request, 'signup.html', {'form':form})

@login_required
def edit_profile(request, pk):
	user = User.objects.get(pk=pk)
	user_form = UserForm(instance=user)

	ProfileInlineFormset = inlineformset_factory(User, Karyawan, fields=('bio', 'alamat', 'tgl_lahir'))
	formset = ProfileInlineFormset(instance=user)

	if request.user.is_authenticated() and request.user.id == user.id:
		if request.method == "POST":
			user_form = UserForm(request.POST, request.FILES, instance=user)
			formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)
			if user_form.is_valid():
				created_user = user_form.save(commit=False)
				formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)
				if formset.is_valid():
					created_user.save()
					formset.save()
					return HttpResponseRedirect('/account/profile/')
		return render(request, "profile_update.html", {
			"user":pk,
			"user_form":user_form,
			"formset":formset,
			})
	else:
		raise PermissionDenied

@login_required
@group_required('Dev-It')
def AddUser(profile):
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

		username = name + str(profile.pk) + get_tgl
		password = User.objects.make_random_password()

		#create User
		profile.username = username
		profile.save()
		user_create = User(username=username)
		user_create.save()
		user_create.set_password(password)
		user_create.save()

		return render(request, 'add-user.html', {'username':username, 'password':password})
	else:
		message = str(profile.nama) + ' sudah terdaftar'
		return render(request, 'add-user.html', {'message':message})
