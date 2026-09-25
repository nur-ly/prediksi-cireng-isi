import pandas as pd

# Membaca dataset
data = pd.read_csv("data/penjualan_cireng.csv")

# Memilih kolom yang akan digunakan
data_model = data[
    [
        "produk",
        "harga",
        "hari",
        "promo",
        "cuaca",
        "stok_awal",
        "jumlah_terjual"
    ]
].copy()

# Mengubah data kategori menjadi angka
data_model = pd.get_dummies(
    data_model,
    columns=["produk", "hari", "cuaca"],
    dtype=int
)

# Memisahkan fitur (X) dan target (y)
X = data_model.drop("jumlah_terjual", axis=1)
y = data_model["jumlah_terjual"]

# Menampilkan hasil persiapan data
print("=== DATA SETELAH PREPARATION ===")
print(data_model.head())

print("\n=== JUMLAH FITUR ===")
print("Jumlah fitur:", X.shape[1])

print("\n=== TARGET ===")
print("Target: jumlah_terjual")