# 🥟 Aplikasi Prediksi & Segmentasi Penjualan Cireng Isi

Aplikasi web interaktif berbasis **Streamlit** yang dirancang untuk membantu analisis bisnis, prediksi hasil penjualan, serta klusterisasi pelanggan pada usaha Cireng Isi menggunakan Machine Learning.

Proyek ini disusun untuk memenuhi tugas **Ujian Akhir Semester (UAS) Machine Learning**.

---

## 📌 Fitur Utama Aplikasi

Aplikasi ini dilengkapi dengan 4 tab utama:
1. **🔮 Prediksi**: Memprediksi estimasi omzet dan tingkat permintaan berdasarkan parameter operasional harian/bulanan.
2. **ℹ️ Informasi Produk**: Menampilkan detail varian rasa, harga, dan profil bisnis Cireng Isi.
3. **📊 Karakteristik**: Visualisasi serta penjelasan mengenai atribut dan tren penjualan produk.
4. **🎯 Prediksi Klaster Pelanggan**: Mengelompokkan segmen pelanggan/penjualan menggunakan Machine Learning (Clustering) serta menyajikan *Rekomendasi Aksionabel* strategi bisnis.

---

## 🛠️ Teknologi yang Digunakan

* **Bahasa Pemrograman**: Python 3.x
* **Framework Web**: Streamlit
* **Analisis & Machine Learning**: Pandas, NumPy, Scikit-Learn
* **Visualisasi Data**: Matplotlib, Seaborn
* **Version Control**: Git & GitHub

---

## 📂 Struktur Repositori

```text
UAS_Machine_Learning/
│
├── app/
│   └── app.py            # Script utama aplikasi Streamlit
├── data/                 # Dataset penjualan cireng
├── model/                # Model machine learning yang sudah dilatih (.pkl)
├── notebook/             # Jupyter Notebook eksperimen model
├── .gitignore            # Konfigurasi pengabaian file Git
└── README.md             # Dokumentasi proyek