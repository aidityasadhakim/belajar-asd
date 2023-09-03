'''
Contoh 2: Mencari angka tertinggi dari 3 angka berbeda
[5, 2, 7]

Start
Buat tiga variable yang akan menampung angka
If(Angka 1 > Angka 2)
    If(Angka 1 > Angka 3)
        display(”Angka 1 merupakan angka terbesar”)
    else
        display(”Angka 3 merupakan angka terbesar”)
else
    If(Angka 2 > Angka 3)
       display(”Angka 2 merupakan angka terbesar")
    else
       display("Angka 3 merupakan angka terbesar")
Stop
'''

angka1 = 5
angka2 = 10
angka3 = 7

if(angka1 > angka2):
    if(angka1 > angka3):
        print("Angka 1 merupakan angka terbesar")
    else:
        print("Angka 3 merupakan angka terbesar")
else:
    if(angka2 > angka3):
        print("Angka 2 merupakan angka terbesar")
    else:
        print("Angka 3 merupakan angka terbesar")