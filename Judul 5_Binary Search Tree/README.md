Judul : Implementasi BST pada Nomor Kursi Bioskop

Deskripsi Singkat : Program ini merupakan implementasi Binary Search Tree (BST) dalam kehidupan sehari-hari dengan studi kasus nomor kursi bioskop. Program digunakan untuk menyimpan, mencari, dan menampilkan nomor kursi secara terurut. Nomor kursi yang lebih kecil disimpan di sisi kiri node, sedangkan nomor yang lebih besar disimpan di sisi kanan, sehingga proses pencarian kursi menjadi lebih cepat dan terstruktur dibanding mencari satu per satu.

Source Code :
<img width="194" height="77" alt="Cuplikan layar 2026-05-19 105025" src="https://github.com/user-attachments/assets/6b9af925-f7d2-4db2-aca9-f1af0c223328" />
Bagian ini digunakan untuk membuat node pada Binary Search Tree (BST). Setiap node akan menyimpan satu data berupa nomor kursi bioskop. Variabel kursi digunakan untuk menyimpan nomor kursi, sedangkan left dan right berfungsi sebagai cabang kiri dan kanan BST. Nilai awal None menandakan bahwa node belum memiliki anak.
<img width="177" height="50" alt="Cuplikan layar 2026-05-19 105039" src="https://github.com/user-attachments/assets/09c7f045-7222-4ad0-b1da-43c7fac3f6c3" />
Class BSTBioskop berfungsi sebagai pengelola seluruh operasi BST. Pada bagian constructor, dibuat variabel root yang berfungsi sebagai akar (node utama) dari BST. Nilai awal None berarti pohon masih kosong dan belum memiliki data kursi.
<img width="347" height="226" alt="Cuplikan layar 2026-05-19 105054" src="https://github.com/user-attachments/assets/acce3b0e-0d34-4fd2-819a-5bc817c9e3ab" />
Fungsi ini digunakan untuk menambahkan nomor kursi ke dalam BST. Program pertama-tama mengecek apakah posisi node masih kosong (root is None). Jika kosong, maka dibuat node baru. Namun jika sudah ada data, program akan membandingkan nilai kursi dengan node saat ini. Jika nomor kursi lebih kecil, data akan masuk ke cabang kiri, sedangkan jika lebih besar akan masuk ke cabang kanan. Konsep ini adalah inti dari BST, yaitu nilai kecil di kiri dan nilai besar di kanan.
<img width="308" height="232" alt="Cuplikan layar 2026-05-19 105105" src="https://github.com/user-attachments/assets/4ef7e9bd-09be-4118-9e83-084e116d9262" />
Fungsi ini digunakan untuk mencari nomor kursi dalam BST. Program akan mengecek apakah node kosong, jika kosong berarti kursi tidak ditemukan. Jika nomor kursi sama dengan node saat ini, maka pencarian berhasil. Jika nomor kursi lebih kecil, pencarian dilakukan ke subtree kiri, sedangkan jika lebih besar akan dilanjutkan ke subtree kanan. Dengan metode ini, proses pencarian menjadi lebih cepat dibanding mengecek satu per satu data. Dan def search digunakan untuk memanggil proses pencarian mulai dari root BST.
<img width="224" height="95" alt="Cuplikan layar 2026-05-19 105116" src="https://github.com/user-attachments/assets/d33aba31-bb0e-4bfb-aafc-3d546e295072" />
Fungsi inorder digunakan untuk menampilkan seluruh nomor kursi secara terurut dari kecil ke besar. Proses traversal dilakukan dengan mengunjungi subtree kiri terlebih dahulu, kemudian node utama, lalu subtree kanan. Karena aturan BST, hasil traversal inorder selalu menghasilkan data yang terurut.
Bagian ini merupakan fungsi utama program. Program membuat objek bst dari class BSTBioskop untuk menjalankan semua operasi BST. Perulangan while True digunakan agar menu program terus berjalan sampai pengguna memilih keluar. Bagian print digunakan untuk menampilkan menu pilihan kepada pengguna, seperti menambah kursi, mencari kursi, melihat semua kursi, atau keluar dari program. 
<img width="287" height="170" alt="Cuplikan layar 2026-05-19 105144" src="https://github.com/user-attachments/assets/3b080086-0aef-41bb-a47e-962d4a9c19f1" />
Bagian ini merupakan fungsi utama program. Program membuat objek bst dari class BSTBioskop untuk menjalankan semua operasi BST. Perulangan while True digunakan agar menu program terus berjalan sampai pengguna memilih keluar. Bagian print digunakan untuk menampilkan menu pilihan kepada pengguna, seperti menambah kursi, mencari kursi, melihat semua kursi, atau keluar dari program. 
<img width="302" height="348" alt="Cuplikan layar 2026-05-19 105157" src="https://github.com/user-attachments/assets/0c720c9e-324c-4960-bdc4-03fcea684a4b" />
Jika pengguna memilih menu 1, program akan meminta input nomor kursi dan menjalankan fungsi insert() untuk menambahkan kursi ke BST.
Jika memilih menu 2, program akan menjalankan fungsi search() untuk mencari nomor kursi.
Jika memilih menu 3, program menjalankan traversal inorder() untuk menampilkan seluruh kursi secara terurut.
Jika pengguna memilih menu 4, program akan berhenti.

Output Kode : 
<img width="196" height="433" alt="OUTPUT TA 5" src="https://github.com/user-attachments/assets/78fcdaeb-7c7f-4d38-bbad-eecbeaea595e" />

Link Youtube : https://youtu.be/OdUKiQjwGK4
