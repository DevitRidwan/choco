# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class karyawan(User):
	nama = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(max_length=500, blank=True)
	alamat = models.CharField(max_length=30, blank=True)
	tgl_lahir = models.DateField(null=True, blank=True)