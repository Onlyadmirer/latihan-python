# class segitiga:
#     def  __init__(self, alas, tinggi):
#         self.alas = alas
#         self.tinggi = tinggi
        
#     def luas(self):
#         return 0.5 * self.alas * self.tinggi

    
# segitiga_1 = segitiga(5, 10)

# segitiga_2 = segitiga(10, 10)

# print(f"luas segitiga 1 : {segitiga_1.luas()}")
# print(f"luas segitiga 2 : {segitiga_2.luas()}")


class buku:
    def __init__(self, judul:str, penulis:str, tahun_terbit:int):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit
        
    def deskripsi_buku(self):
        return f"judul buku : {self.judul}\npenulis : {self.penulis}\ntahun terbit : {self.tahun_terbit}"

buku_1 = buku("Tbate", "TurtleMe", 2016)
print(buku_1.deskripsi_buku())
