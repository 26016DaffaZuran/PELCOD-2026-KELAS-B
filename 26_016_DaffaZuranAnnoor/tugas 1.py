# Data diri
nama = input("Masukkan nama: ")
umur = int(input("Masukkan umur: "))
tinggi = float(input("Masukkan tinggi badan (cm): "))
angka_favorit = int(input("Masukkan angka favorit: "))

# Menampilkan data diri
print("\nData Diri")
print("Nama:", nama)
print("Umur:", umur)
print("Tinggi:", tinggi, "cm")
print("Angka favorit:", angka_favorit)

# Data belanja
jumlah_pensil = int(input("\nMasukkan jumlah pensil: "))
jumlah_buku = int(input("Masukkan jumlah buku: "))

# Harga sesuai soal
harga_pensil = 2000
harga_buku = 5000

# Menghitung total
total_pensil = jumlah_pensil * harga_pensil
total_buku = jumlah_buku * harga_buku
total_belanja = total_pensil + total_buku

# Menampilkan total belanja
print("\nTotal harga belanja:", total_belanja)

# Mengecek angka favorit
if angka_favorit % 2 == 0:
    print("Angka favorit:", angka_favorit)
    print("angka genap")
else:
    print("Angka favorit:", angka_favorit)
    print("angka ganjil")