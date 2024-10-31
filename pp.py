konversi = {
    "m/s": {"nilai": 1},
    "km/h":{"nilai": 3.6},
    "mph": {"nilai": 2.23694},
    "knot":{"nilai": 1.94384},
    "mach":{"nilai": 0.00291545}
}

# Fungsi untuk mengkonversi satuan kecepatan
def kecepatan(satuan1: str, satuan2: str, nilai: float):
    try:
        # Hitung hasil konversi dengan mengalikan nilai awal dengan nilai satuan1 kemudian dibagi nilai satuan2
        hasil = nilai * konversi[satuan1]["nilai"] / konversi[satuan2]["nilai"]
        return f"{hasil:.2f}"
    except KeyError:
        # Jika input tidak valid, cetak pesan kesalahan
        return "Input tidak valid"
    