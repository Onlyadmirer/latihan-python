# a,b = 0,1

# for i in range(15):
#     print(a)
#     a, b = b, a + b

n = int(input("Masukkan jumlah baris: "))
for i in range(1,n+1):
    print("*"*(n-i),end="")
    if i==1:
        print("*")
    elif i==n:
        print("*"*(2*i-1))
    else:
        print("*"+" "*(2*i-3)+"*")