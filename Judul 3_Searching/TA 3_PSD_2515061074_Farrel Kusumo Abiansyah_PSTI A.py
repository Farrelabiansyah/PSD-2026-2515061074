# Fungsi Sequential Search
def sequential_search(barang, target):
    
    # Perulangan untuk mengecek setiap data
    for i in range(len(barang)):
        
        # Jika data ditemukan
        if barang[i] == target:
            return i  
    
    # Jika data tidak ditemukan
    return -1


# Daftar barang belanja
daftar_barang = ["Beras", "Minyak", "Gula", "Telur", "Susu"]

# Barang yang dicari
cari = "Telur"

# Memanggil fungsi searching
hasil = sequential_search(daftar_barang, cari)

# Menampilkan hasil
if hasil != -1:
    print(f"Barang '{cari}' ditemukan pada indeks ke-{hasil}")
else:
    print(f"Barang '{cari}' tidak ditemukan")