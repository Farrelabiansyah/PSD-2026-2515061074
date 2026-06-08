Judul : Implementasi Hash Map Separate Chaining pada Sistem Data Buku Perpustakaan Menggunakan Python

Deskripsi Singkat :
Program ini merupakan implementasi struktur data Hash Map Separate Chaining dalam kehidupan sehari-hari dengan studi kasus pengelolaan data buku perpustakaan. Setiap buku disimpan menggunakan kode buku sebagai key dan judul buku sebagai value. Program menggunakan fungsi hash untuk menentukan lokasi penyimpanan data pada hash table. Jika terjadi collision atau tabrakan data pada index yang sama, maka data akan disimpan menggunakan metode Separate Chaining berupa linked list. Program ini memiliki fitur menambahkan, mencari, menghapus, dan menampilkan data buku sehingga pengelolaan data menjadi lebih cepat dan terstruktur.

Source Code : 
<img width="179" height="65" alt="Cuplikan layar 2026-06-08 155524" src="https://github.com/user-attachments/assets/e16884ca-47d8-4b37-a6e0-0d651479ec43" />
Pada bagian ini program membuat class Node yang digunakan sebagai tempat penyimpanan data pada linked list. Setiap node menyimpan key sebagai kode buku dan value sebagai judul buku. Variabel next digunakan untuk menghubungkan node satu ke node lainnya jika terjadi collision pada hash map. Nilai awal None menandakan node belum terhubung ke data lain.
<img width="283" height="92" alt="Cuplikan layar 2026-06-08 155543" src="https://github.com/user-attachments/assets/b18aeb54-6667-4d34-97c5-b1535f79bea3" />
Bagian ini membuat class utama HashMapSeparateChaining. Constructor __init__() digunakan untuk menentukan ukuran hash table dengan default 10 slot. Variabel table dibuat menggunakan list yang berisi None, artinya semua slot masih kosong. Fungsi ini digunakan untuk menentukan index penyimpanan data berdasarkan key atau kode buku. Program memakai operasi modulus (%) agar hasil hash tetap berada dalam batas ukuran tabel.
<img width="305" height="200" alt="Cuplikan layar 2026-06-08 155551" src="https://github.com/user-attachments/assets/7f5b8616-71b4-4d18-87f1-424122c70c67" />
Fungsi insert() digunakan untuk menambahkan data buku ke dalam hash map. Program terlebih dahulu menentukan posisi index menggunakan fungsi hash berdasarkan key atau kode buku. Setelah itu, program memeriksa apakah pada index tersebut sudah ada data.
Jika kode buku yang dimasukkan sudah tersedia, maka judul buku akan diperbarui tanpa membuat data baru. Namun jika belum ada, program akan membuat node baru lalu menyimpannya ke dalam linked list pada index tersebut.
<img width="208" height="129" alt="Cuplikan layar 2026-06-08 155558" src="https://github.com/user-attachments/assets/4b7f074f-5de9-4441-809f-ddaa2396a51d" />
Fungsi search() digunakan untuk mencari data buku berdasarkan kode buku (key). Program akan mencari index menggunakan hash function, lalu menelusuri linked list pada index tersebut. Jika kode buku ditemukan, maka program akan mengembalikan data buku tersebut. Namun jika data tidak ditemukan sampai akhir linked list, program akan mengembalikan nilai None.
<img width="278" height="249" alt="Cuplikan layar 2026-06-08 155606" src="https://github.com/user-attachments/assets/7a899d3d-4641-4df3-9b97-ee44343e6dee" />
Fungsi remove_key() digunakan untuk menghapus data buku berdasarkan kode buku. Program akan mencari posisi data terlebih dahulu menggunakan hash function, kemudian menelusuri linked list pada index tersebut. Jika data ditemukan, program akan menghapus node tersebut dari linked list. Jika node berada di awal linked list maka head akan dipindahkan ke node berikutnya, sedangkan jika node berada di tengah atau akhir maka hubungan node sebelumnya akan diarahkan ke node setelahnya. Jika data tidak ditemukan, program akan menampilkan pesan bahwa kode buku tidak ditemukan.
<img width="344" height="155" alt="Cuplikan layar 2026-06-08 155612" src="https://github.com/user-attachments/assets/195e315c-78bf-49f4-8820-526dcde11006" />
Fungsi display() digunakan untuk menampilkan seluruh isi data pada hash table. Program akan melakukan perulangan untuk mengecek semua index yang ada pada hash table. Jika pada suatu index terdapat data, program akan menampilkan seluruh node yang tersimpan secara berantai menggunakan linked list. Apabila tidak ada data, maka index tersebut akan langsung menampilkan NULL.
<img width="278" height="158" alt="Cuplikan layar 2026-06-08 155652" src="https://github.com/user-attachments/assets/4be78576-5a05-43af-be1b-cb4570745e7e" />
Fungsi main() merupakan fungsi utama program yang digunakan untuk menjalankan menu sistem perpustakaan. Program membuat objek HashMapSeparateChaining() sebagai tempat penyimpanan data buku. Selanjutnya program menggunakan perulangan while True agar menu terus berjalan sampai pengguna memilih keluar. Pada bagian ini pengguna dapat memilih menu seperti menambah buku, mencari buku, menghapus buku, melihat seluruh data buku, atau keluar dari program.
<img width="352" height="380" alt="Cuplikan layar 2026-06-08 155702" src="https://github.com/user-attachments/assets/b2e74f7a-e3d5-48cc-8f6d-15b8cdc020e9" />
Jika pengguna memilih menu 1, program akan meminta input kode buku dan judul buku, lalu menyimpan data menggunakan fungsi insert().
Jika memilih menu 2, program akan menjalankan fungsi search() untuk mencari data buku berdasarkan kode buku.
Jika memilih menu 3, program menjalankan fungsi remove_key() untuk menghapus data buku.
Jika memilih menu 4, program akan menampilkan seluruh data buku menggunakan fungsi display().
Jika memilih menu 5, program akan berhenti dan menampilkan pesan bahwa program selesai dijalankan.

Output Program : 
<img width="222" height="422" alt="OUT DUA" src="https://github.com/user-attachments/assets/4e3635cd-802f-48d3-aa13-1e7ab02d84a3" />
<img width="283" height="237" alt="OUT SATU" src="https://github.com/user-attachments/assets/c3ba5e34-b806-4649-a643-ba9995e9e635" />

Link Youtube : 
