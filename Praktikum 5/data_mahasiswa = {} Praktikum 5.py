data_mahasiswa = {}

while True:
    print("Program Input Nilai")
    print("="*19)
    print()
    pilih = input("[(L)ihat, (T)ambah], (U)bah, (H)apus, (C)ari, (K)eluar] :")
    
    if pilih.upper() == "T":
        print("Tambah Data")
        nim = input("NIM :")
        nama = input("Nama :")
        nilai_tugas = int(input("Nilai Tugas :"))
        nilai_uts = int(input("Nilai UTS :"))
        nilai_uas = int(input("Nilai UAS :"))
        
        nilai_akhir = (nilai_tugas * 0.30) + (nilai_uts * 0.35) + (nilai_uas * 0.35)
        
        data_mahasiswa[nim] = {
            'nim' : nim,
            'nama' : nama,
            'tugas' : nilai_tugas,
            'uts' : nilai_uts,
            'uas' : nilai_uas,
            'akhir' : nilai_akhir
        }
    
    elif pilih.upper() == "U" :
        print("Ubah Data")
        nim = input("Masukan NIM yang ingin diubah :")
        nilai_tugas = int(input("Nilai Tugas :"))
        nilai_uts = int(input("Nilai UTS :"))
        nilai_uas = int(input("Nilai UAS :"))
        
        nilai_akhir = (nilai_tugas * 0.30) + (nilai_uts * 0.35) + (nilai_uas * 0.35)
        
        data_mahasiswa[nim] = {
            'nim' : nim,
            'nama' : data_mahasiswa[nim]['nama'],
            'tugas' : nilai_tugas,
            'uts' : nilai_uts,
            'uas' : nilai_uas,
            'akhir' : nilai_akhir
        }
        
    elif pilih.upper() == "L" :
        print("Daftar Nilai")
        print("="*78)
        print(f"| {'No':^4} | {'Nama':^15} | {'NIM':^10} | {'Tugas':^7} | {'UTS':^7} | {'UAS':^7} | {'Akhir':^7} |")
        print("="*78)
        
        count = 0
        for nim in data_mahasiswa :
            count = count + 1
            print(f"|{count:^4} | {data_mahasiswa[nim]['nama']:<15} | {data_mahasiswa[nim]['nim']:^10} | {data_mahasiswa[nim]['tugas']:^7} | {data_mahasiswa[nim]['uts']:^7} | {data_mahasiswa[nim]['uas']:^7} | {data_mahasiswa[nim]['akhir']:^7.2f} |")
        print("="*78)
        
    elif pilih.upper() == "H":
        print("Hapus Data")
        nim = input("Masukan NIM yang ingin dihapus :")
        del data_mahasiswa[nim]
        
    elif pilih.upper() == "C":
        print("Cari Data")
        nim = input("Masukan NIM yang dicari :")
        print("="*78)
        print(f"| {'Nama':^15} | {'NIM':^10} | {'Tugas':^7} | {'UTS':^7} | {'UAS':^7} | {'Akhir':^7} |")
        print("="*78)
        print(f"|{data_mahasiswa[nim]['nama']:<15} | {data_mahasiswa[nim]['nim']:^10} | {data_mahasiswa[nim]['tugas']:^7} | {data_mahasiswa[nim]['uts']:^7} | {data_mahasiswa[nim]['uas']:^7} | {data_mahasiswa[nim]['akhir']:^7.2f} |")
        print("="*78)
    
    elif pilih.upper() == "K":
        break
    
    else:
        print("Perintah tidak ditemukan!")