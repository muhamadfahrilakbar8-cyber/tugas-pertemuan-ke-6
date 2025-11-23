dict = {
    "Ari" : "081267888", 
    "Dina" : "087677776"
}

#Menampilkan Ari
print("Ari: ", dict['Ari'])

#Menmabah kontak baru
dict.update({"Riko" : "087654544"})
print(dict)

#Mengubah nomor Dina
dict["Dina"] = '088999776'
print(dict)

#Menampilkan semua nama
nama = dict.keys()
print(nama)

#Menampilkan semua nomor 
nomor = dict.values()
print(nomor)

#Menampilkan semua nama dan nomor
daftar_kontak = dict.items()
print(daftar_kontak)

#Menghapus nomor dina
del dict["Dina"]
print(daftar_kontak)

#Daftar kontak
print(f"# {'Nama':<4} | {'Nomor Telephon'}")
print("#" + "="*23)

for nama, nomor in dict.items():
    print(f"# {nama:<4} | {nomor:<15}")