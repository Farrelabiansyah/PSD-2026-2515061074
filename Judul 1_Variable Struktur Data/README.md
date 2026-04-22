Judul : Program Implementasi Struktur Data Singly Linked List pada Sistem Sederhana Antrian Kasir

Deskripsi Singkat :
Program yang dibuat merupakan implementasi struktur data Singly Linked List dalam bentuk simulasi antrian pelanggan di kasir menggunakan Python. Setiap pelanggan direpresentasikan sebagai node yang menyimpan data nama dan pointer ke node berikutnya, sehingga membentuk rangkaian data yang saling terhubung. Kelas AntrianKasir digunakan untuk mengelola antrian dengan operasi utama seperti menambah pelanggan ke bagian belakang (enqueue), melayani pelanggan dari bagian depan (dequeue), serta menampilkan seluruh isi antrian. Mekanisme ini mencerminkan sistem antrian di kehidupan nyata, di mana pelanggan yang datang lebih dulu akan dilayani terlebih dahulu, sekaligus menunjukkan keunggulan linked list dalam pengelolaan data yang dinamis dan efisien.

Source Code : 
<img width="347" height="80" alt="CLASS NODE TA 1" src="https://github.com/user-attachments/assets/7600de56-c56a-4490-a98e-c3435935e607" />
Membuat class Node
Node = representasi 1 pelanggan
Constructor dengan parameter nama
Digunakan untuk menyimpan nama pelanggan
Menyimpan data pelanggan ke dalam node
Pointer(next) ke node selanjutnya
Default = None (belum terhubung)
Logika:
Setiap pelanggan = 1 node
Node saling terhubung melalui next
Bentuknya seperti rantai:
<img width="254" height="67" alt="ANTRIAN KASIR TA 1" src="https://github.com/user-attachments/assets/746cd198-5f19-4958-9c7e-5302d1e8d450" />
Membuat sebuah class bernama AntrianKasir
Class ini berfungsi sebagai pengelola seluruh antrian (linked list).
Constructor (fungsi otomatis saat objek dibuat)
Digunakan untuk inisialisasi awal.
head adalah penunjuk ke node pertama
None berarti antrian masih kosong (belum ada pelanggan)
Logika:
Saat program mulai → antrian kosong
head akan berubah saat ada pelanggan pertama masuk
<img width="287" height="222" alt="MENAMBAH PELANGGAN KE ANTRIAN   JIKA ANTRIAN KOSONG   TELUSURI SAMPAI NODE TERAKHIR TA 1" src="https://github.com/user-attachments/assets/8c780fe5-74c1-4b08-8933-a9cbb40833f8" />
Fungsi untuk menambahkan pelanggan ke antrian
new(node) Membuat node baru berisi nama pelanggan
Kondisi 1 jika antrian kosong
Mengecek apakah antrian masih kosong
Jika kosong → node baru jadi head (pelanggan pertama)
Kondisi 2 jika antrian sudah terisi
Masuk ke kondisi jika sudah ada pelanggan
Mulai dari node pertama (head)
while.current(next) Selama masih ada node berikutnya → lanjut jalan
current.next Geser ke node berikutnya
Logika:
Program berjalan dari depan ke belakang
Sampai menemukan node terakhir (next = None)
Menambahkan di akhir
current.next = new_node
Node terakhir dihubungkan ke node baru
Logika utama dari fungsi pada gambar ketiga adalah menambahkan pelanggan ke dalam antrian secara berurutan dari belakang.
<img width="219" height="223" alt="PROGRAM UTAMA TA 1" src="https://github.com/user-attachments/assets/16240e12-d747-44bb-9371-f39026acfca1" />
antrian = AntrianKasir()
Baris ini membuat (instansiasi) objek baru bernama antrian. Di dalam memori, program menyiapkan sebuah struktur data (biasanya berupa List atau Queue) yang masih kosong untuk menampung nama-nama pelanggan.
Penambahan Pelanggan (Enqueue)
Pada tahap ini, program memasukkan data ke dalam antrean. Karena ini adalah sistem antrean (Queue), maka berlaku prinsip FIFO (First In, First Out).
antrian.tambah_pelanggan("Farrel"): Farrel masuk ke antrean (urutan ke-1).
antrian.tambah_pelanggan("Yanto"): Yanto masuk ke antrean (urutan ke-2).
antrian.tambah_pelanggan("Suharman"): Suharman masuk ke antrean (urutan ke-3).
Menampilkan Status Antrean Pertama
antrian.tampilkan_antrian()
Program akan mencetak daftar nama yang ada saat ini.
Pelayanan Pelanggan Kedua
antrian.layani_pelanggan()
Sekarang, Yanto berada di posisi paling depan. Program memproses Yanto dan menghapusnya dari daftar.
antrian.tampilkan_antrian()
Menampilkan sisa antrean terakhir.
Logika : Secara keseluruhan, program ini bekerja dengan prinsip FIFO (First In, First Out), yang berarti pelanggan yang pertama kali masuk ke dalam antrean akan menjadi orang pertama yang mendapatkan giliran untuk dilayani.

Output Program : 
<img width="162" height="182" alt="OUTPUT PROGRAM FIX TA 1" src="https://github.com/user-attachments/assets/1d59dabb-58da-48c4-8be7-3d6f54dc5322" />
1. Tahap Pengisian Antrean (Enqueue)
Tiga baris pertama menunjukkan proses masuknya data ke dalam sistem. Program mencetak konfirmasi setiap kali pelanggan ditambahkan. Urutannya adalah Farrel masuk terlebih dahulu, diikuti oleh Yanto, dan terakhir Suharman. Ini membangun daftar antrean awal yang lengkap.
2. Status Antrean Awal
Bagian "Daftar Antrean" pertama menampilkan seluruh elemen yang ada di dalam struktur data. Karena menggunakan prinsip FIFO (First In, First Out), Farrel berada di posisi paling atas (paling depan), sementara Suharman berada di posisi paling bawah (paling belakang).
3. Pemrosesan Pelanggan Pertama
Pesan "Farrel sedang dilayani" menandakan bahwa fungsi untuk melayani pelanggan telah dijalankan. Program secara otomatis mengambil data dari urutan terdepan (Farrel) dan mengeluarkannya dari sistem. Hal ini terbukti pada blok "Daftar Antrean" berikutnya, di mana nama Farrel sudah hilang, meninggalkan Yanto di posisi terdepan dan Suharman setelahnya.
4. Pemrosesan Pelanggan Kedua
Selanjutnya, program menjalankan perintah pelayanan kembali. Kali ini pesan muncul "Yanto sedang dilayani", karena setelah Farrel keluar, Yanto-lah yang menempati posisi terdepan. Setelah proses ini selesai, daftar antrean diperbarui lagi dan menunjukkan bahwa hanya tersisa Suharman di dalam daftar.
Secara teknis, output ini membuktikan bahwa program berhasil mensimulasikan struktur data Queue, di mana setiap elemen diproses sesuai urutan kedatangannya tanpa ada data yang terlewat atau tertukar urutannya.

Link YouTube : 
https://youtu.be/DDVoNiymd_c
