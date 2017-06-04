# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import date
from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
STATUS = (
	('f', 'Founder'),
	('p', 'Pegawai'),
	)

date_format = date.today().year - 25

class Profile(models.Model):
	photo = models.ImageField(null=True, blank=True)
	#username = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
	username = models.CharField(max_length=15, blank=True, editable=False)
	group = models.CharField(max_length=15, blank=True, editable=False)
	status_user = models.BooleanField(default=False, editable=False)
	nama = models.CharField(max_length=50)
	status = models.CharField(max_length=1, choices=STATUS)
	#user = models.OneToOneField(User, related_name='user', null=True)
	bio = models.TextField(max_length=500, blank=True)
	alamat = models.CharField(max_length=30, blank=True)
	tgl_lahir = models.DateField(default=date(date_format,1,1))

	def __unicode__(self):
		return str(self.nama)

