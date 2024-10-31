string = input("masukkan string: ")
kata = input("kata yang ditambahkan: ")
index = int(input())
x = string[:index] + kata +  string[index:]

print(x)

