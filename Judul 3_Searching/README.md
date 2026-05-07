Judul : Implementasi metode seaching sequential search pada pencarian data barang

Deskrpisi singkat : 
Program tersebut merupakan implementasi metode Sequential Search dalam kehidupan sehari-hari, yaitu mencari nama barang pada daftar belanja. Program bekerja dengan cara memeriksa setiap data secara berurutan dari awal hingga akhir list sampai barang yang dicari ditemukan. Jika data ditemukan, program akan menampilkan posisi indeks barang tersebut, sedangkan jika tidak ditemukan maka program akan memberikan informasi bahwa barang tidak ada di dalam daftar.

Source Code :
<img width="467" height="37" alt="Cuplikan layar 2026-05-07 190643" src="https://github.com/user-attachments/assets/0e76b399-761f-412e-8e96-19a7acba19e9" />
Mendefinisikan fungsi bernama sequential_search
barang = list data yang akan dicari
target = data yang ingin ditemukan
<img width="366" height="33" alt="Cuplikan layar 2026-05-07 190702" src="https://github.com/user-attachments/assets/0dde8f0f-e467-4c81-adb7-0c4b05236137" />
Melakukan perulangan dari indeks pertama sampai terakhir
len(barang) digunakan untuk menghitung jumlah data
<img width="295" height="69" alt="Cuplikan layar 2026-05-07 190757" src="https://github.com/user-attachments/assets/6226e140-252f-4614-9a9b-ef07275c00bc" />
Membandingkan data pada indeks ke-i dengan data yang dicari
Mengembalikan indeks tempat data ditemukan
<img width="147" height="25" alt="Cuplikan layar 2026-05-07 190803" src="https://github.com/user-attachments/assets/1aecb853-a5d8-4b9b-a02f-3600e1bc2f02" />
Mengembalikan nilai -1 jika data tidak ada dalam list
<img width="739" height="236" alt="Cuplikan layar 2026-05-07 190821" src="https://github.com/user-attachments/assets/20aea054-5778-4bed-be47-d48835852505" />
Membuat list berisi nama barang belanja
Menyimpan data target pencarian ke variabel cari
Memanggil fungsi sequential_search()
Hasil pencarian disimpan ke variabel hasil
<img width="742" height="116" alt="Cuplikan layar 2026-05-07 190835" src="https://github.com/user-attachments/assets/d7033015-16f7-4751-9db7-0e4230dddfc2" />
Mengecek apakah data ditemukan
Menampilkan pesan jika barang ditemukan
Menampilkan pesan jika data tidak ditemukan

Output Program : 
<img width="475" height="23" alt="Cuplikan layar 2026-05-07 190909" src="https://github.com/user-attachments/assets/d0938ddd-0176-47b8-b10a-d2813139c0ae" />

Link Youtube : https://youtu.be/9qn515nWJj0?si=gDLg7UDOzIDIH_92
