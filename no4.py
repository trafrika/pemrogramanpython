def jadwal_hari(hari):
    """
    Menampilkan jadwal kuliah berdasarkan hari yang dicari.
    """
    jadwal = [
        {"hari": "senin", "mata_kuliah": "Pemrograman Mobile", "jam": "13.30 - 16.00"},
        {"hari": "senin", "mata_kuliah": "Basis Data", "jam": "13.30 - 16.00"},
        {"hari": "selasa", "mata_kuliah": "Pengantar IOT", "jam": "10.30 - 13.30"},
        {"hari": "rabu", "mata_kuliah": "Kecerdasan Mesin dan Buatan", "jam": "10.30 - 13.30"},
        {"hari": "kamis", "mata_kuliah": "Pemrograman Python", "jam": "08.00 - 10.30"},
        {"hari": "jumat", "mata_kuliah": "Teknik Digital", "jam": "08.00 - 10.30"}
    ]

    print(f"\nJadwal kuliah hari {hari.capitalize()}:")
    ditemukan = False
    for data in jadwal:
        if data["hari"].strip() == hari.lower().strip():
            print(f"- {data['mata_kuliah']} ({data['jam']})")
            ditemukan = True

    if not ditemukan:
        print("Tidak ada jadwal pada hari tersebut.")


# 🔁 Program utama
print("=== Jadwal Kuliah Prodi ===")
while True:
    input_hari = input("\nMasukkan nama hari (atau ketik 'keluar' untuk berhenti): ").lower().strip()
    
    if input_hari == "keluar":
        print("Terima kasih telah menggunakan program jadwal prodi!")
        break
    else:
        jadwal_hari(input_hari)
