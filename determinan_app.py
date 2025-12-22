import streamlit as st
import time
import numpy as np

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

# ---------- ALGORITMA ----------
def det_iterative(matrix):
    n = len(matrix)
    left = 0
    right = 0
    
    # Diagonal kiri ke kanan (positif)
    for i in range(n):
        k = i
        total = 1
        for j in range(n):
            if k >= n:
                k = 0
            total *= matrix[j][k]
            k += 1
        left += total
    
    # Diagonal kanan ke kiri (negatif)
    for i in range(n):
        k = i
        total = 1
        for j in range(n):
            if k < 0:
                k = n - 1
            total *= matrix[j][k]
            k -= 1
        right += total
    
    return left - right

def inner_recursive(matrix, n, column=0, row=0, step=1):
    if column == n:
        return 1
    
    if step == 1:
        if row == n - 1:
            return matrix[column][row] * inner_recursive(matrix, n, column + 1, 0, 1)
        else:
            return matrix[column][row] * inner_recursive(matrix, n, column + 1, row + 1, 1)
    elif step == -1:
        if row == 0:
            return matrix[column][row] * inner_recursive(matrix, n, column + 1, n - 1, -1)
        else:
            return matrix[column][row] * inner_recursive(matrix, n, column + 1, row - 1, -1)

def det_recursive_helper(matrix, n, row, step):
    """
    Fungsi pembantu untuk rekursi determinan
    """
    if row == n - 1:
        return inner_recursive(matrix, n, 0, row, step)
    else:
        return inner_recursive(matrix, n, 0, row, step) + det_recursive_helper(matrix, n, row + 1, step)

def det_recursive(matrix):
    n = len(matrix)
    return det_recursive_helper(matrix, n, 0, 1) - det_recursive_helper(matrix, n, 0, -1)

# ---------- TIMING HELPER ----------
def measure_time(func, matrix, trials=3):
    times = []
    for _ in range(trials):
        start = time.perf_counter()
        result = func(matrix)
        end = time.perf_counter()
        times.append((end - start) * 1000)
    return result, sum(times) / len(times)

# ---------- STREAMLIT APP ----------
st.set_page_config(page_title="Tubes - Analisis Kompleksitas Algoritma", layout="centered")


# ---------- MAIN APP ----------
st.title("🌐 Aplikasi Perbandingan Algoritma Iteratif vs Rekursif")

# ---------- TEAM SECTION ----------
st.subheader("👥 Anggota Tim IF-48-05")
st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("**Nama:** ANNISA ROSLINA ANWAR")
    st.write("**NIM:** 103012430064")

with col2:
    st.write("**Nama:** HASNAT FERDIANANDA")
    st.write("**NIM:** 103012430038")

with col3:
    st.write("**Nama:** RASYID RIDLO")
    st.write("**NIM:** 103012400042")

st.markdown("---")

st.markdown("### Studi Kasus: Membandingkan perhitungan iteratif dan rekursif dalam menghitung determinan Matriks")
st.info("ℹ️ Aplikasi ini membandingkan efisiensi dua versi algoritma determinan matriks yakni iteratif dan rekursif menggunakan aturan Sarrus.")

# ukurann matrix
n = 3

st.markdown("#### Input Matriks 3 x 3")
st.caption("Masukkan nilai-nilai matriks (bisa angka desimal)")

# default matrix
default_values = [
    [2, -1, 4],
    [-4, 3, 0],
    [5, -2, 1]
]

# matrix input
matrix = []
cols = st.columns(n)

for i in range(n):
    row = []
    for j in range(n):
        with cols[j]:
            val = st.number_input(
                f"[{i},{j}]",
                value=float(default_values[i][j]),
                step=0.1,
                format="%.2f",
                key=f"cell_{i}_{j}",
                label_visibility="collapsed"
            )
            row.append(val)
    matrix.append(row)

# tampilan matrix
st.markdown("**Matriks yang akan dihitung:**")
st.code(np.array(matrix))

