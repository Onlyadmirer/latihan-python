# 1. mengurutkan sebuah angka menggunakan key "sorted"
my_list = input("masukkan angka(pisahkan dengan spasi): ")
urutkan = sorted(my_list.split())
#konversi string ke float dan jadikan index
konversi_float = [float(x) for x in urutkan]
print(konversi_float)

# 2. menghitung rata-rata
jumlah = 0
for  i in konversi_float:
    jumlah += i
    
rata_rata = jumlah / len(konversi_float)
print(f"rata-rata = {rata_rata}")

# 3. menghitung  median
#median genap
if len(konversi_float) % 2 == 0:
    x = konversi_float[len(konversi_float) // 2 - 1]
    y = konversi_float[len(konversi_float) // 2] 
    print(f"median adalah : {(x + y) / 2 }")
# median ganjil
else:
    print(f"median adalah: {konversi_float[(len(konversi_float) + 1) // 2]}")

# 4. modus

    
