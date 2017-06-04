from django.conf.urls import url
from . import views

urlpatterns = [
	#url main items
	url(r'^$', views.ProdukView, name='item'),

	#url produk
	url(r'^/produk/$', views.ProdukView, name='produk'),
	url(r'^/produk/(?P<pk>[0-9]+)$', views.ProdukDetail, name='produk-detail'),
	url(r'^/produk/(?P<pk>[0-9]+)/edit/$', views.ProdukEdit, name='produk-edit'),
	url(r'^/produk/tambah/$', views.ProdukTambah, name='produk-tambah'),
	url(r'^produk/(?P<pk>[0-9]+)/delete/$', views.ProdukDelete, name='produk-delete'),
	#url bahan
	url(r'^/bahan$', views.BahanView, name='bahan'),
	url(r'^/bahan/(?P<pk>[0-9]+)$', views.BahanDetail, name='bahan-detail'),
	url(r'^/bahan/(?P<pk>[0-9]+)/edit/$', views.BahanEdit, name='bahan-edit'),
	url(r'^/bahan/tambah/$', views.BahanTambah, name='bahan-tambah'),
	url(r'^/bahan(?P<pk>[0-9]+)/delete/$', views.BahanDelete, name='bahan-delete'),
]