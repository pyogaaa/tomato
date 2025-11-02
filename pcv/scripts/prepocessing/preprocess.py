import cv2
import numpy as np

def clean_frame(frame: np.ndarray, width: int = 640, height: int = 480, blur_ksize: tuple = (5, 5)) -> np.ndarray:
    """
    Membersihkan frame dengan melakukan resize dan blur.
    
    Parameter:
        frame (numpy.ndarray): Frame gambar yang akan diproses.
        width (int): Lebar frame setelah di-resize. Default 640.
        height (int): Tinggi frame setelah di-resize. Default 480.
        blur_ksize (tuple): Ukuran kernel blur Gaussian. Default (5, 5).
    
    Return:
        cleaned_frame (numpy.ndarray): Frame yang sudah diresize dan diblur.
    """
    if frame is None:
        raise ValueError("Frame tidak boleh None.")

    # Pastikan frame valid
    if not isinstance(frame, np.ndarray):
        raise TypeError("Input frame harus berupa array gambar (numpy.ndarray).")

    # Resize frame ke ukuran tertentu
    resized_frame = cv2.resize(frame, (width, height))  # pyright: ignore

    # Lakukan Gaussian blur untuk mengurangi noise
    blurred_frame = cv2.GaussianBlur(resized_frame, blur_ksize, 0)  # pyright: ignore

    return blurred_frame


# ---- Contoh penggunaan langsung (bisa dihapus saat diimpor modul lain) ----
if __name__ == "__main__":
    # Perbaikan penamaan folder (dari prepocessing → preprocessing)
    input_path = "scripts/preprocessing/daun_tomat.jpg"
    output_path = "scripts/preprocessing/hasil_cleaned.jpg"

    image = cv2.imread(input_path)

    if image is None:
        print(f"Gagal membaca gambar dari '{input_path}'. Pastikan file ada dan path benar.")
    else:
        cleaned = clean_frame(image)
        cv2.imwrite(output_path, cleaned)
        print(f"Frame berhasil diproses dan disimpan sebagai '{output_path}'.")
