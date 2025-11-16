print ("NAMA  : RIFKI ADE TIA")
print ("NIM   : 312510334")
print ("KELAS : TI.25.C5")
print()
# Buat sebuah list sebanyak 5 elemen dengan nilai bebas
A = [10, 20, 30, 40, 50]
print("List A:", A)
print()
print("===== AKSES LIST =====")
# tampilkan elemen ke 3
print("Elemen ke-3:", A[2])

# ambil nilai elemen ke 2 sampai elemen ke 4
print("Elemen ke 2 sampai 4:", A[1:4])

# ambil elemen terakhir
print("Elemen terakhir:", A[-1])
print()
print("===== UBAH ELEMEN LIST =====")
# ubah elemen ke 4 dengan nilai lainnya
A[3] = 99
print("Ubah elemen ke-4:", A)

# ubah elemen ke 4 sampai elemen terakhir
A[3:] = [100, 200] 
print("Ubah elemen ke-4 s/d terakhir:", A)
print()
print("===== TAMBAH ELEMEN LIST =====")
# ambil 2 bagian dari list pertama (A) dan jadikan list ke-2 (B)
B = A[:2]
print("List B:", B)

# tambah list B dengan nilai string
B.append("pyton")
print("List B tambah string:", B)

# tambah list B dengan 3 nilai
B.extend([100, 200, 300])
print("List B tambah 3 nilai:", B)

# gabungkan list B dengan list A
gabungan = B + A
print("Gabungan B + A:", gabungan)
print()
print("=== HASIL AKHIR ===")
print("List A:", A)
print("List B:", B)