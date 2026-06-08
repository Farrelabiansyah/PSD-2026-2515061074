class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMapSeparateChaining:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [None] * self.SIZE

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        index = self.hash_function(key)
        current = self.table[index]

        while current is not None:
            if current.key == key:
                current.value = value
                print("Kode buku sudah ada, data diperbarui!")
                return
            current = current.next

        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node

        print(f"Buku '{value}' berhasil ditambahkan")

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]

        while current is not None:
            if current.key == key:
                return current
            current = current.next

        return None

    def remove_key(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None

        while current is not None:
            if current.key == key:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next

                print("Buku berhasil dihapus")
                return True

            prev = current
            current = current.next

        print("Kode buku tidak ditemukan")
        return False

    def display(self):
        print("\nDaftar Buku Perpustakaan:")
        for i in range(self.SIZE):
            print(f"{i}: ", end="")
            current = self.table[i]

            while current is not None:
                print(f"({current.key}, {current.value}) -> ", end="")
                current = current.next

            print("NULL")


def main():
    perpustakaan = HashMapSeparateChaining()

    while True:
        print("\n=== HASH MAP SEPARATE CHAINING ===")
        print("1. Tambah Buku")
        print("2. Cari Buku")
        print("3. Hapus Buku")
        print("4. Lihat Semua Buku")
        print("5. Keluar")

        pilih = input("Pilih: ")

        if pilih == "1":
            key = int(input("Masukkan kode buku: "))
            value = input("Masukkan judul buku: ")
            perpustakaan.insert(key, value)

        elif pilih == "2":
            key = int(input("Cari kode buku: "))
            hasil = perpustakaan.search(key)

            if hasil is not None:
                print(f"Buku ditemukan: {hasil.value}")
            else:
                print("Buku tidak ditemukan")

        elif pilih == "3":
            key = int(input("Masukkan kode buku yang ingin dihapus: "))
            perpustakaan.remove_key(key)

        elif pilih == "4":
            perpustakaan.display()

        elif pilih == "5":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()