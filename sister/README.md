# Proyek Sistem Tertanam: Monitoring Hidroponik Tomat

Repositori ini berisi kode untuk *firmware* (ESP32-CAM) dan *software* (PC Receiver) untuk proyek monitoring kesehatan daun tomat dan nutrisi (TDS).

---

## 🚀 Cara Setup & Flashing ESP32-CAM (W1-P2)

Ini adalah panduan untuk meng-upload *firmware* (kode `.ino`) ke ESP32-CAM menggunakan Arduino IDE.

### Alat yang Dibutuhkan
* ESP32-CAM
* FTDI Programmer (USB-to-TTL Converter)
* Kabel Jumper
* Komputer dengan Arduino IDE

### Langkah-langkah Upload (Flashing)

1.  **Instalasi Board ESP32:**
    * Buka `File > Preferences` di Arduino IDE.
    * Masukkan URL ini di "Additional Boards Manager URLs":
        ```
        [https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json](https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json)
        ```
    * Buka `Tools > Board > Boards Manager...`, cari "esp32", dan instal.

2.  **Setup Hardware (Mode Upload):**
    * Hubungkan FTDI Programmer ke ESP32-CAM:
        * `5V` FTDI -> `5V` ESP32
        * `GND` FTDI -> `GND` ESP32
        * `TX` FTDI -> `UOR` (RX) ESP32
        * `RX` FTDI -> `UOT` (TX) ESP32
    * **PENTING:** Pasang kabel jumper antara pin `GPIO 0` dan `GND` di ESP32-CAM. Ini adalah "Mode Upload".

3.  **Upload Kode:**
    * Buka *file* `.ino` (dari folder `/firmware/`) di Arduino IDE.
    * Pilih *board*: `Tools > Board > ESP32 Arduino > AI Thinker ESP32-CAM`.
    * Pilih *port* (Port COM tempat FTDI terdeteksi).
    * Tekan tombol `Upload` (panah ke kanan).

4.  **Menjalankan Kode (Mode Run):**
    * Setelah "Done uploading" muncul, **CABUT KABEL JUMPER** antara `GPIO 0` dan `GND`.
    * Buka `Serial Monitor` (set *baud rate* ke `115200`).
    * Tekan tombol `RST` (reset) di papan ESP32-CAM.
    * Perhatikan Serial Monitor untuk melihat proses koneksi WiFi dan Alamat IP.