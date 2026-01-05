# Sistem Deteksi Nominal Uang Rupiah Real-Time Menggunakan YOLO  
### Berbasis Jetson Orin Nano dan Streaming Kamera

Repositori ini berisi implementasi sistem deteksi nominal uang rupiah secara real-time
menggunakan algoritma **YOLO (You Only Look Once)** yang dijalankan pada perangkat
**Jetson Orin Nano** sebagai edge AI device. Sistem memanfaatkan kamera USB sebagai
sumber input citra dan mampu menampilkan hasil deteksi berupa bounding box, label
nominal uang, serta nilai FPS secara langsung.

---

## Fitur Utama
- Deteksi nominal uang rupiah:  
  **Rp1.000, Rp2.000, Rp5.000, Rp10.000, Rp20.000, Rp50.000, Rp100.000**
- Deteksi objek real-time menggunakan kamera USB
- Performa real-time ±28–33 FPS pada Jetson Orin Nano
- Implementasi berbasis Ultralytics YOLO
- Siap dikembangkan ke TensorRT untuk optimasi performa

---

## Arsitektur Sistem
1. Kamera USB menangkap citra secara real-time  
2. Citra diproses oleh model YOLO terlatih  
3. Model menghasilkan bounding box dan label nominal  
4. Hasil deteksi ditampilkan pada layar beserta FPS  

---

## Dependencies:
- Ubuntu 20.04 (Jetson Orin Nano)
- JetPack 6
- Python 3.10
- Ultralytics YOLO
- PyTorch (NVIDIA ARM64 build)
- OpenCV
- NumPy
