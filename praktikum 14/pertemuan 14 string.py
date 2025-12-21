# Input data
nama = input("Masukkan nama lengkap: ")
telepon = input("Masukkan nomor telepon: ")
email = input("Masukkan email: ")

error = False

# Validasi nama (huruf dan spasi saja)
if not nama.replace(" ", "").isalpha():
    print("Error: Nama lengkap harus hanya berisi huruf.")
    error = True

# Validasi nomor telepon (angka saja)
if not telepon.isdigit():
    print("Error: Nomor telepon harus hanya berisi angka.")
    error = True

# Validasi email (mengandung @ dan .)
if "@" not in email or "." not in email:
    print("Error: Email harus mengandung karakter '@' dan '.'.")
    error = True

# Hasil akhir
if not error:
    print("Data pendaftaran valid")
