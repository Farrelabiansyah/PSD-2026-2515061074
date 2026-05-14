Judul : Implementasi stack array pada tumpukan buku

Deskripsi Singkat :
Program tersebut merupakan implementasi struktur data Stack Array menggunakan bahasa Python dengan studi kasus tumpukan buku di meja belajar. Program menerapkan konsep LIFO (Last In First Out), yaitu buku yang terakhir dimasukkan ke dalam tumpukan akan menjadi buku pertama yang diambil. Data disimpan menggunakan array/list dengan beberapa operasi utama seperti push untuk menambahkan buku, pop untuk mengambil buku paling atas, peek untuk melihat buku teratas, dan display untuk menampilkan seluruh isi tumpukan buku.

Source Code : 
<img width="244" height="89" alt="1" src="https://github.com/user-attachments/assets/b6fbcd02-28e5-40c4-b965-44c8dafc1daa" />
Membuat class bernama StackBuku,
max_size=100 menentukan kapasitas maksimal stack,
Menyimpan kapasitas maksimal stack,
Membuat array/list kosong sebanyak kapasitas maksimal,
Penanda posisi data paling atas
-1 berarti stack masih kosong
<img width="227" height="57" alt="2" src="https://github.com/user-attachments/assets/40c4ae02-c01b-4e8e-babc-979785c89012" />
Mengecek apakah stack kosong
<img width="255" height="54" alt="3" src="https://github.com/user-attachments/assets/0d9651c1-fd61-42ce-8625-bb036ba6e8e9" />
Mengecek apakah stack sudah penuh
<img width="259" height="85" alt="4" src="https://github.com/user-attachments/assets/e5e54fe0-d649-423e-9fda-937afdb7ac0d" />
Fungsi untuk menambahkan buku ke stack,
Mengecek apakah stack penuh,
Menampilkan pesan jika stack penuh
<img width="360" height="59" alt="5" src="https://github.com/user-attachments/assets/fc513a93-b79e-441c-83be-d81448c1613a" />
Posisi top naik satu tingkat,
Menyimpan data buku ke posisi paling atas,
Menampilkan pesan bahwa buku berhasil ditambahkan
<img width="403" height="120" alt="6" src="https://github.com/user-attachments/assets/6b0a4c84-d8c7-4f25-8b56-40104627da37" />
Fungsi untuk mengambil buku paling atas,
Mengecek apakah stack kosong,
Menampilkan pesan jika tidak ada buku,
Menampilkan buku yang diambil,
Menghapus data teratas dengan menurunkan posisi top
<img width="395" height="121" alt="7" src="https://github.com/user-attachments/assets/662f7ff0-3945-4168-b7c2-5d1f90010453" />
Fungsi untuk melihat buku paling atas tanpa menghapusnya,
Menampilkan data pada posisi top
<img width="337" height="103" alt="8" src="https://github.com/user-attachments/assets/70ab94e6-d82f-4298-9524-26faa22b2b6f" />
Fungsi untuk menampilkan semua isi stack,
Perulangan dari atas ke bawah,
<img width="305" height="60" alt="9" src="https://github.com/user-attachments/assets/c4e2679a-6276-4e58-b668-06c8db821834" />
Perulangan dari atas ke bawah,
Menampilkan isi stack satu per satu
<img width="305" height="247" alt="10" src="https://github.com/user-attachments/assets/480ad344-571c-4cbb-9289-7fc39ee11b97" />
Fungsi utama program,
Membuat objek stack dari class StackBuku,
Perulangan menu sampai user memilih keluar,
Menampilkan judul program,
Menampilkan pilihan menu operasi stack,
User memasukkan pilihan menu
<img width="302" height="236" alt="11" src="https://github.com/user-attachments/assets/f80c897d-c37e-449c-bc51-684bd4af8739" />
Jika memilih menu 1 → tambah buku,
Memanggil fungsi push,
Menjalankan fungsi pop,
Menjalankan fungsi peek,
Menampilkan seluruh isi stack,
Keluar dari program
<img width="258" height="103" alt="12" src="https://github.com/user-attachments/assets/73b53747-c9bb-43d6-a042-0aab4cb2484f" />
Jika user tidak memilih sesuai pilihan maka menampilkan pesan pilihan tidak valid

Output Kode :
<img width="303" height="356" alt="OUTPUT 1" src="https://github.com/user-attachments/assets/b32e7b71-614a-452a-9806-d0847a474adb" />
<img width="257" height="224" alt="OUTPUT 2" src="https://github.com/user-attachments/assets/ba607d2e-4d78-4140-93a3-574abbb0c253" />

Link Youtube : https://youtu.be/bjOqNiH1DWw

