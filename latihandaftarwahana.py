print("Selamat datang di Dufan") 
nama = input("Masukan Namamu :")
umur = int(input("Masukan Umurmu :"))
print("Halo", nama, "Selamat datang di Dufan")

print("Daftar wahana")
wahana = ["Biang lala RP. 13.000", "Istana Boneka RP. 10.000", "Rumah kaca RP. 15.000", "Roller Coeaster RP. 20.000"]
angka = 1

total_pembelian = 0

for daftar in wahana : 
    print(str(angka), "." , daftar)
    angka = angka + 1
nama_wahana = int(input("pilih nomor wahana :"))

if nama_wahana == 1 :
    print("pilihan wahana nomor 1")
    total_pembelian += 13000
elif nama_wahana == 2 :
    print("pilihan wahana nomor 2")
    total_pembelian += 10000
elif nama_wahana == 3 :
    print("pilihan wahana nomor 3")
    total_pembelian += 15000
elif nama_wahana == 4:
   if(int(umur) > 18) :
    print("pilihan wahana nomor 4")
    total_pembelian += 20000
   else :
      print("umur anda tidak mencukupi, silahkan pilih wahana lain") 
else:
    print("pilihan anda tidak ada di list")

total_pembelian += 2000
print("+ pajak 2000")
print(total_pembelian)