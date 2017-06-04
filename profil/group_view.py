from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import Group
from .forms import GroupForm

def GroupView(request):
	group = Group.objects.all()
	return render(request, 'group/groups.html')

def AddGruop(request):
	form = GroupForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect(GroupView)
	return render(request, 'group/add-groups.html', {'form':form})