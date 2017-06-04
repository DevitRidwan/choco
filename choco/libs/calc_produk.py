from produk.models import Item, Formula

def check_stok(item):
	pre_stok = []
	filter_bahan = Formula.objects.filter(item__pk=item.pk)
	for bahan in filter_bahan:
		stok_bahan = int(bahan.stok/bahan.jumlah)
		pre_stok.append(stok_bahan)
	stoks = min(pre_stok)
	return stoks

def view_stok(items):
	list_stok = []
	for item in items:
		stok_item = item.stok + check_stok(item)
		list_stok.append(stok_item)
	return list_stok

def update_stok(status, sub_status, transaksi, jumlah):
	if status == "in":
		item = Item.objects.get(pk=transaksi.item_id)
		filter_bahan = Formula.objects.filter(item__pk=item.pk)
		transaksi.total_harga = jumlah * item.harga
		transaksi.save()
		for bahan in filter_bahan:
			if sub_status == "tambah":
				bahan.stok = bahan.stok - (jumlah * bahan.jumlah)
			elif sub_status == "edit":
				bahan.stok = bahan.stok + (transaksi.jumlah * bahan.jumlah)-(jumlah * bahan.jumlah)
			elif sub_status == "delete":
				bahan.stok = bahan.stok + (transaksi.jumlah * bahan.jumlah)
			bahan.save()
	if status == "out":
		bahan = Formula.objects.get(pk=transaksi.item_id)
		if sub_status == "tambah":
			bahan.stok = bahan.stok + (jumlah * bahan.netto)
		elif sub_status == "edit":
			bahan.stok = (bahan.stok - (transaksi.jumlah * bahan.netto)) + (jumlah * bahan.netto)
		else:
			bahan.stok = bahan.stok - (transaksi.jumlah * bahan.netto)
		bahan.save()