import pandas as pd

# Membaca dataset
data = pd.read_csv("data/penjualan_cireng.csv")

# Menampilkan 5 data pertama
print("=== 5 DATA PERTAMA ===")
print(data.head())

# Menampilkan informasi dataset
print("\n=== INFORMASI DATASET ===")
print(data.info())

# Menampilkan jumlah baris dan kolom
print("\n=== UKURAN DATASET ===")
print("Jumlah baris:", data.shape[0])
print("Jumlah kolom:", data.shape[1])
# Mengecek data kosong
print("\n=== DATA KOSONG ===")
print(data.isnull().sum())

# Mengecek data duplikat
print("\n=== DATA DUPLIKAT ===")
print("Jumlah data duplikat:", data.duplicated().sum())
# Statistik data numerik
print("\n=== STATISTIK DATA ===")
print(data.describe())