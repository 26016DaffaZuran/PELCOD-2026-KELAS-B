daftarbuku = ["audit", "tata kelola", "sikancil"]

print ("===KOLEKSI BUKU===")
print ("0", "daftar_buku"[0])
print ("1", "daftar_buku"[1])
print ("2", "daftar_buku"[2])

nama = input("Masukkan nama: ")
umur = int(input("Masukkan umur: "))
status_aktif = input ("Apakah anda aktif? (y/n)").lower() == "y"

pilihan = int (input("pilih buku ke1 : "))

syarat_umur = status_aktif == "ya" and umur >= 17

hari_sekarang = 0
lama_pinjam = 1
batas_penembalian = hari_sekarang + lama_pinjam

print ("\n==hasil pengemblian==")
if not syarat_umur:
    print (f"Maaf {nama}, pinjaman ditolak.")
    if not status_aktif:
        print ("anda bukan mahasiswa aktif.")
else :
    buku_pimjam = [daftar_buku[pilihan]]
    print (f"selamat{nama}, pinjaman berhasil")
    print ("buku yang dipinjam: ", buku_pimjam)
    print ("batas pengembalian: ", {batas_pengembalian,})