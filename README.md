# Praktikum-3-Arthur-Pengantar-Pemrograman
# Latihan-3-Arthur-Adam-Radhitya-312510233

# Logika-Flowchart-Latihan-3

Mulai
Input
Masukkan a → bilangan pertama
Masukkan b → bilangan kedua
Masukkan c → bilangan ketiga
Masukkan d → bilangan keempat
Proses Penentuan Bilangan Terbesar
Periksa: apakah a >= b dan a >= c?
Jika ya, maka terbesar = a
Periksa: apakah b >= a dan b >= c?
Jika ya, maka terbesar = b
Jika tidak, maka terbesar = c
(Catatan)
Variabel d belum digunakan di dalam perbandingan (jadi hasilnya hanya dari a, b, dan c).
Output
Tampilkan teks: "Bilangan terbesar adalah: [terbesar]"
Selesai

# Penjelasan

a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))
c = int(input("Masukkan bilangan ketiga: "))

Program meminta pengguna untuk memasukkan empat bilangan (a, b, c, dan d).
int() digunakan agar bisa menerima bilangan desimal (misal 3.5, 2.1, dll).
Tapi, walau ada d, nilai d tidak digunakan dalam perhitungan — jadi hasilnya tetap hanya membandingkan a, b, dan c.

if a >= b and a >= c:
    terbesar = a
if b >= a and b >= c:
    terbesar = b
else:
    terbesar = c

Pertama, dicek apakah a lebih besar atau sama dengan b dan c.
Jika benar, terbesar diisi dengan nilai a.
Lalu dicek lagi apakah b lebih besar atau sama dengan a dan c.
Jika benar, terbesar diisi dengan nilai b.
Jika kondisi kedua salah, berarti c yang paling besar → terbesar = c.


print(f"Bilangan terbesar adalah: {terbesar}")
Program menampilkan hasil akhir dengan format string f-string.
Misalnya, jika a=5, b=2, c=3, maka output-nya:
Bilangan terbesar adalah: 5
