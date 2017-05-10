from django.conf.urls import url
from . import views

urlpatterns = [
	#url(r'^$', views.Inventory, name='inventory'),
	#url pemasukan
	url(r'^/pemasukan/$', views.PemasukanView, name='pemasukan'),
	url(r'^/pemasukan/(?P<pk>[0-9]+)$', views.PemasukanDetail, name='pemasukan-detail'),
	url(r'^/pemasukan/(?P<pk>[0-9]+)/edit/$', views.PemasukanEdit, name='pemasukan-edit'),
	url(r'^/pemasukan/tambah/$', views.PemasukanTambah, name='pemasukan-tambah'),
	url(r'^/pemasukan/(?P<pk>[0-9]+)/delete/$', views.PemasukanDelete, name='pemasukan-delete'),
	#url pengeluaran
	url(r'^/pengeluaran$', views.PengeluaranView, name='pengeluaran'),
	url(r'^/pengeluaran/(?P<pk>[0-9]+)$', views.PengeluaranDetail, name='pengeluaran-detail'),
	url(r'^/pengeluaran/(?P<pk>[0-9]+)/edit/$', views.PengeluaranEdit, name='pengeluaran-edit'),
	url(r'^/pengeluaran/tambah/$', views.PengeluaranTambah, name='pengeluaran-tambah'),
	url(r'^/pengeluaran(?P<pk>[0-9]+)/delete/$', views.PengeluaranDelete, name='pengeluaran-delete'),
]