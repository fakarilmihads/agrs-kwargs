x = 'awesome'

def myfunc():
    print('python is ' + x)



global_var = 20

def fungsi2():
    print("nilai variabel global_var dari dalam fungsi", global_var)

fungsi2()

def fungsi_ubah():
    global global_var
    global_var = 30
    print("nilai variabel global_var dari dalam fungsi", global_var)

fungsi_ubah()

fungsi2()


a, b = True, False

print(not a)
print(not b)

a, b = True, False
# hasil akan True
print (not a)
print (not b)


sebuah_list = [1, 2, 3, 4 ,5]
print (5 in sebuah_list)



kalimat = "Halo ini contoh string"
kapital = kalimat.upper()
print(kapital)

kalimat_kecil = "Halo INI Contoh string"
kapital = kalimat.lower()
print(kapital)

kalimat_besar = "ini Adalah Judul banget"
kapital_awal = (kalimat_besar.capitalize())
print (kapital_awal)

kalimat_hitung = "berapa kali berapa muncul berapa didalam tulisan ini"
kalimat_dua = kalimat_hitung.count("berapa")
print(kalimat_dua)

kalimat_ganti = 'berapa kali ganti kata itu dalam kata'
kalimat_mengganti = kalimat_ganti.replace('kata', "baca")
print(kalimat_mengganti)

kalimat = "pisang anggur jelek banget"
kalimat_dua = kalimat.split( )
print(kalimat_dua)

# Import library NumPy
# Import library NumPy
import numpy as np
# Data nilai siswa
nilai_siswa = np.array([75, 80, 65, 90, 85])

# Menghitung rata-rata nilai
rata_rata = np.mean(nilai_siswa)

# Menghitung nilai maksimum
nilai_maks = np.max(nilai_siswa)

# Menghitung nilai minimum
nilai_min = np.min(nilai_siswa)

# Cetak hasil
print("Data nilai siswa:", nilai_siswa)
print("Rata-rata nilai:", rata_rata)
print("Nilai maksimum:", nilai_maks)
print("Nilai minimum:", nilai_min)


