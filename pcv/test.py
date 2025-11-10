import cv2
import numpy as np
import prepocess as pp  # pastikan file ini ada
import segmentation as seg  # pastikan file ini ada


# --- MAIN PROGRAM ---
GAMBAR_UJI = "daun2.jpg"  # Ganti sesuai file
frame = cv2.imread(GAMBAR_UJI)

if frame is None:
    print(f"Error: Tidak bisa membaca gambar dari {GAMBAR_UJI}")
    exit()

print(f"Berhasil memuat gambar: {GAMBAR_UJI}")
print("Memproses gambar...")

# 1. Preprocessing
clean_frame = pp.clean_frame(frame)

# 2. Segmentasi daun (daun = putih)
mask = seg.get_leaf_mask(clean_frame)

# 3. Ambil kontur dari area putih
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

output_frame = clean_frame.copy()

if contours:
    # Ambil kontur terbesar (daun utama)
    cnt = max(contours, key=cv2.contourArea)
    area = cv2.contourArea(cnt)

    if area > 2000:
        x, y, w, h = cv2.boundingRect(cnt)

        # Pastikan area ini benar-benar dominan hijau
        roi = clean_frame[y:y + h, x:x + w]
        hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        lower_green = np.array([25, 40, 40])
        upper_green = np.array([90, 255, 255])
        mask_roi = cv2.inRange(hsv_roi, lower_green, upper_green)
        green_ratio = cv2.countNonZero(mask_roi) / (w * h)

        # Jika >50% hijau, dianggap daun
        if green_ratio > 0.5:
            cv2.rectangle(output_frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.putText(output_frame, "Daun Terdeteksi", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            
            cropped_leaf = seg.crop_leaf(clean_frame, x, y, w, h)
            cv2.imshow("Daun Terpotong", cropped_leaf)

# --- Tampilkan hasil ---
cv2.imshow("Deteksi Daun", output_frame)
cv2.imshow("Mask Daun", mask)
print("Proses selesai. Tekan 'q' atau tutup jendela untuk keluar.")

# Tunggu sampai semua jendela ditutup oleh user
while True:
    # waitKey(1) return -1 jika tidak ada tombol ditekan
    key = cv2.waitKey(1)

    # Jika tombol 'q' ditekan
    if key == ord('q'):
        break

    # Jika semua jendela sudah ditutup manual (klik X)
    if cv2.getWindowProperty("Deteksi Daun", cv2.WND_PROP_VISIBLE) < 1 or \
       cv2.getWindowProperty("Mask Daun", cv2.WND_PROP_VISIBLE) < 1:
        break

# Tutup semua jendela secara aman
cv2.destroyAllWindows()
