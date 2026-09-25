import streamlit as st
import pandas as pd
import joblib
from pathlib import Path
import streamlit as st

# Judul Utama
st.title("🥟 Prediksi Penjualan :orange[Cireng Isi]")
st.write("Aplikasi ini digunakan untuk memprediksi jumlah produk cireng isi yang dapat terjual.")

st.divider() # Garis pemisah

import streamlit as st

# 1. Buat Tab terlebih dahulu
tab1, tab2, tab3 = st.tabs([
    "📍 Prediksi", 
    "ℹ️ Informasi Produk", 
    "📊 Karakteristik"
])

# 2. Isi Tab 1 (Prediksi Penjualan)
with tab1:
    st.subheader("Form Prediksi Penjualan")
    
    # Masukkan semua inputan dan tombol kamu di sini
    produk = st.selectbox("Pilih Produk", ["Cireng Ayam Suwir", "Cireng Keju", "Cireng Sosis", "Cireng Bakso"])
    harga = st.number_input("Harga Produk", value=5000)
    hari = st.selectbox("Hari", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
    promo = st.selectbox("Promo", ["Tidak Ada Promo", "Ada Promo"])
    cuaca = st.selectbox("Cuaca", ["Cerah", "Hujan"])
    
    if st.button("📊 Prediksi Penjualan"):
        # Logika prediksi kamu
        st.success("Perkiraan jumlah produk terjual: **50** pcs")
          # Menampilkan kartu berwarna kustom
    col_m1, col_m2 = st.columns(2)
    
    with col_m1:
        st.markdown("""
        <div style="background-color: #1E293B; padding: 15px; border-radius: 10px; border-left: 5px solid #10B981;">
            <p style="color: #94A3B8; margin: 0; font-size: 14px;">📦 Perkiraan Terjual</p>
            <h2 style="color: #FFFFFF; margin: 0;">50 pcs</h2>
        </div>
        """, unsafe_allow_html=True)
        
    with col_m2:
        st.markdown("""
        <div style="background-color: #1E293B; padding: 15px; border-radius: 10px; border-left: 5px solid #3B82F6;">
            <p style="color: #94A3B8; margin: 0; font-size: 14px;">💰 Estimasi Omset</p>
            <h2 style="color: #FFFFFF; margin: 0;">Rp 250.000</h2>
        </div>
        """, unsafe_allow_html=True)

# 3. Isi Tab 2 (Informasi Produk)
with tab2:
    st.subheader("Detail Varian Cireng Isi")
    st.write("Daftar rasa yang tersedia saat ini:")
    st.markdown("""
    * 🍗 **Cireng Ayam Suwir** - Pedas gurih dengan isian ayam melimpah.
    * 🧀 **Cireng Keju** - Lumer di dalam dengan keju pilihan.
    * 🌭 **Cireng Sosis** - Rasa favorit anak muda.
    * 🍡 **Cireng Bakso** - Isian bakso kenyal dan lezat.
    """)
    import streamlit as st
# 4. Isi Tab3 Karakteristik)
with tab3:
    st.title("📊 Karakteristik & Profiling 4 Klaster Pelanggan Cireng")
    st.caption("Hasil analisis segmentasi mendalam berdasarkan model Machine Learning yang telah dilatih.")
    
    # BARIS PERTAMA (KLASTER 0 & KLASTER 1)
    col1, col2 = st.columns(2, gap="medium")
    
    with col1:
        with st.container(border=True):
            st.subheader("👑 Klaster #0: Pelanggan Setia / Langganan")
            st.caption("30% Pelanggan — Pembeli rutin mingguan dengan volume pesanan stabil & menyukai varian favorit.")
            
            c1, c2, c3 = st.columns(3)
            c1.metric("🔄 Rata-rata Beli", "8x / Bln")
            c2.metric("🍽️ Porsi / Beli", "5-10 Pcs")
            c3.metric("💰 Pengeluaran", "Rp 100rb")
            
            st.info("💡 **ACTION PLAN:** Berikan program stamp kartu langganan (Gratis 1 pcs setiap beli 10x) dan diskon porsi besar.")

    with col2:
        with st.container(border=True):
            st.subheader("🎉 Klaster #1: Pembeli Party / Event (Borongan)")
            st.caption("25% Pelanggan — Jarang membeli, namun sekali memesan dalam jumlah sangat banyak untuk acara/kumpul.")
            
            c1, c2, c3 = st.columns(3)
            c1.metric("📅 Rata-rata Beli", "1x / Bln")
            c2.metric("📦 Porsi / Beli", "30-50 Pcs")
            c3.metric("💵 Pengeluaran", "Rp 250rb")
            
            st.info("💡 **ACTION PLAN:** Sediakan paket bundling hampers / catering box dan penawaran gratis ongkir pengiriman instan.")

    st.write("") # Jarak antar baris

    # BARIS KEDUA (KLASTER 2 & KLASTER 3)
    col3, col4 = st.columns(2, gap="medium")
    
    with col3:
        with st.container(border=True):
            st.subheader("🔥 Klaster #2: Anak Muda Impulsif (Cemilan)")
            st.caption("25% Pelanggan — Sangat responsif terhadap promo di medsos, suka mencoba varian pedas & kekinian.")
            
            c1, c2, c3 = st.columns(3)
            c1.metric("⚡ Rata-rata Beli", "5x / Bln")
            c2.metric("🍢 Porsi / Beli", "2-4 Pcs")
            c3.metric("💸 Pengeluaran", "Rp 50rb")
            
            st.info("💡 **ACTION PLAN:** Tawarkan promo flash sale jam istirahat sekolah/kuliah serta varian pedas bertingkat (level pedas).")

    with col4:
        with st.container(border=True):
            st.subheader("🔍 Klaster #3: Pembeli Coba-coba / Pasif")
            st.caption("20% Pelanggan — Hanya sesekali membeli, frekuensi transaksi rendah dan cenderung memilih harga termurah.")
            
            c1, c2, c3 = st.columns(3)
            c1.metric("🐢 Rata-rata Beli", "1x / Bln")
            c2.metric("🛒 Porsi / Beli", "1-2 Pcs")
            c3.metric("🪙 Pengeluaran", "Rp 15rb")
            
            st.info("💡 **ACTION PLAN:** Kirimkan kupon diskon 'Selamat Datang Kembali' atau penawaran paket hemat trial mix varian.")
            # Isi Tab 4 (Prediksi Klaster Pelanggan)
st.set_page_config(
    page_title="Prediksi Klaster Pelanggan",
    layout="wide"
)
st.markdown("""
    <style>
    /* Latar belakang utama */
    .stApp {
        background-color: #F8FAFC;
    }
    
    /* Efek Kartu / Container Putih */
    div[data-testid="stVerticalBlock"] > div[data-testid="stBlock"] {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.05);
        border: 1px solid #E2E8F0;
    }
    
    /* Styling Tombol Utama */
    .stButton > button {
        width: 100%;
        background-color: #0066FF;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        height: 48px;
        border: none;
        box-shadow: 0px 4px 8px rgba(0, 102, 255, 0.3);
    }
    
    .stButton > button:hover {
        background-color: #0052CC;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)
col_left, col_right = st.columns([1, 1.8], gap="large")
# 4. Isi Tab 4 (Prediksi Klaster Pelanggan)                            
with tab1:
    st.subheader("Input Parameter Penjualan Cireng")
    st.caption("Masukkan detail operasional harian/bulanan di bawah ini.")
    
    # Contoh input disesuaikan dengan fitur dataset Cireng Isi kamu:
    harga_jual = st.number_input("Harga Jual per Pcs (Rp)", value=5000)
    jumlah_produksi = st.slider("Jumlah Produksi Harian (Pcs)", 50, 1000, 200)
    biaya_promosi = st.slider("Biaya Promosi (Rb)", 0, 500, 50)
    hari_operasional = st.slider("Hari Operasional / Bulan", 1, 30, 26)
    
    btn_predict = st.button("🚀 Prediksi Hasil Penjualan")
        
    st.divider()

with tab1:
    st.subheader("Hasil Prediksi Model Machine Learning")
    st.caption("Menampilkan estimasi performa penjualan & rekomendasi bisnis.")
    
    # Kartu Hasil Prediksi Cireng Isi
    st.markdown("""
        <div style="background-color: #F0FDF4; border-left: 5px solid #22C55E; padding: 15px; border-radius: 8px;">
            <span style="background-color: #DCFCE7; color: #15803D; padding: 4px 12px; border-radius: 20px; font-weight: bold; font-size: 12px;">Kategori: Laris Manis</span>
            <h2 style="color: #1E293B; margin-top: 10px;">Estimasi Omzet: Rp 15.000.000 / Bulan</h2>
            <p style="color: #64748B;">Prediksi menunjukkan tingkat permintaan tinggi berdasarkan harga dan anggaran promosi yang diinputkan.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Strategi Bisnis Cireng Isi
    st.markdown("""
    **💡 Rekomendasi Aksionabel:**
    * Pertahankan kualitas rasa dan tingkat kepedasan isi cireng.
    * Tingkatkan stok bahan baku pada akhir pekan (weekend).
    * Optimalkan promosi media sosial lokal.
    """)