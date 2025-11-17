from koleksi import tambah_buku, tampilkan_semua, update_buku, hapus_buku   
from utils import cari_buku
from database import load_data

load_data()

def menu():
    while True:
        print("""
=========================================
        APLIKASI KOLEKSI BUKU
=========================================
1. Tambah Buku
2. Lihat Semua Buku
3. Cari Buku
4. Ubah Data Buku
5. Hapus Buku
0. Keluar
""")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_buku()
        elif pilihan == "2":
            tampilkan_semua()
        elif pilihan == "3":
            cari_buku()
        elif pilihan == "4":
            update_buku()
        elif pilihan == "5":
            hapus_buku()
        elif pilihan == "0":
            print("Keluar dari program...")
            break
        else:
            print("Pilihan tidak valid.\n")

menu()