# running
if st.button("Jalankan Algoritma"):
    try:
        # iteratif
        res_it, time_it = measure_time(det_iterative, matrix)
        st.success(f"✅ **Iteratif**: det(A) = {res_it:.6f} | Waktu = {time_it:.4f} ms")

        # rekursif
        if n > 8:
            st.warning("⚠️ Rekursif mungkin lambat untuk n > 8.")
        res_rec, time_rec = measure_time(det_recursive, matrix)
        st.error(f"🔁 **Rekursif**: det(A) = {res_rec:.6f} | Waktu = {time_rec:.4f} ms")

        # verif dengan NumPy
        numpy_det = np.linalg.det(matrix)
        st.info(f"🔍 **Verifikasi NumPy**: det(A) = {numpy_det:.6f}")

        # bar chart
        st.subheader("📊 Perbandingan Waktu Eksekusi")
        fig, ax = plt.subplots()
        ax.bar(["Iteratif", "Rekursif"], [time_it, time_rec], color=["green", "red"])
        ax.set_ylabel("Waktu (milidetik)")
        ax.set_title(f"Ukuran Matriks: 3 x 3")
        for i, v in enumerate([time_it, time_rec]):
            ax.text(i, v + max(time_it, time_rec) * 0.02, f"{v:.6f} ms", ha="center")
        st.pyplot(fig)

    except RecursionError:
        st.error("❌ Kedalaman rekursi terlampaui. Coba ukuran matriks yang lebih kecil!")
    except Exception as e:
        st.error(f"❌ Terjadi kesalahan: {e}")


# Optional full graph untuk PENDEKATAN VARIASI MATRIKS
st.markdown("---")
st.subheader("📈 Grafik Perbandingan untuk Berbagai Jenis Matriks 3 x 3")
if st.checkbox("Tampilkan perbandingan berbagai jenis matriks"):
    with st.spinner("Menghitung runtime... (mohon tunggu)"):
        
        test_matrices = {
            "Input User": matrix,
            "Identitas": [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            "Sparse": [[1, 0, 0], [0, 0, 0], [0, 0, 2]],
            "Dense": [[5, 7, 9], [3, 8, 6], [4, 2, 1]],
            "Negatif": [[-2, -5, -1], [-3, -4, -6], [-7, -8, -9]],
            "Campuran": [[10, -5, 3], [-2, 0, 7], [4, -8, 1]],
            "Besar": [[100, 200, 300], [400, 500, 600], [700, 800, 900]],
            "Desimal": [[1.5, 2.7, 3.9], [4.2, 5.8, 6.1], [7.3, 8.6, 9.4]]
        }
        
        matrix_names = list(test_matrices.keys())
        it_times = []
        rec_times = []
        
        for name, mat in test_matrices.items():
            _, t_it = measure_time(det_iterative, mat)
            try:
                _, t_rec = measure_time(det_recursive, mat)
            except RecursionError:
                t_rec = None
            it_times.append(t_it)
            rec_times.append(t_rec if t_rec is not None else 0)
        
        # Plot
        fig2, ax2 = plt.subplots(figsize=(10, 5))
        x_pos = np.arange(len(matrix_names))
        width = 0.35
        
        ax2.bar(x_pos - width/2, it_times, width, label="Iteratif", color="green", alpha=0.8)
        ax2.bar(x_pos + width/2, rec_times, width, label="Rekursif", color="red", alpha=0.8)
        
        ax2.set_xlabel("Jenis Matriks")
        ax2.set_ylabel("Waktu (ms)")
        ax2.set_title("Perbandingan Runtime untuk Berbagai Jenis Matriks 3×3")
        ax2.set_xticks(x_pos)
        ax2.set_xticklabels(matrix_names, rotation=45, ha='right')
        ax2.legend()
        ax2.grid(True, axis='y', linestyle='--', linewidth=0.5, alpha=0.7)
        plt.tight_layout()
        st.pyplot(fig2)
        
        # Tabel detail
        st.markdown("#### 📋 Detail Hasil per Jenis Matriks")
        import pandas as pd
        df = pd.DataFrame({
            'Jenis Matriks': matrix_names,
            'Iteratif (ms)': [f"{t:.6f}" for t in it_times],
            'Rekursif (ms)': [f"{t:.6f}" for t in rec_times],
            'Selisih (ms)': [f"{abs(it_times[i] - rec_times[i]):.6f}" for i in range(len(it_times))]
        })
        st.dataframe(df, use_container_width=True)