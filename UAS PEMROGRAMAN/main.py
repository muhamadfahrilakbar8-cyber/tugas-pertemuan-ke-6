from process import Process
from view import View

proses = Process()
view = View()

while True:
    print("\n === MENU UTAMA ===")
    print("1. Tambah data")
    print("2. Lihat data")
    print("3. keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        try:
            nama = input("masukan nama mahasiswa")
            nilai = input("masukan nilai mahasiswa")
            proses.tambah(nama,nilai)
            print("data berhasil ditambahkan!")
        except Exception as e:
            print(f"eror: {e}")

    elif pilih == "2":
        view.tampilkan(proses.get_all())

    elif pilih == "3":
        print("program selesai.")
        break

    else:
        print("pilihan tidal valid!")