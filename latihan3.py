# Program menentukan bilangan terbesar dari tiga bilangan

# Input tiga bilangan dari pengguna
a = float(input("Masukkan bilangan pertama: "))
b = float(input("Masukkan bilangan kedua: "))
c = float(input("Masukkan bilangan ketiga: "))

# Menentukan bilangan terbesar
if a >= b and a >= c:
    terbesar = a
if b >= a and b >= c:
    terbesar = b
else:
    terbesar = c

# Menampilkan hasil
print(f"Bilangan terbesar adalah: {terbesar}")
