# Meminta tiga angka satu per satu
s1 = int(input("Masukkan setoran minggu 1: "))
s2 = int(input("Masukkan setoran minggu 2: "))
s3 = int(input("Masukkan setoran minggu 3: "))

#  Validasi input
if s1 <= 0 or s2 <= 0 or s3 <= 0:
    print("Input tidak valid.")
else:
    # Hitung total
    total = s1 + s2 + s3
    print(f"Total setoran: Rp{total:,.0f}")

    #  Klasifikasi total
    if total < 300000:
        print("Kategori: rendah")
    elif total <= 600000:  # berarti 300000 ≤ total < 600000
        print("Kategori: sedang")
    else:  # total ≥ 600000
        print("Kategori: tinggi")
        