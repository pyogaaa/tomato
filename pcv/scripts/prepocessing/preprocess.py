import cv2
import numpy as np

def clean_frame(frame):
    """
    Membersihkan frame input dengan me-resize dan menerapkan Gaussian blur
    untuk mengurangi noise.
    
    Args:
        frame: Gambar input (dari cv2.read())
        
    Returns:
        Frame yang sudah bersih (resized dan blurred)
    """
    
    # 1. Resize frame agar pemrosesan lebih konsisten dan cepat
    # Kita gunakan ukuran standar 640x480
    width = 640
    height = 480
    dim = (width, height)
    
    # Lakukan resize hanya jika frame-nya ada
    if frame is not None and frame.shape[0] > 0 and frame.shape[1] > 0:
        resized_frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
    else:
        # Kembalikan frame kosong jika ada masalah
        return np.zeros((height, width, 3), dtype=np.uint8)

    # 2. Terapkan Gaussian Blur untuk mengurangi noise
    # Kernel (5,5) adalah ukuran blur yang umum untuk noise reduction
    blurred_frame = cv2.GaussianBlur(resized_frame, (5, 5), 0)
    
    return blurred_frame