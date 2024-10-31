# # momor 1
x = int(input("masukkan jarak: "))
y = 10000
z = 10000*1.25
p = z*1.1
q = p*1.5

if x < 0:
    print("jarak harus lebih dari nol")
elif x <= 10 :
    print(f"biayanya: {int(y)}")
elif x <= 20 :
    print(f"biayanya: {int(z)}")
elif x <= 35 :
    print(f"biayanya:  {int(p)}")
elif x <= 40 :
    print(f"biayanya: {int(q)}")  
else:
    print("jarak diluar jangkauan")


# # nomor 2
# x = int(input("masukkan angka: "))
# a, b = 0, 1
# for i in range(x):
#     print(a)
#     a, b =  b, a+b


# nomor 3
x = input("masukkan jenis koin: ")

for i in range(len(x)):
    if x.count(x[i]) == 1:
        print(f"koin ke {i + 1}")
        break