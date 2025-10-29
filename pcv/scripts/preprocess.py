# File: /scripts/preprocess.py
# Pemilik: Anggota 2 (Preprocessing)

import cv2
import numpy as np

# Tentukan ukuran standar untuk semua gambar
TARGET_WIDTH = 640
TARGET_HEIGHT = 480

# Tentukan kernel untuk blurring
# (Angka ganjil, (5,5) adalah awal yang baik)
BLUR_KERNEL = (5, 5)

def clean_frame(frame):
    """
    Fungsi ini menerima frame mentah (BGR) dari kamera dan melakukan
    langkah preprocessing dasar (resize & blur).
    
    Input: frame (gambar BGR mentah)
    Output: clean_frame (gambar BGR yang sudah di-resize & blur)
    """
    
    # 1. Resize Gambar
    #    Menyamakan ukuran semua gambar agar proses konsisten
    resized_frame = cv2.resize(frame, (TARGET_WIDTH, TARGET_HEIGHT))
    
    # 2. Noise Reduction (Blurring)
    #    Menghaluskan gambar untuk mengurangi noise sensor
    blurred_frame = cv2.GaussianBlur(resized_frame, BLUR_KERNEL, 0)

    return blurred_frame