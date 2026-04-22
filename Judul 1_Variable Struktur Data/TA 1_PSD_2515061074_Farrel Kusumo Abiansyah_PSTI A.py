# Membuat Node (setiap pelanggan)
class Node:
    def __init__(self, nama):
        self.nama = nama  # data pelanggan
        self.next = None  # pointer ke node berikutnya


# Membuat Singly Linked List
class AntrianKasir:
    def __init__(self):
        self.head = None  # awal antrian

    # Menambah pelanggan ke antrian (enqueue)
    def tambah_pelanggan(self, nama):
        new_node = Node(nama)
        
        # Jika antrian kosong
        if self.head is None:
            self.head = new_node
        else:
            # Telusuri sampai node terakhir
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        
        print(f"{nama} masuk ke antrian.")

    # Melayani pelanggan (dequeue)
    def layani_pelanggan(self):
        if self.head is None:
            print("Antrian kosong.")
        else:
            print(f"{self.head.nama} sedang dilayani.")
            self.head = self.head.next  # pindah ke node berikutnya

    # Menampilkan semua antrian
    def tampilkan_antrian(self):
        if self.head is None:
            print("Antrian kosong.")
        else:
            current = self.head
            print("Daftar Antrian:")
            while current:
                print(f"- {current.nama}")
                current = current.next


# Program utama
antrian = AntrianKasir()

# Simulasi kehidupan sehari-hari
antrian.tambah_pelanggan("Farrel")
antrian.tambah_pelanggan("Yanto")
antrian.tambah_pelanggan("Suharman")

antrian.tampilkan_antrian()

antrian.layani_pelanggan()
antrian.tampilkan_antrian()

antrian.layani_pelanggan()
antrian.tampilkan_antrian()