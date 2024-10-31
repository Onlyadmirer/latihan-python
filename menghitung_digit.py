a = int(input("masukkan angka: "))
a1 = a
jumlah = 0

while a1 != 0:
    a1 //= 10
    jumlah += 1
    
print(f"jumlah digit dari {a} adalah {jumlah}")