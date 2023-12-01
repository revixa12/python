# def hitung(angka1, angka2, operasi):
#     if operasi == 'tambah':
#         hasil = angka1 + angka2
#     elif operasi == 'kali':
#         hasil = angka1 * angka2
#     else:
#         hasil = 'Operasi tidak valid'
    
#     return hasil

# angka1 = 5
# angka2 = 3
# operasi_tambah = 'tambah'
# operasi_kali = 'kali'

# hasil_tambah = hitung(angka1, angka2, operasi_tambah)
# hasil_kali = hitung(angka1, angka2, operasi_kali)

# print(f'Hasil penjumlahan: {hasil_tambah}')
# print(f'Hasil perkalian: {hasil_kali}')

def buat_perulangan(kata, jumlah_perulangan):
    for _ in range(jumlah_perulangan):
        print(kata)

kata = "Hello, World!"
jumlah_perulangan = 3

buat_perulangan(kata, jumlah_perulangan)        
