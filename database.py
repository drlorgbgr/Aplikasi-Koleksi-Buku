# Data disimpan di list
buku_list = []

def load_data():
    file = open("data_buku.txt", "r")
    lines = file.readlines()
    file.close()

    buku_list.clear()

    for line in lines:
        split = line.strip().split("|")
        buku = {
            "id": int(split[0]),
            "judul": split[1],
            "penulis": split[2],
            "tahun": int(split[3]),
            "kategori": split[4]
        }
        buku_list.append(buku)

def urutkan_id():
    buku_list.sort(key=lambda x: x['id'])
    
    id = 1
    for i in buku_list:
        i['id'] = id
        id += 1
    
def save_data():
    file = open("data_buku.txt", "w")
    for b in buku_list:
        baris = f"{b['id']}|{b['judul']}|{b['penulis']}|{b['tahun']}|{b['kategori']}\n"
        file.write(baris)
    file.close()