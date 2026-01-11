class View:
    def tampilkan(self, data):
        print("\n=== TABEL DATA MAHASISWA ===")
        print(f"{'No':<5}{'Nama':<35}{'Nilai':10}")
        print("_" * 57)

        for i, mhs in enumerate(data, 1):
            print(f"{i:<5}{mhs.nama:<35}{mhs.nilai:<10}")

        print("-"* 57)