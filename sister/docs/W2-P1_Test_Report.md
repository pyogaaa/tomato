# Laporan Pengujian (W2-P1) - Anggota 6: Integrator & Tester

**Subjek Tes:** `main_receiver.py` (v0.2 dari Anggota 4)
**Tujuan Tes:** Verifikasi *logic* auto-reconnect stream video.

---

## Hasil Pengujian

**Tes 1: Stream Dimatikan (ESP32-CAM dicabut)**
* **Hasil:** `main_receiver.py` **TIDAK CRASH**.
* **Observasi:** Skrip berhasil mendeteksi kegagalan *frame* (`ret == False`) dan masuk ke *loop* "mencoba menyambung kembali..." seperti yang diharapkan.

**Tes 2: Stream Dinyalakan Kembali (ESP32-CAM dicolok)**
* **Hasil:** `main_receiver.py` **BERHASIL** menyambung ulang ke *stream*.
* **Observasi:** *Live feed* video muncul kembali di jendela secara otomatis dalam ~3 detik.

---

## Kesimpulan

**Status: LULUS** ✅

*Logic* auto-reconnect pada `main_receiver.py` berfungsi dengan baik dan stabil.