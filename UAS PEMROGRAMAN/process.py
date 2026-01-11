from data import Mahasiswa

class Process:
    def __init__(self):
        self.database = []

    def tambah(self, nama, nilai):
        if not nama.strip():
            raise ValueError("nama wajib diisi!")

        try:
            nilai = float(nilai)

        except:
            raise ValueError("nilai wajib diisi!")

        if nilai < 0 or nilai > 100:
            raise ValueError("nilai wajib diisi!")

        self.database.append(Mahasiswa(nama, nilai))

    def get_all(self):
        return self.database
