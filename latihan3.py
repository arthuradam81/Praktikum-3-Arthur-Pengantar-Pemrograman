# Program menentukan bilangan terbesar dari tiga bilangan

# Input tiga bilangan dari pengguna
a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))
c = int(input("Masukkan bilangan ketiga: "))

# Menentukan bilangan terbesar
if a >= b and a >= c:
    terbesar = a
if b >= a and b >= c:
    terbesar = b
else:
    terbesar = c

# Menampilkan hasil
print(f"Bilangan terbesar adalah: {terbesar}")
