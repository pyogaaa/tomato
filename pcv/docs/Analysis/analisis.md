

## 1. Tujuan
Mengetahui cara menghitung luas area piksel pada citra daun menggunakan OpenCV dan menentukan persentase gejala kerusakan daun.

## 2. Dasar Teori
- Fungsi `cv2.countNonZero()` digunakan untuk menghitung jumlah piksel putih (non-zero) dalam citra biner.
- Rumus persentase gejala:
  \[
  \text{Persentase} = \frac{\text{Area Gejala}}{\text{Area Daun}} \times 100
  \]

## 3. Metode
1. Konversi citra ke ruang warna HSV.
2. Buat mask daun dan mask gejala berdasarkan rentang warna.
3. Hitung area masing-masing menggunakan `cv2.countNonZero()`.
4. Hitung persentase menggunakan rumus di atas.

## 4. Hasil
- Area gejala = 800 piksel
- Area daun = 5000 piksel
- Persentase gejala = 16%

## 5. Kesimpulan
Fungsi `cv2.countNonZero()` efektif untuk menghitung luas area objek pada citra biner. Dengan rumus persentase, tingkat kerusakan daun dapat ditentukan secara kuantitatif.
