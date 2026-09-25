import pandas as pd
import numpy as np

# Supaya hasil data tetap sama setiap kali program dijalankan
np.random.seed(42)

# Jumlah transaksi yang akan dibuat
jumlah_data = 1000

# Membuat tanggal transaksi
tanggal = pd.date_range(
    start="2026-01-01",
    periods=jumlah_data,
    freq="D"
)

# Daftar produk
produk = np.random.choice(
    ["Cireng Ayam Suwir", "Cireng Keju", "Cireng Sosis", "Cireng Bakso"],
    size=jumlah_data
)

# Harga setiap produk
harga_produk = {
    "Cireng Ayam Suwir": 5000,
    "Cireng Keju": 5000,
    "Cireng Sosis": 5000,
    "Cireng Bakso": 5000
}

# Menentukan harga berdasarkan produk
harga = [harga_produk[p] for p in produk]

# Menentukan hari
hari = tanggal.day_name()

# Menentukan apakah sedang ada promo
promo = np.random.choice(
    [0, 1],
    size=jumlah_data,
    p=[0.7, 0.3]
)

# Menentukan kondisi cuaca
cuaca = np.random.choice(
    ["Cerah", "Mendung", "Hujan"],
    size=jumlah_data,
    p=[0.5, 0.3, 0.2]
)

# Menentukan stok awal
stok_awal = np.random.randint(
    40,
    121,
    size=jumlah_data
)

# Membuat jumlah produk yang terjual
jumlah_terjual = (
    15
    + (stok_awal * 0.35)
    + (promo * 15)
    + np.where(hari.isin(["Saturday", "Sunday"]), 15, 0)
    - np.where(cuaca == "Hujan", 10, 0)
    + np.random.normal(0, 5, jumlah_data)
)

# Membatasi jumlah penjualan agar tidak melebihi stok
jumlah_terjual = np.clip(
    np.round(jumlah_terjual),
    1,
    stok_awal
).astype(int)

# Membuat tabel data
data = pd.DataFrame({
    "tanggal": tanggal,
    "produk": produk,
    "harga": harga,
    "hari": hari,
    "promo": promo,
    "cuaca": cuaca,
    "stok_awal": stok_awal,
    "jumlah_terjual": jumlah_terjual
})

# Menyimpan dataset ke folder data
data.to_csv(
    "data/penjualan_cireng.csv",
    index=False
)

# Menampilkan informasi
print("Dataset berhasil dibuat!")
print(f"Jumlah data: {len(data)}")
print("\n5 data pertama:")
print(data.head())