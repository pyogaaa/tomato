# File: /scripts/segmentation.py
# Pemilik: Anggota 3 (Segmentasi Daun)

import cv2
import numpy as np

def create_leaf_mask(clean_bgr_frame):
    """
    Fungsi ini menerima frame BGR yang sudah bersih (dari Anggota 2),
    mengubahnya ke HSV, dan membuat mask biner untuk warna hijau (daun).
    
    Input: clean_bgr_frame (gambar BGR)
    Output: mask (gambar biner hitam-putih)
    """
    
    # 1. Konversi Color Space (Krusial!)
    #    Mengubah dari BGR ke HSV untuk deteksi warna yang stabil
    hsv_image = cv2.cvtColor(clean_bgr_frame, cv2.COLOR_BGR2HSV)
    

    # 2. Tentukan Rentang Warna Hijau di HSV
    #    Ini adalah estimasi awal (Tugas W1-P2 Anggota 3)
    #    Format: (Hue, Saturation, Value)
    lower_green = np.array([35, 40, 40])   # Batas bawah hijau
    upper_green = np.array([85, 255, 255]) # Batas atas hijau

    # 3. Buat Mask (Thresholding)
    #    Membuat gambar biner: putih (daun) dan hitam (bukan daun)
    mask = cv2.inRange(hsv_image, lower_green, upper_green)

    # 4. Pembersihan Mask (Tugas W2-P2 Anggota 3, tapi kita masukkan di sini)
    #    Menggunakan MORPH_OPEN untuk menghilangkan bintik-bintik noise kecil
    kernel = np.ones((5, 5), np.uint8)
    mask_cleaned = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    
    #    Menggunakan MORPH_CLOSE untuk menutup lubang-lubang kecil di dalam daun
    mask_final = cv2.morphologyEx(mask_cleaned, cv2.MORPH_CLOSE, kernel)

    return mask_final