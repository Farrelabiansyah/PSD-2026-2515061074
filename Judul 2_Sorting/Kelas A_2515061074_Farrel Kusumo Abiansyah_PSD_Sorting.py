def bubble_sort(harga):
    n = len(harga)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            
            # Bandingkan harga
            if harga[j] > harga[j + 1]:
                # Tukar posisi
                harga[j], harga[j + 1] = harga[j + 1], harga[j]
    
    return harga


# Data harga barang
harga_barang = [15000, 5000, 12000, 8000, 20000]

# Proses sorting
hasil = bubble_sort(harga_barang)

# Output
print("Harga setelah diurutkan:", hasil)