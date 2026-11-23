umur = int(input("Masukkan umur: "))
pendapatan = int(input("Masukkan pendapatan: "))

if umur <= 17:
    if pendapatan <= 3000000:
        kategori = "Bukan prioritas"
    else:
        kategori = "Prioritas"
else:
    kategori = "Prioritas"

print("Kategori:", kategori)