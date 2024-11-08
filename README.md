# Program Menghitung Sisi Miring Segitiga Siku-Siku

Program ini adalah aplikasi Python berbasis terminal yang dirancang untuk membantu pengguna menghitung sisi miring dari segitiga siku-siku menggunakan **rumus Pythagoras**. Program ini dilengkapi antarmuka pengguna yang interaktif, mendukung pilihan satuan, dan menyimpan riwayat perhitungan dengan timestamp.

## Fitur Utama
- **Perhitungan Sisi Miring**: Menghitung panjang sisi miring (hipotenusa) menggunakan rumus Pythagoras \( a² + b² = c² \).
- **Pilihan Satuan**: Mendukung perhitungan dalam satuan sentimeter (CM) atau meter (M).
- **Riwayat Perhitungan**: Menyimpan dan menampilkan riwayat perhitungan sebelumnya lengkap dengan timestamp.
- **Tampilan Warna**: Menggunakan `colorama` untuk memberikan efek warna pada teks di terminal.
- **Pembersihan Layar Otomatis**: Terminal akan dibersihkan setiap kali perhitungan ulang dilakukan untuk menjaga kerapian tampilan.

## Teknologi yang Digunakan
- **Python**: Bahasa pemrograman utama yang digunakan.
- **Modul `math`**: Untuk perhitungan matematis.
- **Modul `colorama`**: Memberikan efek warna pada tampilan teks terminal.
- **Modul `datetime`**: Untuk mencatat waktu setiap perhitungan dilakukan.
- **Modul `os`**: Untuk membersihkan layar terminal.

## Cara Penggunaan
1. **Jalankan Program**: Setelah menjalankan file, program akan meminta pengguna memilih satuan panjang.
2. **Masukkan Panjang Sisi A dan B**: Pengguna memasukkan panjang sisi segitiga (alas dan tinggi).
3. **Tampilkan Hasil Perhitungan**: Program akan menampilkan panjang sisi miring dalam berbagai konversi satuan (CM, M, MM, KM).
4. **Riwayat Perhitungan**: Pengguna dapat melihat riwayat perhitungan sebelumnya beserta timestamp.
5. **Keluar dari Program**: Pengguna dapat keluar dari program kapan saja.

## Contoh Tampilan
```plaintext
========================================
Menghitung Sisi Miring Segitiga Siku-Siku
========================================

Rumus Pythagoras:
Untuk segitiga siku-siku, rumusnya: a² + b² = c²

Pilih satuan panjang:
1. Sentimeter (CM)
2. Meter (M)
3. Tampilkan Riwayat
4. Keluar

Masukkan panjang sisi A (CM): 8
Masukkan panjang sisi B (CM): 6

Hasil:
10.00 CM | 0.10 M | 100.00 MM | 0.00010 KM
