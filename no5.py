import os
import csv
import json
import logging

# 1) Setup logging ===
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)

# 2) Membuat folder data (jika belum ada) ===
folder = "data"
if not os.path.exists(folder):
    os.makedirs(folder)
    logging.info("Folder 'data' berhasil dibuat.")
else:
    logging.info("Folder 'data' sudah ada, lanjut proses.")

# 3) Menulis file CSV presensi ===
csv_file = os.path.join(folder, "presensi.csv")
try:
    with open(csv_file, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        # Header
        writer.writerow(["nim", "nama", "hadir_uts"])
        # Tiga baris data contoh
        writer.writerow(["230103180","TRAFRIKA NINING ERINA",1])
        writer.writerow(["230103180","SAVINA DYAH A", 1])
        writer.writerow(["2301032563", "NIA", 0])
    logging.info(f"File CSV '{csv_file}' berhasil ditulis.")
except Exception as e:
    logging.error(f"Gagal menulis CSV: {e}")

# 4) Membaca CSV dan menghitung ringkasan ===
try:
    with open(csv_file, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        data = list(reader)

        total = len(data)
        hadir = sum(int(row["hadir_uts"]) for row in data)
        persentase = (hadir / total) * 100 if total > 0 else 0

        ringkasan = {
            "total_mahasiswa": total,
            "jumlah_hadir": hadir,
            "persentase_hadir": round(persentase, 2)
        }

    logging.info("Data berhasil dibaca dan dihitung.")
except Exception as e:
    logging.error(f"Gagal membaca CSV: {e}")
    ringkasan = {}

# 5) Menulis hasil ringkasan ke file JSON ===
json_file = os.path.join(folder, "ringkasan.json")
try:
    with open(json_file, mode="w", encoding="utf-8") as f:
        json.dump(ringkasan, f, indent=4)
    logging.info(f"Ringkasan berhasil disimpan di '{json_file}'.")
except Exception as e:
    logging.error(f"Gagal menulis JSON: {e}")
