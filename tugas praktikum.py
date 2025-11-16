daftar_data = []

while True:
    print("\nMasukkan Data Mahasiswa")
    nama = input("NAMA : ")
    nim = input("NIM  : ")
    tugas = float(input("Nilai Tugas : "))
    uts = float(input("Nilai UTS   : "))
    uas = float(input("Nilai UAS   : "))

    nilai_akhir = (0.30 * tugas) + (0.35 * uts) + (0.35 * uas)

    # simpan ke list
    daftar_data.append([nama, nim, tugas, uts, uas, nilai_akhir])

    lanjut = input("Tambah data (y/t)? ").lower()
    if lanjut == "t":
        break

# tampilkan daftar data
print("\n=============================================================")
print("No | Nama          | NIM       | Tugas | UTS  | UAS  | Akhir")
print("---------------------------------------------------------------")

no = 1
for d in daftar_data:
    print(f"{no:2} | {d[0]:10} | {d[1]:6} | {d[2]:5} | {d[3]:3} | {d[4]:3} | {d[5]:.2f}")
    no += 1