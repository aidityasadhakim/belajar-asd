# Contoh 3: Mencari faktorial

'''
12345!
1 * 2 * 3 * 4 * 5 * ... * 1234 * 12345

5!
1*2*3*4*5
'''

# start
# n!
# Deklarasi variabel n yang akan menjadi tujuan faktorial
# Deklarasi variabel i yang akan menjadi awal dari faktorial
# Mengalikan angka dari i sampai ke n
# Display hasil
# stop

# 5!
# 1 * 2 * 3 * 4 * 5

# Iterasi
# angka = 1 2 3 4 5
# total = 1 1 2 6 24 120

n = 5
i = 1
total = 1

for angka in range(i,n + 1):
    total = total * angka

print(total)