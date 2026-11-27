# Soal
"""
Buatlah program Python untuk menerima nama dan nilai siswa, kemudian tampilkan kembali informasi tersebut. Mulailah dengan membuat pseudocode, lalu implementasikan ke dalam Python dengan memperhatikan case sensitivity dan penulisan statement. Setelah program dasar berhasil, kembangkan program untuk menentukan status siswa: nilai ≥ 75 = LULUS dan nilai < 75 = TIDAK LULUS. Gunakan keyword if dan else, serta perhatikan whitespace dan indentation pada kode Python.
"""
# Jawaban
"""
MULAI
masukkan nama siswa dan simpan pada variabel
masukkan nilai siswa dalam bentuk bilangan bulat dan simpan pada sebuah variabel
jika nilai siswa lebih dari sama dengan 75 maka siswa dinyatakan lulus
jika tidak maka siswa dinyatakan tidak lulus
cetak status kelulusan siswa
SELESAI
"""
# Code
nama = input("Masukkan nama siswa: ")
nilai = float(input("Masukkan nilai siswa: ")) 
if nilai >= 75 :
    print("LULUS ")
else:
    print("TIDAK LULUS ")