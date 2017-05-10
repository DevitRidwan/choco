from django.conf.urls import url
from . import views

urlpatterns = [
	#url item
	url(r'^$', views.ItemView, name='item'),
	url(r'^/(?P<pk>[0-9]+)$', views.ItemDetail, name='item-detail'),
	url(r'^/(?P<pk>[0-9]+)/edit/$', views.ItemEdit, name='item-edit'),
	url(r'^/tambah/$', views.ItemTambah, name='item-tambah'),
	url(r'^(?P<pk>[0-9]+)/delete/$', views.ItemDelete, name='item-delete'),
	#url bahan
	url(r'^/bahan$', views.BahanView, name='bahan'),
	url(r'^/bahan/(?P<pk>[0-9]+)$', views.BahanDetail, name='bahan-detail'),
	url(r'^/bahan/(?P<pk>[0-9]+)/edit/$', views.BahanEdit, name='bahan-edit'),
	url(r'^/bahan/tambah/$', views.BahanTambah, name='bahan-tambah'),
	url(r'^/bahan(?P<pk>[0-9]+)/delete/$', views.BahanDelete, name='bahan-delete'),
]