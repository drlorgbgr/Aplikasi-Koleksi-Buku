from database import buku_list

def cari_buku():
    keyword = input("Masukkan judul/penulis yang dicari: ").lower()
    ditemukan = False

    print("\n===== HASIL PENCARIAN =====")
    for i in buku_list:
        if keyword in i["judul"].lower() or keyword in i["penulis"].lower():
            print(f"[{i['id']}] {i['judul']} - {i['penulis']}")
            ditemukan = True

    if ditemukan == False:
        print("Tidak ditemukan.")

    print()