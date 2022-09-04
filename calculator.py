# Belajar membuat kalkulator sederhana
# Dengan konsep Object Orinted Programming Dalam Bahasa Python

class Kalkulator:
    hasil = 0
    def __init__(self, angka1, angka2, operasi):
        self.angka1 = angka1
        self.angka2 = angka2
        self.operasi = operasi

    def Hasil(self):
        if self.operasi == 1:
            self.hasil = self.angka1 + self.angka2
            print(self.hasil)
        elif self.operasi == 2:
            self.hasil = self.angka1 - self.angka2
            print(self.hasil)
        elif self.operasi == 3:
            self.hasil = self.angka1 * self.angka2
            print(self.hasil)
        elif self.operasi == 4:
            self.hasil = self.angka1 / self.angka2
            print(self.hasil)
        elif self.operasi == 5:
            self.hasil = self.angka1 // self.angka2
            print(self.hasil)
        elif self.operasi == 6:
            self.hasil = self.angka1 % self.angka2
            print(self.hasil)
        elif self.operasi == 7:
            self.hasil = self.angka1 ** self.angka2
            print(self.hasil)
        else:
            print("Operasi Yang Di masukkan Tidak Valid")

stop = False
while (not stop):
    angka1 = int(input("Masukkan angka pertama : "))
    angka2 = int(input("Masukkan angka kedua   : "))
    print('''
            Pilih Operasi Di bawah! :
            1. tambah  (+)
            2. kurang  (-)
            3. kali    (*)
            3. bahagiP (/)
            4. modulus (%)
            5. bahagiB (//)
            6. pankat  (**)
    ''')
    operasi = int(input("Masukkan Operasi! : "))

    hasilJumlah = Kalkulator(angka1, angka2, operasi)
    hasilJumlah.Hasil()

    Next = input("Do You Want To Continue?[Y/n] : ").lower()

    if Next == 'n':
        stop = True


print("PROGRAM END")
