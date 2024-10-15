# DATA PRIBADI
print("1. DATA PRIBADI")
nama = (input('Masukan nama : '))
nim = int(input('Masukan NIM Anda : '))
tempat = str(input('Masukan Tempat Tinggal : '))
no = int(input('No HP : '))
print()

# Kelengkapan Syarat
print('2. KELENGKAPAN SYARAT')
wni = (input("input Kewargakenegaraan Anda : "))
pekerjaan_orang_tua = (input('Masukan Pekerjaan : '))
gaji = float(input('Masukan Gaji Anda : '))

# Syarat
daftar = ['asn','tni','polri']
js = ('aktif')
wei = ('indonesia')

if (wni in wei) and (pekerjaan_orang_tua not in daftar) and (gaji <= 2000000):
    hasil = ('BERHAK MENDAPATKAN PROGRAM')
else:
    hasil = ('TIDAK BERHAK MENDAPATKAN PROGRAM')

print('-'*20)
print('Nama : ', nama)
print('NIM : ', nim)
print('Pekerjaan : ', pekerjaan_orang_tua)
print('Tempat Tinggal : ', tempat)
print('Nomor handphone : ', no)
print(hasil)