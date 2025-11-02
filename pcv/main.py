import cv2
import time
import numpy as np

# --- Import skrip anggota lain (INI PENTING) ---
# Kita sekarang meng-import dan menggunakan skrip Anggota 2 & 3
import pcv.scripts.prepocessing.preprocess as pp
import scripts.segmentasi.segmentation as seg
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
    # --- PIPELINE LAMA (W2-P1) ---
    # ----------------------------------------------------

    # 1. Panggil Anggota 2 (Preprocessing)
    #    (Fungsi ini me-resize dan blur frame)
    clean_frame = pp.clean_frame(frame)
    
    # 2. Panggil Anggota 3 (Segmentasi)
    #    (Fungsi ini menghasilkan mask biner hitam-putih)
    mask = seg.get_leaf_mask(clean_frame)

    # ----------------------------------------------------
    # --- PIPELINE BARU (W2-P2) DIMULAI ---
    # ----------------------------------------------------

    # 3. Cari Kontur (bentuk objek) dari mask biner
    #    cv2.RETR_EXTERNAL: Hanya mengambil kontur terluar (pas untuk daun)
    #    cv2.CHAIN_APPROX_SIMPLE: Menyederhanakan poin-poin kontur
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 4. Siapkan frame untuk digambar
    #    Kita akan menggambar kotak di atas 'clean_frame', karena koordinat
    #    kontur dari 'mask' sudah pasti cocok dengan 'clean_frame'
    output_frame = clean_frame.copy()

    # 5. Loop setiap kontur (calon daun) yang ditemukan
    for cnt in contours:
        
        # 6. Filter kontur: Abaikan jika areanya terlalu kecil (noise)
        area = cv2.contourArea(cnt)
        
        # Nilai '500' ini bisa di-tuning (dikecilkan/dibesarkan)
        if area > 500:
            
            # 7. Dapatkan koordinat Bounding Box (kotak) dari kontur
            x, y, w, h = cv2.boundingRect(cnt)
            
            # 8. Gambar kotak HIJAU (0, 255, 0) di 'output_frame'
            #    dengan ketebalan 2 piksel
            cv2.rectangle(output_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
    # ----------------------------------------------------
    # --- AKHIR PIPELINE W2-P2 ---
    # ----------------------------------------------------
    
    
    # --- PENYESUAIAN TAMPILAN SESUAI INSTRUKSI W2-P2 ---
    
    # Tampilkan hasil akhir ke pengguna (Video dengan Kotak)
    # Ini adalah "satu jendela live feed utama" yang diminta
    cv2.imshow("Deteksi Daun (W2-P2)", output_frame)

    # Jendela-jendela lama dari W2-P1 bisa kita matikan (beri komentar)
    # agar tidak mengganggu
    # cv2.imshow("Mask Daun", mask) 
    # cv2.imshow("Live Feed - Deteksi Daun (Anggota 6)", frame)

    # Cek jika tombol 'q' ditekan untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print("Menutup stream...")
cap.release()
cv2.destroyAllWindows()