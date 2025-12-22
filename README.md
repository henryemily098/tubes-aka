# ANALISIS KOMPLEKSITAS ALGORITMA ITERATIF dan REKURSIF dalam MENGHITUNG DETERMINAN MATRIKS

Determinan matriks didefinisikan sebagai suatu nilai skalar yang dihitung dari elemen-elemen sebuah matriks persegi. Determinan banyak digunakan dalam berbagai permasalahan aljabar linear, seperti penyelesaian sistem persamaan linear, penentuan keberadaan invers matriks, serta aplikasi dalam komputasi numerik dan rekayasa.

## The Problem

Permasalahan yang diangkat dalam tugas besar ini adalah perhitungan determinan matriks persegi berordo n. Permasalahan ini dipilih untuk dianalisis karena dapat diselesaikan menggunakan lebih dari satu pendekatan algoritmik, khususnya pendekatan iteratif dan rekursif.

Studi kasus ini dipilih dengan pertimbangan sebagai berikut:

- Memiliki representasi yang dapat diimplementasikan secara iteratif menggunakan struktur perulangan.
- Memiliki representasi yang dapat diimplementasikan secara rekursif menggunakan pemanggilan fungsi.
- Menunjukkan perbedaan karakteristik kinerja antara pendekatan iteratif dan rekursif seiring dengan bertambahnya ukuran matriks.
- Memungkinkan dilakukan pengukuran empiris waktu eksekusi yang jelas berdasarkan variasi ukuran masukan.

Melalui studi kasus ini, analisis kompleksitas algoritma tidak hanya dilakukan secara teoretis, tetapi juga diverifikasi melalui pengujian empiris, sehingga dapat menunjukkan pentingnya pemilihan algoritma yang efisien dalam penyelesaian suatu permasalahan komputasi.

---

## 👥 Anggota Tim IF-48-05

| Nama                 | NIM          |
| -------------------- | ------------ |
| ANNISA ROSLINA ANWAR | 103012430064 |
| HASNAT FERDIANANDA   | 103012430038 |
| RASYID RIDLO         | 103012400042 |

---

## 🎯 Studi Kasus

**Perhitungan Determinan Matriks 3×3 dengan Aturan Sarrus**

Aturan Sarrus adalah metode khusus untuk menghitung determinan matriks 3×3 dengan cara:

1. Menjumlahkan hasil perkalian diagonal kiri ke kanan (positif)
2. Mengurangi hasil perkalian diagonal kanan ke kiri (negatif)

Rumus:

```
det(A) = (a11×a22×a33 + a12×a23×a31 + a13×a21×a32) - (a13×a22×a31 + a11×a23×a32 + a12×a21×a33)
```

---

## ✨ Fitur Aplikasi

### 1. **Input Matriks Interaktif**

- Input matriks 3×3 dengan nilai default yang dapat diubah
- Mendukung bilangan desimal
- Nilai default:
  ```
  [ 2  -1   4]
  [-4   3   0]
  [ 5  -2   1]
  ```

### 2. **Perbandingan Algoritma**

- ✅ **Algoritma Iteratif**: Menggunakan loop untuk menghitung diagonal
- 🔁 **Algoritma Rekursif**: Menggunakan fungsi rekursif
- 🔍 **Verifikasi NumPy**: Memvalidasi hasil dengan library NumPy

### 3. **Analisis Waktu Eksekusi**

- Mengukur waktu rata-rata dari 3 percobaan (`measure_time`)
- Menampilkan hasil dalam milidetik (ms)
- Visualisasi grafik bar perbandingan

### 4. **Grafik Perbandingan Berbagai Jenis Matriks**

Menguji algoritma pada 8 jenis matriks berbeda:

- Input User (matriks yang diinput)
- Matriks Identitas
- Matriks Sparse (jarang)
- Matriks Dense (padat)
- Matriks Negatif
- Matriks Campuran
- Matriks Besar (nilai tinggi)
- Matriks Desimal

---

## 🛠️ Teknologi yang Digunakan

- **Python 3.x**
- **Streamlit** - Framework untuk web app interaktif
- **NumPy** - Library komputasi numerik
- **Matplotlib** - Library visualisasi data
- **time** - Modul untuk pengukuran waktu eksekusi

---

## 📦 Instalasi

### 1. Clone Repository

```bash
git clone https://github.com/henryemily098/tubes-aka.git
cd tubes-aka
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Isi File `requirements.txt`

```txt
streamlit
numpy
matplotlib
```

---

## 🚀 Cara Menjalankan

### Jalankan Aplikasi Streamlit

```bash
streamlit run determinan_app.py
```

Aplikasi akan terbuka di browser pada alamat:

```
http://localhost:8501
```

---

## 📊 Analisis Kompleksitas

### **Algoritma Iteratif**

```python
def det_iterative(matrix):
    # Kompleksitas Waktu: O(n²) → untuk n=3, O(9)
    # Kompleksitas Ruang: O(1)
```

**Karakteristik:**

- ✅ Lebih **efisien** dalam penggunaan memori
- ✅ **Lebih cepat** untuk kasus sederhana
- ✅ Tidak ada overhead pemanggilan fungsi
- ✅ Tidak ada risiko stack overflow

### **Algoritma Rekursif**

```python
def det_recursive(matrix):
    # Kompleksitas Waktu: O(n²) → untuk n=3, O(9)
    # Kompleksitas Ruang: O(n) → karena call stack
```

**Karakteristik:**

- ✅ **Lebih elegan** dan mudah dipahami secara konseptual
- ❌ **Overhead** pemanggilan fungsi berulang
- ❌ Menggunakan **call stack** lebih banyak
- ❌ Potensi **stack overflow** untuk matriks besar

### **Kesimpulan Analisis**

Untuk kasus determinan matriks 3×3 dengan Aturan Sarrus:

- **Kompleksitas waktu teoritis sama** (keduanya O(n²))
- **Iteratif lebih cepat dalam praktik** karena tidak ada overhead rekursi
- **Rekursif lebih lambat** sekitar 2-5x lipat karena overhead fungsi

---

## 📈 Hasil Pengujian (Contoh)

### Perbandingan Waktu Eksekusi

```
Matrix: [[2, -1, 4], [-4, 3, 0], [5, -2, 1]]

Iteratif  : 0.0023 ms
Rekursif  : 0.0089 ms
NumPy     : 0.0012 ms

Kesimpulan: Iteratif ~3.9x lebih cepat dari Rekursif
```

---

## 📂 Struktur Proyek

```
tubes_aka/
│
├── determinan_app.py   # Aplikasi utama Streamlit
├── requirements.txt    # Dependencies Python
├── README.md           # Dokumentasi proyek
└── determinan.js       # (Opsional) Implementasi JavaScript
```

---

## 🔗 Referensi

1. **Aturan Sarrus** - [Wikipedia](https://en.wikipedia.org/wiki/Rule_of_Sarrus)
2. **Streamlit Documentation** - [docs.streamlit.io](https://docs.streamlit.io)
3. **NumPy Documentation** - [numpy.org](https://numpy.org/doc/)
4. **Big O Notation** - Analisis Kompleksitas Algoritma

---

## 📝 Lisensi

Proyek ini dibuat untuk keperluan tugas akademik **Analisis Kompleksitas Algoritma** di Telkom University.

---

## 🙏 Kontribusi

Dibuat dengan ❤️ oleh **Tim IF-48-05**

Jika ada pertanyaan atau saran, silakan hubungi anggota tim melalui email institusi.
