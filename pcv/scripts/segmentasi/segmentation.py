import cv2
import numpy as np

def get_leaf_mask(frame):
    """
    Membuat mask biner (hitam-putih) untuk mendeteksi area daun 
    berdasarkan rentang warna hijau dalam HSV.
    
    Args:
        frame: Frame input (sudah di-preprocess / dibersihkan)
        
    Returns:
        Mask biner (gambar hitam-putih)
    """
    
    # 1. Konversi frame dari BGR ke HSV (Hue, Saturation, Value)
    # HSV jauh lebih baik untuk segmentasi warna daripada BGR
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 2. Tentukan rentang warna hijau di HSV
    # CATATAN: Ini adalah bagian PALING PENTING. 
    # Nilai ini mungkin perlu diubah (tuning) tergantung kondisi cahaya
    # dan kehijauan daun Anda.
    
    # H[35-85] umumnya mencakup warna hijau hingga hijau kekuningan
    # S[40-255] membuang warna pudar/abu-abu
    # V[40-255] membuang warna gelap/hitam
    
    lower_green = np.array([35, 40, 40])   # H(min), S(min), V(min)
    upper_green = np.array([85, 255, 255]) # H(max), S(max), V(max)

    # 3. Buat mask biner
    # Area yang warnanya masuk rentang -> Putih (255)
    # Area yang warnanya di luar rentang -> Hitam (0)
    mask = cv2.inRange(hsv_frame, lower_green, upper_green)

    # 4. (Opsional tapi direkomendasikan) Bersihkan mask dari noise kecil
    # Gunakan Erosi untuk menghilangkan titik-titik putih kecil
    # Gunakan Dilasi untuk menebalkan kembali area daun utama
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.erode(mask, kernel, iterations=1)
    mask = cv2.dilate(mask, kernel, iterations=2)
    
    return mask