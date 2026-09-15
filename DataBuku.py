buku = {
    "judul": "Cantik Itu Luka" ,
    "penulis": "Eka Kurniawan" ,
    "Tahun_Terbit": 2002
}

while True:
    print("\n----MENU DATA BUKU----")
    print("1. Tampilkan Data")
    print("2. Tambah Penerbit")
    print("3. Ubah Penulis") 
    print("4. Hapus Penerbit")
    print("5. Keluar")

    pilihan = input("Pilih Menu: ") 

    if pilihan == "1":
        print("\nData Buku: ")
        print(buku)

    elif pilihan == "2":
        buku["penerbit"] = "Bentang Pustaka"
        print("Penerbit Berhasil Ditambahkan")

    elif pilihan == "3":
        buku["penulis"] = "Septiya Maharani"
        print("Penulis Berhasil Diubah")

    elif pilihan == "4":
        if "penerbit" in buku:
            del buku["penerbit"]
            print("Penerbit Berhasi Dihapus")
        else:
            print("Penerbit tidak Ditemukan" )

    elif pilihan == "5":
        print("Keluar Dari Program")
        break

    else:
        print("Pilihan Tidak Tersedia")

print("\n----DATA BUKU SETELAH PERUBAHAN----")
print(buku)