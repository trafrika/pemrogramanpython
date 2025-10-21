def hitung_ongkir(berat_kg, kota, asuransi=False):
    """
    Menghitung total ongkos kirim berdasarkan kota, berat, dan opsi asuransi.
    """
    # Daftar tarif dasar per kota
    tarif_dasar = {
        "jakarta": 10000,
        "bandung": 12000,
        "surabaya": 15000,
        "medan": 18000,
        "denpasar": 20000
    }

    # Cek apakah kota tersedia
    if kota.lower() not in tarif_dasar:
        return "Kota tidak tersedia dalam layanan RapidSend."

    # Hitung ongkir: tarif_dasar + (2000 * berat) + (asuransi jika True)
    total = tarif_dasar[kota.lower()] + 2000 * berat_kg

    if asuransi:
        total += 3000

    return total


# Contoh pemanggilan fungsi:
print("1️. Ongkir ke Bandung tanpa asuransi:", hitung_ongkir(2.5, "Bandung"))
print("2️. Ongkir ke Surabaya dengan asuransi:", hitung_ongkir(1.2, "Surabaya", asuransi=True))
