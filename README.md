1️⃣ data.py (Class Data)
class Mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai

2️⃣ process.py (Class Process)
from data import Mahasiswa

class Process:
    def __init__(self):
        self.database = []

    def tambah(self, nama, nilai):
        if not nama.strip():
            raise ValueError("Nama tidak boleh kosong!")

        try:
            nilai = float(nilai)
        except:
            raise ValueError("Nilai harus berupa angka!")

        if nilai < 0 or nilai > 100:
            raise ValueError("Nilai harus antara 0–100!")

        self.database.append(Mahasiswa(nama, nilai))

    def get_all(self):
        return self.database

3️⃣ view.py (Class View)
class View:
    def tampilkan(self, data):
        print("\n=== TABEL DATA MAHASISWA ===")
        print(f"{'No':<4}{'Nama':<20}{'Nilai':<10}")
        print("-" * 36)

        for i, mhs in enumerate(data, 1):
            print(f"{i:<4}{mhs.nama:<20}{mhs.nilai:<10}")

        print("-" * 36)

4️⃣ main.py (Demo Program / Program Utama)
from process import Process
from view import View

proses = Process()
view = View()

while True:
    print("\n=== MENU UTAMA ===")
    print("1. Tambah Data")
    print("2. Tampilkan Semua Data")
    print("3. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        try:
            nama = input("Masukkan nama mahasiswa : ")
            nilai = input("Masukkan nilai         : ")
            proses.tambah(nama, nilai)
            print("✔ Data berhasil ditambahkan!")
        except Exception as e:
            print(f"✖ Error: {e}")

    elif pilih == "2":
        view.tampilkan(proses.get_all())

    elif pilih == "3":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")

▶️ Cara Demo Saat Program Dijalankan

Contoh demo input:

Pilih menu: 1
Masukkan nama mahasiswa : Fahril
Masukkan nilai         : 85


Output:

✔ Data berhasil ditambahkan!


Tampilkan data:

Pilih menu: 2


Output tabel:

=== TABEL DATA MAHASISWA ===
No  Nama                Nilai
------------------------------------
1   Fahril                85.0
------------------------------------
