
# 🧪 Riset Fitur Extraction – `cv2.mean()` dan Mask Creation

## 1. Fungsi `cv2.mean(image, mask)`

### 📘 Deskripsi

`cv2.mean()` digunakan untuk menghitung **nilai rata-rata dari setiap channel image** pada area yang ditentukan oleh *mask*.

---

### 🧩 Syntax

```python
mean_values = cv2.mean(image, mask=None)
```

---

### 🔁 Return Value

| Jenis Gambar  | Nilai yang Dikembalikan       |
| ------------- | ----------------------------- |
| **BGR image** | `(mean_B, mean_G, mean_R, 0)` |
| **HSV image** | `(mean_H, mean_S, mean_V, 0)` |
| **Grayscale** | `(mean_intensity, 0, 0, 0)`   |

---

### 🧠 Contoh Penggunaan dengan Mask

```python
import cv2
import numpy as np

# Baca gambar contoh
image = cv2.imread('image.jpg')

# Buat mask untuk area tertentu
mask = np.zeros(image.shape[:2], dtype=np.uint8)
cv2.rectangle(mask, (50, 50), (150, 150), 255, -1)

# Hitung mean hanya pada area mask
mean_values = cv2.mean(image, mask=mask)
print(f"Mean B: {mean_values[0]}, G: {mean_values[1]}, R: {mean_values[2]}")
```

---

## 2. Membuat Mask Individual per Kontur

### ✏️ Menggunakan `cv2.drawContours()`

```python
def create_contour_mask(contour, image_shape):
    """
    Membuat mask individual untuk satu kontur
    """
    mask = np.zeros(image_shape[:2], dtype=np.uint8)
    cv2.drawContours(mask, [contour], -1, 255, -1)  # -1 untuk fill contour
    return mask
```

---

### 🧩 Contoh Penerapan dengan Multiple Contours

```python
# Dapatkan contours dari image
contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Buat mask untuk setiap kontur
masks = []
for contour in contours:
    mask = create_contour_mask(contour, image.shape)
    masks.append(mask)
```

---

## 3. Kombinasi `cv2.mean()` dengan Mask Kontur

### ⚙️ Workflow Lengkap

```python
# Untuk setiap kontur, hitung mean warna pada area tersebut
for i, contour in enumerate(contours):
    # Buat mask individual
    mask = create_contour_mask(contour, image.shape)
    
    # Hitung mean warna hanya pada area kontur
    mean_color = cv2.mean(image, mask=mask)
    
    print(f"Kontur {i}: Mean Color = {mean_color}")
```

---

## ✅ Keuntungan Pendekatan Ini

* **Efisien:** Hanya menghitung pada area yang diperlukan.
* **Akurat:** Hanya area kontur yang dianalisis.
* **Fleksibel:** Bisa diterapkan untuk berbagai jenis fitur citra.

---
