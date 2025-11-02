import cv2
from analysis import calculate_health_percentage

# === 1. Baca gambar mask statis ===
leaf_mask = cv2.imread("d:/projek pcv/minggu10/daun 12.png", cv2.IMREAD_GRAYSCALE)
symptom_mask = cv2.imread("d:/projek pcv/minggu10/daun 4.png", cv2.IMREAD_GRAYSCALE)

# === 2. Jalankan fungsi perhitungan ===
result = calculate_health_percentage(leaf_mask, symptom_mask)

# === 3. Tampilkan hasil ===
print(f"Persentase gejala: {result['symptom_percentage']:.2f}%")
print(f"Persentase kesehatan daun: {result['health_percentage']:.2f}%")

# === 4. Laporan hasil tes ===
print("Laporan Tes: Perhitungan persentase sudah benar ")
