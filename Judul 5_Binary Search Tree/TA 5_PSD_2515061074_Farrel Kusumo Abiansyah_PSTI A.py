class Node:
    def __init__(self, kursi):
        self.kursi = kursi
        self.left = None
        self.right = None


class BSTBioskop:
    def __init__(self):
        self.root = None

    # Menambahkan nomor kursi
    def insert_node(self, root, kursi):
        if root is None:
            return Node(kursi)

        if kursi < root.kursi:
            root.left = self.insert_node(root.left, kursi)

        elif kursi > root.kursi:
            root.right = self.insert_node(root.right, kursi)

        return root

    def insert(self, kursi):
        self.root = self.insert_node(self.root, kursi)

    # Mencari nomor kursi
    def search_node(self, root, kursi):
        if root is None:
            return False

        if root.kursi == kursi:
            return True

        if kursi < root.kursi:
            return self.search_node(root.left, kursi)

        return self.search_node(root.right)

    def search(self, kursi):
        return self.search_node(self.root, kursi)

    # Menampilkan kursi secara urut
    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.kursi, end=" ")
            self.inorder(root.right)


def main():
    bst = BSTBioskop()

    while True:
        print("\n=== BST KURSI BIOSKOP ===")
        print("1. Tambah Nomor Kursi")
        print("2. Cari Nomor Kursi")
        print("3. Lihat Semua Kursi")
        print("4. Keluar")

        pilih = input("Pilih: ")

        if pilih == "1":
            kursi = int(input("Masukkan nomor kursi: "))
            bst.insert(kursi)
            print("Nomor kursi berhasil ditambahkan")

        elif pilih == "2":
            kursi = int(input("Cari nomor kursi: "))
            if bst.search(kursi):
                print("Nomor kursi ditemukan")
            else:
                print("Nomor kursi tidak ditemukan")

        elif pilih == "3":
            print("Daftar nomor kursi: ", end="")
            bst.inorder(bst.root)
            print()

        elif pilih == "4":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()