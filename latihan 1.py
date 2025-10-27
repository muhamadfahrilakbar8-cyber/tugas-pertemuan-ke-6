#program menentukan bilangan terbesar dari 4 bilangan

#input 4 bilangan dari pengguna
a = int(input("masukan bilangan pertama:" ))
b = int(input("masukan bilangan kedua:" ))
c = int(input("masukan bilangan ketiga:" ))
d = int(input("masukan bilangan keempat:" ))

terbesar = a
if b > terbesar: terbesar = b
if c > terbesar: terbesar = c
if d > terbesar: terbesar = d

print("print bilangan terbesar adalah:", terbesar)