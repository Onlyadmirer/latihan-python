# evensquare = [x**2 for x in range(1, 11)if x % 2 == 0]
# print(evensquare)


# id = {
#     "name": {"John", "akmal", "joni", "doni"}
# }
# print(id["name"])

isi = {
    "nama": {"akmal":66, "jono":33,"joni":55},
}
pilih =  input("pilih option: ")
print("menu option (Add, update, delete, view, exist)")
if pilih == "add":
    nama = input("nama: ").lower()
    nilai = int(input("nilai: "))
    isi.append(nilai)

if pilih == "update":
    nama1 = input("cari nama: ").lower()
    if  nama1 in isi:
        nilai1 = input("ganti nilai: ")
        isi.remove(isi["nama"],  nilai1)

        
        

    
    

    

