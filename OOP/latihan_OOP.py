class Hero:
    def __init__(self, nama, kekuatan, kecepatan):
        self.nama = nama
        self.kekuatan = kekuatan
        self.kecepatan = kecepatan
        self.darah = 100

    def serang(self, lawan):
        print(f"{self.nama} menyerang {lawan.nama} dengan kekuatan {self.kekuatan}!")
        lawan.darah -= self.kekuatan
        print(f"Darah {lawan.nama} sekarang {lawan.darah}")

    def tampil_status(self):
        print(f"Nama: {self.nama}, Darah: {self.darah}, Kekuatan: {self.kekuatan}, Kecepatan: {self.kecepatan}")


class Pertarungan:
    def __init__(self, hero1, hero2):
        self.hero1 = hero1
        self.hero2 = hero2

    def mulai_pertarungan(self):
        while self.hero1.darah > 0 and self.hero2.darah > 0:
            self.hero1.serang(self.hero2)
            if self.hero2.darah <= 0:
                break
            self.hero2.serang(self.hero1)
        if self.hero1.darah > 0:
            print(f"{self.hero1.nama} menang!")
        else:
            print(f"{self.hero2.nama} menang!")


# Buat dua hero
hero1 = Hero("Gatotkaca", 20, 10)
hero2 = Hero("Srikandi", 15, 12)

# Tampilkan status hero
hero1.tampil_status()
hero2.tampil_status()

# Mulai pertarungan
pertarungan = Pertarungan(hero1, hero2)
pertarungan.mulai_pertarungan()