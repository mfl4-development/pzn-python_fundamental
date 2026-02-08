# pzn-python_fundamental

## Program Hello Python
###  File Python
- Pada kenyataannya, saat membuat program menggunakan Python, kita biasanya tidak mungkin jarang menggunakan Python Interactive Shell, biasanya kita akan simpan kode program Python kita dalam file
- File Python menggunakan ekstensi / akhiran .py, menggunakan huruf kecil semua, jika butuh lebih dari satu kata, pisahkan kata dengan underscore (_), dan terakhir hindari spasi dan karakter khusus pada nama file

###  Komentar
- Saat membuat kode program Python, kadang kita butuh menambahkan komentar pada kode ini
- Ini biasanya digunakan untuk catatan agar kita ingat apa yang dilakukan oleh kode ini
- Komentar merupakan kode yang tidak akan dieksekusi oleh Python, jadi ini hanya digunakan sebagai catatan kita
- Kita bisa menggunakan tanda # di awal baris, yang artinya baris tersebut dianggap sebagai komentar

---

## Variabel dan Tipe Data
###  Apa itu Variabel?
- Variabel adalah "wadah" atau "kotak" untuk menyimpan data di dalam memori komputer. Dalam Python, variabel bersifat dinamis - tipe datanya bisa berubah selama program berjalan.
- Analogi Sederhana, bayangkan variabel seperti kotak dengan label. Kita bisa memasukkan berbagai jenis barang ke dalam kotak tersebut, dan labelnya adalah nama variabel.

###  Aturan Penamaan Variabel
- Tidak boleh dimulai dengan angka
- Tidak boleh dimulai dengan angka
- Tidak boleh pakai tanda minus
- Tidak boleh pakai keyword Python
- Tidak boleh ada spasi

###  Tipe Data Dasar Python
- Integer (int) - Bilangan Bulat
- Float - Bilangan Desimal
- String (str) - Teks
- Boolean (bool) - True/False

###  Membuat Variabel
- Untuk membuat variabel, caranya seperti yang sudah kita lihat sebelumnya, yaitu menggunakan tanda = (sama dengan)
- Termasuk jika ingin mengubah data variabel yang sudah dibuat, kita juga bisa menggunakan tanda = (sama dengan)

###  Menggunakan Variabel
- Untuk menggunakan variabel, kita bisa langsung menyebut nama variabel nya
- Contoh misal jika kita ingin print() isi variabel, kita bisa langsung menggunaan function print(nama_variabel)
- Namun jika kita ingin menampilkan lebih dari satu data pada function print(), maka kita perlu menggunakan pemisah koma, misal : print(pertama, kedua, ketiga)

###  Input dari Pengguna
- Kita bisa meminta input dari pengguna menggunakan function input()
- input() selalu menghasilkan string (teks).

###  Konversi Tipe Data
- Konversi tipe data adalah mengubah data dari satu tipe ke tipe lainnya.
- Terdapat beberapa function yang bisa kita gunakan untuk melakukan konversi dari satu tipe data ke tipe data lain
- int(), mengubah string atau data lain menjadi integer (bilangan bulat)
- str(), mengubah integer atau data lain menjadi string (teks)
- float(), mengubah string atau integer menjadi float (bilangan desimal)
- bool(), mengubah data lain menjadi boolean (True/False)
