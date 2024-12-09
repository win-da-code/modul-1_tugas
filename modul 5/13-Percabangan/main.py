# Percabangan
# Percabangan 1 kondisi

# struktur percabangan
"""
    1. if -nya
    2. kondisi, statement yang harus 
    terpenuhi agar aksinya dijalangkan
    3. aksinya
"""

nama = input ("masukan nama anda! ")

# percabangan inline
# if <kondisi> : <aksi>
#if nama == "Imam" : print ("selamat ulang tahun")
#print("Terimah Kasih") # bukan aksi

# Percabangan dengan indentitas
#if nama == "imam" : # kondisi
#    print ("Selamat Ulang Tahun") # aksi
#    print ("sehat selalu") # aksi
#print("jangan berhenti tersenyum") # bukan aksi

# percabangan dengan Else Statement
if nama == "imam" :
    print("selamat datang")
else:
    print("anda bukan imam")

print("program berakhir")