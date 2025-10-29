# File: /pc_receiver/main_receiver.py
# Pemilik: Anggota 4 (PC Interface)
# Tester: Anggota 6 (Integrator)

import cv2
import time
import requests # Pastikan ini ada di requirements.txt untuk W2

# --- URL didapat dari Anggota 3 (Network) ---
# IP ini harus sesuai dengan output Serial Monitor ESP32-CAM
URL_STREAM = "http://192.168.1.10/stream"  # <--- GANTI INI SESUAI IP ANDA

# --- URL Status (Untuk Minggu 2 dan seterusnya) ---
# URL_STATUS = "http://192.168.1.10/status"

print(f"Mencoba menyambung ke stream: {URL_STREAM}...")
cap = cv2.VideoCapture(URL_STREAM)

# Cek koneksi berhasil
if not cap.isOpened():
    print("==============================================")
    print("Error: Tidak bisa membuka stream video.")
    print(f"Pastikan URL ({URL_STREAM}) sudah benar dan ESP32-CAM terhubung ke WiFi.")
    print("==============================================")
    exit()

print("Berhasil terhubung ke stream ESP32-CAM.")
print("Tekan 'q' pada jendela video untuk keluar.")

# Ini adalah 'main loop' aplikasi Anda
while True:
    # --- Bagian 1: Baca Stream Video ---
    ret, frame = cap.read()

    # Jika stream gagal/terputus, coba sambung ulang
    if not ret:
        print("Error: Gagal mengambil frame. Mencoba menyambung kembali...")
        cap.release()
        cap = cv2.VideoCapture(URL_STREAM)
        time.sleep(1) # Beri jeda 1 detik sebelum mencoba lagi
        continue

    
    # --- Bagian 2: Ambil Data Sensor (Tugas W2-P2) ---
    # (Biarkan kosong dulu di W1-P2)
    # try:
    #    response = requests.get(URL_STATUS, timeout=1)
    #    data = response.json()
    #    tds_value = data.get('tds')
    #    print(f"Nilai TDS: {tds_value} PPM")
    # except requests.RequestException as e:
    #    print(f"Error mengambil data JSON: {e}")
    

    # --- Bagian 3: Tampilkan Video (Tugas W1-P2) ---
    # Untuk minggu ini, kita hanya tampilkan frame aslinya
    cv2.imshow("Live Feed ESP32-CAM (PC Receiver)", frame)

    # Cek jika tombol 'q' ditekan untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Setelah loop selesai, lepaskan 'capture' dan tutup semua jendela
print("Menutup stream...")
cap.release()
cv2.destroyAllWindows()