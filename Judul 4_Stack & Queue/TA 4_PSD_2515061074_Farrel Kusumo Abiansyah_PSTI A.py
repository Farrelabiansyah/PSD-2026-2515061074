class StackBuku:
    
    def __init__(self, max_size=100):
        self.MAX = max_size
        self.stack = [None] * self.MAX
        self.top = -1

    # Mengecek apakah stack kosong
    def is_empty(self):
        return self.top == -1

    # Mengecek apakah stack penuh
    def is_full(self):
        return self.top == self.MAX - 1

    # Menambahkan buku ke stack
    def push(self, buku):
        if self.is_full():
            print("Tumpukan Buku Penuh")
            return
        
        self.top += 1
        self.stack[self.top] = buku
        print(f"Buku '{buku}' berhasil ditambahkan ke tumpukan")

    # Mengambil buku paling atas
    def pop(self):
        if self.is_empty():
            print("Tumpukan Buku Kosong")
            return
        
        print(f"Buku '{self.stack[self.top]}' diambil dari tumpukan")
        self.top -= 1

    # Melihat buku paling atas
    def peek(self):
        if self.is_empty():
            print("Tumpukan Buku Kosong")
            return
        
        print(f"Buku paling atas adalah: {self.stack[self.top]}")

    # Menampilkan seluruh isi stack
    def display(self):
        if self.is_empty():
            print("Belum ada buku di tumpukan")
            return
        
        print("Daftar Buku (atas ke bawah): ", end="")
        
        for i in range(self.top, -1, -1):
            print(self.stack[i], end=" ")
        print()


def main():
    stack = StackBuku()
    pilih = 0

    while pilih != 5:
        print("\n=== STACK ARRAY BUKU ===")
        print("1. Tambah Buku")
        print("2. Ambil Buku")
        print("3. Lihat Buku Teratas")
        print("4. Lihat Semua Buku")
        print("5. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            buku = input("Masukkan nama buku: ")
            stack.push(buku)

        elif pilih == 2:
            stack.pop()

        elif pilih == 3:
            stack.peek()

        elif pilih == 4:
            stack.display()

        elif pilih == 5:
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()