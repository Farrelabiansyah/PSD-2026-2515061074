Judul : Implementasi metode sorting bubblesort pada urutan harga barang

Deskkripsi Singkat : 
Program tersebut merupakan implementasi algoritma Bubble Sort dalam kehidupan sehari-hari, yaitu untuk mengurutkan harga barang dari yang termurah ke termahal. Data harga disimpan dalam sebuah list, kemudian diproses menggunakan perulangan berulang (nested loop) untuk membandingkan setiap dua elemen yang bersebelahan. Jika ditemukan urutan yang salah, yaitu harga yang lebih besar berada di depan, maka kedua elemen tersebut akan ditukar posisinya hingga akhirnya seluruh data tersusun secara terurut.

Source Code : 
<img width="158" height="31" alt="TA 2 1" src="https://github.com/user-attachments/assets/99a496f9-0cb3-4fce-a50f-d7a612e09c54" />
Mendefinisikan fungsi bernama bubble_sort
Parameter harga adalah list data yang akan diurutkan
Menghitung jumlah data dalam list
Disimpan ke variabel n
<img width="224" height="41" alt="TA 2 2" src="https://github.com/user-attachments/assets/2eda9760-0f5a-4a50-8786-6bcb49c42507" />
Perulangan utama (loop luar)
Digunakan untuk menentukan berapa kali proses sorting dilakukan
Perulangan dalam (loop kedua) untuk membandingkan elemen
n - i - 1 artinya:
Bagian belakang sudah tidak perlu dicek lagi (sudah terurut)
<img width="372" height="105" alt="TA 2 3" src="https://github.com/user-attachments/assets/d9bef25b-a8b3-4bff-86d6-2a6291a397fd" />
Membandingkan dua elemen yang bersebelahan
Jika elemen kiri lebih besar dari kanan → berarti salah urutan
Menukar posisi kedua elemen (swap)
Ini inti dari Bubble Sort
return harga itu berarti Mengembalikan hasil list yang sudah diurutkan
<img width="293" height="37" alt="TA 2 4" src="https://github.com/user-attachments/assets/608fbcea-6242-4a71-b858-c72bf88617f5" />
Data awal (harga barang yang belum terurut)
<img width="219" height="37" alt="TA 2 5" src="https://github.com/user-attachments/assets/6d2ff4b2-fdb9-44de-96df-5fb24b819a65" />
Memanggil fungsi bubble_sort
Hasilnya disimpan ke variabel hasil
<img width="266" height="44" alt="TA 2 6" src="https://github.com/user-attachments/assets/bfd1dc06-ba81-4297-b0d5-f1220245e5ce" />
Menampilkan hasil sorting ke layar

Output Program :
<img width="332" height="16" alt="OUTPUT TA 2" src="https://github.com/user-attachments/assets/7a4fa81d-87a3-47c6-b595-b150ec37b934" />

Link Youtube : 
