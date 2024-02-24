#data stok gudang sumbiri 

from tabulate import tabulate
from collections import defaultdict

ListProduk = [
    {'no': '100', 'nama': 'benang', 'harga': '1200000', 'stock': '71'},
    {'no': '340', 'nama': 'kain', 'harga': '1500000', 'stock': '45'},
    {'no': '333', 'nama': 'kancing', 'harga': '800000', 'stock': '15'},
    {'no': '360', 'nama': 'karet', 'harga': '500000', 'stock': '20'}
]

ListLaporan = []

def main_menu():
    while True:
        menu_utama = input('''
    ---------------------------------------------------
                       SELAMAT DATANG
                DI SISTEM GUDANG SUMBIRI
    ---------------------------------------------------
    Pilih menu berikut ini :
    1. Lihat Daftar Barang        4. Hapus Data Barang
    2. Tambah Barang              5. Filter dan Sort Barang 
    3. Update Data Barang         6. Tambah Laporan       
    0. Keluar
    ---------------------------------------------------
    Ketik angka menu : ''')
        
        if menu_utama == '1':
            daftar_barang()
        elif menu_utama == '2':
            tambah_stock()
        elif menu_utama == '3':
            update_produk()
        elif menu_utama == '4':
            hapus_produk()
        elif menu_utama == '5':
            filter_sort_menu()
        elif menu_utama == '6':
            tambah_laporan()
        elif menu_utama == '0':
            print('''\n
    ----------------------
         Terima Kasih
         Sampai Jumpa
    ----------------------''')
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def daftar_barang():
    while True:
        menu_daftar_barang = input('''\n
    -------------------------
       LIHAT DAFTAR BARANG
    -------------------------
    Pilih menu berikut ini :
    1. Daftar seluruh Barang
    2. Lihat barang tertentu
    0. Kembali ke menu utama
    -------------------------
    Ketik angka menu: ''')
        if menu_daftar_barang == '1':
            daftar_barang_semua()
        elif menu_daftar_barang == '2':
            daftar_barang_tertentu()
        elif menu_daftar_barang == '0':
            break
        else:
            input_salah()

def daftar_barang_semua():
    print('''\n
    ---------------------------------------------------------
                         DAFTAR BARANG
    ---------------------------------------------------------
    ''')
    if not ListProduk:
        tidak_ada_data()
    else:
        headers = ["Kode", "Nama Barang", "Harga", "Stock"]
        table_data = [[prod["no"], prod["nama"], f'Rp {prod["harga"]}', prod["stock"]] for prod in ListProduk]
        table = tabulate(table_data, headers=headers, tablefmt="fancy_grid")
        print(table)

def daftar_barang_tertentu():
    print('''\n
    ------------------
    DAFTAR NAMA BARANG
    ------------------
    Kode|Nama Barang''')
    for i in range(len(ListProduk)):
        print('     {}  |{}'.format(ListProduk[i]['no'], ListProduk[i]['nama']))
    print('    ------------------')

    InputBarang = input_no_Barang()
    PilihBarang = filter_data(InputBarang)
    if not PilihBarang:
        tidak_ada_data()
    else:
        info_Barang(PilihBarang)

def tambah_stock():
    while True:
        menu_tambah_stock = input('''\n
    ------------------------
       TAMBAH DATA BARANG
    ------------------------
    Pilih menu berikut ini :
    1. Tambah data barang
    0. Kembali ke menu utama
    ------------------------
    Ketik angka menu: ''')
        if menu_tambah_stock == '1':
            tambah_stock_barang()
        elif menu_tambah_stock == '0':
            break
        else:
            input_salah()

def tambah_stock_barang():
    InputBarang = input_no_Barang()
    PilihBarang = filter_data(InputBarang)
    InputNamaBarang = input_nama_Barang()
    FilterNamabarang = filter_nama_barang(InputNamaBarang)

    if PilihBarang:
        print('\n    ----Data Sudah Ada----')
    elif FilterNamabarang:
        print('\n    ----Data Sudah Ada----')
    else:
        while True:
            try:
                HargaBarang = int(input('    Masukkan harga barang (hanya angka): '))
                break
            except:
                input_salah(); print()
        while True:
            try:
                StockBarang = int(input('    Masukkan stock barang (hanya angka): '))
                break
            except:
                input_salah();print()
        while True:
            Inputkonfirmasi = input('    Apakah data akan disimpan? (Y/N): ').lower()
            if Inputkonfirmasi == 'y':
                ListProduk.append(
                    {'no': InputBarang,
                     'nama': InputNamaBarang,
                     'harga': HargaBarang,
                     'stock': StockBarang})
                print('\n    ----Data Tersimpan----')
                break
            elif Inputkonfirmasi == 'n':
                print('\n    ----Data tidak tersimpan----')
                break
            else:
                input_salah()

def update_produk():
    while True:
        menu_update_produk = input('''\n
    ------------------------
       UPDATE DATA BARANG
    ------------------------
    Pilih menu berikut ini :
    1. Update data barang
    0. Kembali ke menu utama
    ------------------------
    Ketik angka menu: ''')
        if menu_update_produk == '1':
            update_produk_barang()
        elif menu_update_produk == '0':
            break
        else:
            input_salah()

