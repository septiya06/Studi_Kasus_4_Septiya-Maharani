# Studi_Kasus_4_Septiya-Maharani

**NAMA  : SEPTIYA MAHARANI**<br>
**NIM   : 101**


# PENJELASAN KODE PROGRAM

# **1.Inisialisasi Data Buku (Struktur Data Dictionary)**

> <img width="218" height="83" alt="DIREC" src="https://github.com/user-attachments/assets/3fcb6a9d-af66-47b5-a03a-dfd98fcc2a07" />

- **Kegunaan: Bagian ini berfungsi untuk membuat sebuah Dictionary bernama buku sebagai tempat penyimpanan data**
- **Cara Kerja: Data disimpan dalam bentuk pasangan key (kunci/label) dan value (nilai/isi data) yang dipisahkan oleh tanda titik dua (:), serta ditutup dengan kurung kurawal {}. Pada awal program, dictionary ini diisi dengan tiga pasangan data:<br>
      - Key "judul" dengan value "Cantik Itu Luka"<br>
      -Key "penulis" dengan value "Eka Kurniawan"<br>
      -Key "Tahun_Terbit" dengan value 2002<br>
Dan tanda koma (,) digunakan sebagai pemisah antar data dalam Dictionary. Koma diperlukan agar Python dapat mengenali bahwa satu pasangan key dan value sudah selesai dan dilanjutkan dengan data berikutnya.**
  

# **2.while True**

> <img width="90" height="25" alt="while true" src="https://github.com/user-attachments/assets/a0cc3f0a-f24a-42f0-8dda-33f78cf1d56c" />

- **Digunakan untuk membuat program terus mengulang menu sampai pengguna memilih untuk keluar.**

# **3.Menu Data Buku**

> <img width="248" height="119" alt="print" src="https://github.com/user-attachments/assets/6dc888d5-333f-4e61-bb82-67412d7c91a1" />

- **Bagian ini digunakan untuk menampilkan pilihan menu yang dapat dipilih oleh pengguna, yaitu tampilkan data, tambah penerbit, ubah penulis, hapus penerbit, dan keluar.**

# **4.input() Pilihan Menu**

> <img width="206" height="29" alt="pilihan" src="https://github.com/user-attachments/assets/854dd2c5-8a31-4eac-9d42-1cb0d66c336d" />

- **Digunakan untuk menerima pilihan menu yang dimasukkan oleh pengguna.**

# **5.Pilihan 1(Tampilkan Data)**

> <img width="181" height="56" alt="1" src="https://github.com/user-attachments/assets/dee0695c-59aa-4d72-a79f-05f5ea3d23d2" />

- **if pilihan == "1" digunakan untuk menjalankan perintah ketika pengguna memilih menu 1. print("\nData Buku:") digunakan untuk menampilkan tulisan Data Buku di layar. Sedangkan print(buku) digunakan untuk menampilkan isi Dictionary buku.**

# **6.Pilihan 2 (Tambah Penerbit)**

> <img width="277" height="59" alt="2" src="https://github.com/user-attachments/assets/a51c4eb3-38cf-43d4-bf22-725f111a5f52" />

- **elif pilihan == "2" digunakan ketika pengguna memilih menu 2. buku["penerbit"] digunakan untuk menambahkan data penerbit ke Dictionary. print() digunakan untuk menampilkan pesan bahwa penerbit berhasil ditambahkan.**

# **7.Pilihan 3(Ubah Penulis)**

> <img width="248" height="56" alt="3" src="https://github.com/user-attachments/assets/083d5e9d-dd50-4880-a75c-44877321b000" />

- **elif pilihan == "3" digunakan ketika pengguna memilih menu 3. buku["penulis"] digunakan untuk mengubah data penulis menjadi Septiya Maharani. print() digunakan untuk memberi tahu bahwa data penulis berhasil diubah.**

# **8.Pilihan 4 (Hapus Penulis)**

> <img width="282" height="103" alt="5" src="https://github.com/user-attachments/assets/f1dcf756-653c-4765-bf58-63cf307b0544" />

- **elif pilihan == "4" digunakan ketika pengguna memilih menu 4. if "penerbit" in buku digunakan untuk mengecek apakah data penerbit ada. Jika ada, del buku["penerbit"] digunakan untuk menghapusnya dan print() menampilkan pesan bahwa penerbit berhasil dihapus. Jika tidak ada, else akan menjalankan print() yang memberi tahu bahwa penerbit tidak ditemukan.**

# **9.Pilihan 5 (Keluar)**

> <img width="217" height="62" alt="break" src="https://github.com/user-attachments/assets/71dc99cf-b4ab-4f21-a4d2-e7d6d65aeff5" />

- **elif pilihan == "5" digunakan ketika pengguna memilih menu 5. print() menampilkan pesan keluar dari program, sedangkan break digunakan untuk menghentikan perulangan.**


# **10.break**

> <img width="217" height="62" alt="break" src="https://github.com/user-attachments/assets/5b78590e-e39a-45b4-922e-94ed44bc1a76" />

- **break digunakan untuk menghentikan perulangan ketika pengguna memilih menu 5 atau menu keluar.**

# **11.Data Buku Setelah Perubahan**

> <img width="290" height="41" alt="selesI" src="https://github.com/user-attachments/assets/d5a59fd2-95f0-4095-a07a-6648ef8eb2ae" />

- **print() pertama digunakan untuk menampilkan judul Data Buku Setelah Perubahan. print(buku) digunakan untuk menampilkan isi Dictionary buku setelah melakukan perubahan pada data buku.**


# HASIL OUTPUT PROGRAM

# **1.Hasil Tampilkan Data**

> <img width="467" height="304" alt="lihat data" src="https://github.com/user-attachments/assets/91b54663-7877-4f11-b08b-78f5b2d37343" />

# **2.Hasil Tambah Penerbit dan Tampilkan Data Setelah Menambah Penerbit**

> <img width="652" height="361" alt="tambah penerbit" src="https://github.com/user-attachments/assets/b746eea3-b118-4aee-891a-c9b6ca0f9c7c" />

# **3.Hasil Ubah Penulis dan Tampilkan Data Setelah Ubah Penulis**

> <img width="668" height="364" alt="ubah penulis" src="https://github.com/user-attachments/assets/8d8da720-51f5-4cd7-997d-129d2900d6a7" />

# **4.Hasil Hapus Penerbit dan Tampilkan Data Setelah Penerbit Dihapus**

> <img width="499" height="367" alt="hapus penerbit" src="https://github.com/user-attachments/assets/89144308-d739-488f-b3e9-01ee4adb8858" />

# **5.Tampilan Jika Gagal Keluar/Pilihan Tidak Tersedia**

> <img width="226" height="225" alt="pilihan tidak tersedia" src="https://github.com/user-attachments/assets/00a434b1-3bfd-42a7-8f2e-b13058730fe9" />

# **6.Hasil Dari Tampilan Berhasi Keluar dan Tampilan Data Buku Setelah Perubahan**

> <img width="479" height="171" alt="keluar" src="https://github.com/user-attachments/assets/988b611a-1556-48b6-a1fa-6e20a349758f" />
















