def garis():
    print("-" * 40)

def hitung_total(harga, jumlah):
    return harga * jumlah

def hitung_diskon(total):
    if total > 1000000:
        return total * 0.10  # diskon 10%
    elif total > 300000:
        return total * 0.05  # diskon 5%
    else:
        return 0

def bonus(total):
    if total > 1000000:
        return "Diskon 10% + KAOS KAKI"
    elif total > 300000:
        return "KAOS KAKI"
    else:
        return "VOUCHER"

def main():
    try:
        garis()
        print("🛒 PROGRAM KASIR TOKO SEPATU SEDERHANA 🛒")
        garis()

        nama = input("Nama pelanggan: ")
        barang = input("Nama barang: ")
        harga = int(input("Harga satuan (Rp): "))
        jumlah = int(input("Jumlah beli: "))

        total = hitung_total(harga, jumlah)
        diskon = hitung_diskon(total)
        total_bayar = total - diskon

        garis()
        print(f"Total belanja  : Rp{total:,}")
        print(f"Diskon         : Rp{diskon:,}")
        print(f"Total bayar    : Rp{total_bayar:,}")
        print(f"Bonus          : {bonus(total)}")
        garis()

        bayar = int(input("Jumlah uang dibayar: Rp"))
        kembalian = bayar - total_bayar

        print(f"Kembalian      : Rp{kembalian:,}")
        garis()
        print(f"Terima kasih, {nama}! Selamat berbelanja kembali 😊")

    except KeyboardInterrupt:
        print("\n❌ Program dibatalkan oleh pengguna.")
    except ValueError:
        print("\n⚠️ Input harus berupa angka untuk harga, jumlah, dan pembayaran!")

if __name__ == "__main__":
    main()
