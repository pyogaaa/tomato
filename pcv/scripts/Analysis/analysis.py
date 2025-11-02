import cv2

def calculate_health_percentage(leaf_mask, symptom_mask):
    """
    Menghitung luas area daun, area gejala, dan persentase gejala & kesehatan.
    """
    # --- 1. Hitung area ---
    area_daun = cv2.countNonZero(leaf_mask)
    area_gejala = cv2.countNonZero(symptom_mask)

    # --- 2. Cegah pembagian dengan nol ---
    if area_daun == 0:
        symptom_percentage = 0.0
    else:
        symptom_percentage = (area_gejala / area_daun) * 100

    health_percentage = 100 - symptom_percentage

    # --- 3. Kembalikan hasil dalam bentuk dict ---
    return {
        "area_daun": area_daun,
        "area_gejala": area_gejala,
        "symptom_percentage": round(symptom_percentage, 2),
        "health_percentage": round(health_percentage, 2)
    }

# Contoh uji (opsional)
if __name__ == "__main__":
    import numpy as np

    # Buat contoh mask sederhana
    leaf_mask = np.ones((10, 10), dtype="uint8") * 255  # seluruh area daun
    symptom_mask = np.zeros((10, 10), dtype="uint8")
    symptom_mask[0:4, 0:4] = 255  # area rusak (4x4 piksel = 16 piksel)

    result = calculate_health_percentage(leaf_mask, symptom_mask)
    print(result)