def update_produk_barang():
    daftar_barang_semua()
    InputBarang = input_no_Barang()
    PilihBarang = filter_data(InputBarang)

    if not PilihBarang:
        tidak_ada_data()
    else:
        info_Barang(PilihBarang)
        ProdukIndex = -1
        for i in PilihBarang:
            ProdukIndex = ListProduk.index(i)

        while True:
            InputKonfirmasi = input('\n    Apakah data akan diubah? (Y/N): ').lower()
            if InputKonfirmasi == 'y':
                while True:
                    InputUpdateProduk = input('    Tulis bagian yang akan diubah (stock/harga): ').lower()
                    if InputUpdateProduk == 'stock' or InputUpdateProduk == 'harga':
                        break
                    else:
                        input_salah()
                BagianUpdate = any(InputUpdateProduk in i for i in ListProduk)
                if BagianUpdate:
                    InputDataBaru = input('    Masukkan {} baru:'.format(InputUpdateProduk.lower()))
                    while True:
                        KonfirmasiUpdate = input('    Anda yakin ingin diubah? (Y/N): ').lower()
                        if KonfirmasiUpdate == 'y':
                            ListProduk[ProdukIndex][InputUpdateProduk] = InputDataBaru
                            print('\n    ----Data Berhasil Diubah----')
                            break
                        elif KonfirmasiUpdate == 'n':
                            print('\n    ----Data Tidak Berubah----')
                            break
                        else:
                            input_salah()
                else:
                    input_salah()
                break
            elif InputKonfirmasi == 'n':
                break
            else:
                input_salah()

def hapus_produk():
    while True:
        menu_hapus_barang = input('''\n
    ------------------------
        HAPUS DATA BARANG
    ------------------------
    Pilih menu berikut ini :
    1. Hapus Produk
    0. Kembali ke menu utama
    ------------------------
    Ketik angka menu: ''')

        if menu_hapus_barang == '1':
            hapus_produk_barang() 
        elif menu_hapus_barang == '0':
            break
        else:
            input_salah()

def hapus_produk_barang():
    daftar_barang_semua()
    InputBarang = input_no_Barang()
    PilihBarang = filter_data(InputBarang)

    if not PilihBarang:
        tidak_ada_data()
    else:
        info_Barang(PilihBarang)
        while True:
            KonfirmasiUpdate = input('    Anda yakin ingin dihapus? (Y/N): ').lower()
            if KonfirmasiUpdate == 'y':
                del ListProduk[next((index for (index, d) in enumerate(ListProduk) if d['no'] == InputBarang), None)]
                print('\n    ----Data berhasil dihapus----')
                break
            elif KonfirmasiUpdate == 'n':
                print('\n    ----Data Tidak Terhapus----')
                break
            else:
                input_salah()

def input_salah():
    print('\n    ----Maaf inputan anda salah----')

def filter_data(InputBarang):
    return list(filter(lambda x: x.get('no') == InputBarang, ListProduk))

def filter_nama_barang(InputBarang):
    return list(filter(lambda x: x.get('nama') == InputBarang, ListProduk))

def tidak_ada_data():
    print('\n    ----Data yang anda cari tidak ditemukan----')

def input_no_Barang():
    return input('    Masukkan kode Barang: ')

def input_nama_Barang():
    return input('    Masukkan nama Barang: ').lower()

def info_Barang(Pilihnamabarang):
    print('''
    -----------------
       Info barang
    -----------------''')
    for i in Pilihnamabarang:
        print('    No    : {}\n    Nama  : {}\n    Harga : {}\n    stock : {}'.format(i['no'], i['nama'], i['harga'], i['stock']))

def tambah_laporan():
    jenis_laporan = input('''\n
    --------------------------------
          TAMBAH LAPORAN
    --------------------------------
    Pilih jenis laporan:
    1. Pembelian
    2. Stok Masuk
    0. Kembali ke menu utama
    --------------------------------
    Ketik angka menu: ''')
    
    if jenis_laporan == '1':
        tambah_laporan_pembelian()
    elif jenis_laporan == '2':
        tambah_laporan_stok_masuk()
    elif jenis_laporan == '0':
        pass
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

def tambah_laporan_pembelian():
    tanggal = input("Masukkan tanggal pembelian (YYYY-MM-DD): ")
    nama_barang = input_nama_Barang()
    jumlah = int(input("Masukkan jumlah pembelian: "))
    deskripsi = f"Pembelian {nama_barang} sebanyak {jumlah}"
    ListLaporan.append({'tanggal': tanggal, 'jenis': 'Pembelian', 'deskripsi': deskripsi})
    print("\nLaporan pembelian berhasil ditambahkan.")

def tambah_laporan_stok_masuk():
    tanggal = input("Masukkan tanggal stok masuk (YYYY-MM-DD): ")
    nama_barang = input_nama_Barang()
    jumlah = int(input("Masukkan jumlah stok masuk: "))
    deskripsi = f"Stok Masuk {nama_barang} sebanyak {jumlah}"
    ListLaporan.append({'tanggal': tanggal, 'jenis': 'Stok Masuk', 'deskripsi': deskripsi})
    print("\nLaporan stok masuk berhasil ditambahkan.")

def filter_sort_menu():
    nama_barang = input("Masukkan nama Barang yang ingin difilter: ")
    filtered_produk = [produk for produk in ListProduk if produk['nama'].lower() == nama_barang.lower()]
    if filtered_produk:
        headers = ["Kode", "Nama Barang", "Harga", "Stock"]
        table_data = [[prod["no"], prod["nama"], f'Rp {prod["harga"]}', prod["stock"]] for prod in filtered_produk]
        table = tabulate(table_data, headers=headers, tablefmt="fancy_grid")
        print(table)
    else:
        print("Barang tidak ditemukan.")

main_menu()
