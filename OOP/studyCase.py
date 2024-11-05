class dino:
    def __init__(self,nama, hewan, hidup):
        self.__hewan = hewan
        self.__hidup = hidup
        self.nama = nama

    def isanimal(self):
        if self.__hewan == True:
            return f"hewan"
        else:
            return f"bukan hewan"

    def isalive(self):
        if self.__hidup == True:
            return f"mahkluk hidup"
        else:
            return f"bukan mahkluk hidup"

class makanan(dino):
    def __init__(self, nama, hewan, hidup, makanan):
        self.makanan = makanan
        super().__init__(nama, hewan, hidup)

    def karnivora(self):
        self.makanan = "karnivora"
        return self.makanan
    def herbivora(self):
        self.makanan = "herbivora"
        return self.makanan
    def __str__(self):
        return f"{self.nama} adalah {self.isalive()} dan merupakan {self.isanimal()} dan dia juga adalah {self.makanan}"

class caraHidup(dino):
    def __init__(self, nama, hewan, hidup, cara_hidup):
        self.cara_hidup = cara_hidup
        super().__init__(nama, hewan, hidup)
    
    def terbang(self):
        self.cara_hidup = "terbang"
        return self.cara_hidup
    def darat(self):
        self.cara_hidup = "darat"
        return self.cara_hidup
    def __str__(self):
        return f"dia hidup di/dengan cara {self.cara_hidup}"
trex1 = makanan("t-rex", True, True, "karnivora")
trex = caraHidup("t-rex", True, True, "terbang")
print(trex1)
print(trex)
