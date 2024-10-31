class kucing:
    nyawa = 100
    def __init__(self,  nama, umur, skils):
        self.nama = nama
        self.umur = umur
        self.skils = skils
        
    def bunuh_diri(self):
        self.nyawa -= 10
        return f"\nnama: {self.nama}\nskils: {self.skils}\nnyawa: {self.nyawa}\numur: {self.umur}"

kucing1 = kucing("Tom", 5, "berlari cepat")
kucing2 = kucing("Mochi", 3, "cakar dajjal")

panggil = int(input("masukkan berapa kali kucing dipanggil: "))
for i in range(panggil):
    print(kucing1.bunuh_diri() * i)
    
