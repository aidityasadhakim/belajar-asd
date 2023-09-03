# Mengaplikasikan fitur search untuk mencari angka dari kumpulan angka

'''
[
9,3,4,6,3,6,7,8,2,3,4,1,4,5,234,656,2,234,65,7,8,4,2,43,45,7,4845,132,32,45,43,5,52,2,324,4,21
]
'''
# 123

# Algoritma search

# start
# Menerima list angka done
# Menerima angka yang ingin dicari done
# Melakukan perulangan ke dalam list, untuk mencari angka yang diinginkan
# Jika ketemu, tampilkan bahwa ditemukan
# stop

dataAngka = [
    3,4,6,7,8,3,2,1,3,6,3,3,1,212,35,1,35,61,124,2,6,43,2,4,6,6,6,4432,432,31,
]

angkaCari = 212

if angkaCari in dataAngka:
    print("Number found")
else:
    print("Number not found")

for angka in dataAngka:
    if(angka == angkaCari):
        print("Angka ditemukan")
        break
    else:
        print("Angka tidak sama dengan yang dicari")