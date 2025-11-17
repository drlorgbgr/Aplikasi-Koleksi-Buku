from database import buku_list, save_data, urutkan_id
# Fungsi untuk mengelola koleksi buku
# Tambah buku baru

def tambah_buku():
    
    judul = input("Judul buku: ")
    penulis = input("Penulis: ")
    tahun = int(input("Tahun terbit: "))
    kategori = input("Kategori: ")

    id = 1
    if len(buku_list) == 0:
        id = 1
    else:
        id = buku_list[-1]["id"] + 1

    buku = {
        "id": id,
        "judul": judul,
        "penulis": penulis,
        "tahun": tahun,
        "kategori": kategori
    }

    buku_list.append(buku)

    save_data()
    print("\nBuku berhasil ditambahkan!\n")

# Tampilkan semua buku
def tampilkan_semua():
    if len(buku_list) == 0:
        print("\nBelum ada buku.\n")
        return

    print("\n===== DAFTAR BUKU =====")
    for i in buku_list:
        print(f"[{i['id']}] {i['judul']} - {i['penulis']} ({i['tahun']}) | {i['kategori']}")
    
    print()

# Update data buku
def update_buku():
    id_buku = int(input("Masukkan ID buku: "))

    for i in buku_list:
        if i["id"] == id_buku:
            print("Masukkan data baru (kosongkan jika tidak mengubah):")

            judul = input("Judul baru: ")
            if judul != "":
                i["judul"] = judul

            penulis = input("Penulis baru: ")
            if penulis != "":
                i["penulis"] = penulis

            tahun = input("Tahun baru: ")
            if tahun != "":
                i["tahun"] = int(tahun)

            kategori = input("Kategori baru: ")
            if kategori != "":
                i["kategori"] = kategori
            save_data()
            print("\nBuku berhasil diperbarui!\n")
            return
    
    print("\nID buku tidak ditemukan.\n")

# Hapus buku
def hapus_buku():
    id_buku = int(input("Masukkan ID buku: "))

    for i in buku_list:
        if i["id"] == id_buku:
            buku_list.remove(i)
            urutkan_id()
            save_data()
            print("\nBuku berhasil dihapus!\n")
            return

    print("\nID buku tidak ditemukan.\n")