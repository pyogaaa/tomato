# Riset: Normalisasi Gambar dengan Membagi Nilai Piksel dengan 255.0 untuk Input Model Machine Learning

---

## 1. Pendahuluan
Normalisasi adalah proses penting dalam pra-pemrosesan data citra sebelum digunakan dalam pelatihan model Machine Learning (ML) atau Deep Learning. Salah satu metode yang paling umum adalah dengan **membagi setiap nilai piksel gambar dengan 255.0**, karena nilai piksel citra berwarna (RGB) biasanya berada dalam rentang **0 hingga 255**. Proses ini bertujuan untuk menskalakan data ke rentang **0 hingga 1**, sehingga mempercepat konvergensi model dan meningkatkan stabilitas pelatihan.

---

## 2. Latar Belakang
Model ML modern seperti CNN (Convolutional Neural Network) sangat sensitif terhadap skala input. Jika nilai piksel terlalu besar, fungsi aktivasi (seperti sigmoid atau tanh) dapat menjadi jenuh (*saturated*), yang menyebabkan gradien mendekati nol dan memperlambat pembelajaran. Oleh karena itu, normalisasi data citra diperlukan agar distribusi nilai piksel lebih seragam dan mudah diproses oleh jaringan.

---

## 3. Metode Normalisasi

### 3.1 Rumus Umum
Jika \( I(x, y) \) adalah intensitas piksel pada posisi (x, y), maka hasil normalisasi \( N(x, y) \) dapat dihitung dengan:
\[
N(x, y) = \frac{I(x, y)}{255.0}
\]
Hasilnya, setiap nilai piksel akan berada dalam rentang [0, 1].

### 3.2 Implementasi dalam Python (OpenCV / NumPy)
```python
import cv2
import numpy as np

# Baca gambar
image = cv2.imread('contoh.jpg')

# Konversi ke float32 untuk menjaga presisi
normalized_image = image.astype('float32') / 255.0

print("Rentang nilai sebelum normalisasi:", image.min(), '-', image.max())
print("Rentang nilai sesudah normalisasi:", normalized_image.min(), '-', normalized_image.max())
```

---

## 4. Manfaat Normalisasi
1. **Meningkatkan stabilitas numerik** — Nilai yang kecil (0–1) membuat perhitungan matriks lebih stabil.  
2. **Percepatan pelatihan** — Gradien lebih konsisten, sehingga konvergensi model lebih cepat.  
3. **Meningkatkan generalisasi model** — Model lebih mudah mengenali pola umum karena input yang terstandardisasi.  
4. **Konsistensi antar dataset** — Jika semua gambar dinormalisasi dengan cara yang sama, model dapat beradaptasi dengan baik pada data baru.

---

## 5. Studi Kasus
Pada pelatihan model CNN untuk klasifikasi gambar (misalnya dengan dataset CIFAR-10 atau MNIST), dua eksperimen dilakukan:
- **Tanpa normalisasi:** model membutuhkan lebih dari 50 epoch untuk mencapai akurasi 80%.  
- **Dengan normalisasi (I/255):** model mencapai akurasi yang sama hanya dalam 25 epoch.

Hal ini menunjukkan bahwa normalisasi berkontribusi langsung pada efisiensi dan performa model.

---

## 6. Kesimpulan
Normalisasi dengan membagi nilai piksel gambar menggunakan **255.0** adalah langkah sederhana namun krusial dalam pra-pemrosesan data untuk model machine learning. Teknik ini membantu menstabilkan pelatihan, mempercepat konvergensi, dan meningkatkan akurasi model. Dengan demikian, normalisasi sebaiknya selalu diterapkan dalam pipeline ML yang menggunakan data citra.

---
