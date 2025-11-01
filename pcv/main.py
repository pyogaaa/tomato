import cv2
import time
import numpy as np

# --- Import skrip anggota lain (INI PENTING) ---
# Kita sekarang meng-import dan menggunakan skrip Anggota 2 & 3
import pcv.scripts.prepocessing.preprocess as pp
import scripts.segmentation as seg
# --------------------------------------------------

# URL Stream ESP32-CAM
URL_STREAM = "http://192.168.137.56:81/stream"  # <--- Pastikan IP ini masih valid

print(f"Mencoba menyambung ke stream: {URL_STREAM}...")
cap = cv2.VideoCapture(URL_STREAM)

if not cap.isOpened():
    print("==============================================")
    print("Error: Tidak bisa membuka stream.")
    print(f"Pastikan URL ({URL_STREAM}) sudah benar dan ESP32-CAM terhubung ke WiFi.")
    print("==============================================")
    exit()

print("Berhasil terhubung ke stream ESP32-CAM.")
print("Tekan 'q' pada jendela video untuk keluar.")


while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Gagal mengambil frame. Mencoba menyambung kembali...")
        cap.release()
        cap = cv2.VideoCapture(URL_STREAM)
        time.sleep(1)
        continue

    # ----------------------------------------------------
    # --- PIPELINE INTEGRASI MINGGU 2 (W2-P1) DIMULAI ---
    # ----------------------------------------------------

    # 1. Panggil Anggota 2 (Preprocessing)
    #    (Fungsi ini harusnya me-resize dan blur frame)
    clean_frame = pp.clean_frame(frame)
    
    # 2. Panggil Anggota 3 (Segmentasi)
    #    (Fungsi ini harusnya konversi ke HSV dan membuat mask hijau)
    #    Outputnya adalah gambar BINER (hitam-putih)
    mask = seg.create_leaf_mask(clean_frame)

    # --- TUGAS W2-P1: Tampilkan Mask (Tujuan Utama) ---
    # Ini adalah jendela debug baru untuk melihat hasil segmentasi
    cv2.imshow("Mask Daun (Debug - W2-P1)", mask)

    # ----------------------------------------------------
    # --- AKHIR PIPELINE W2-P1 ---
    # ----------------------------------------------------
    
    # Tampilkan hasil akhir ke pengguna (Video Asli)
    cv2.imshow("Live Feed - Deteksi Daun (Anggota 6)", frame)

    # Cek jika tombol 'q' ditekan untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print("Menutup stream...")
cap.release()
cv2.destroyAllWindows()