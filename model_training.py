import pandas as pd
from sklearn.model_selection import train_test_split

# Membaca dataset
data = pd.read_csv("data/penjualan_cireng.csv")

# Mengubah data kategori menjadi angka
data_model = pd.get_dummies(
    data[
        [
            "produk",
            "harga",
            "hari",
            "promo",
            "cuaca",
            "stok_awal",
            "jumlah_terjual"
        ]
    ],
    columns=["produk", "hari", "cuaca"],
    dtype=int
)

# Memisahkan fitur (X) dan target (y)
X = data_model.drop("jumlah_terjual", axis=1)
y = data_model["jumlah_terjual"]

# Membagi data menjadi 80% training dan 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Menampilkan hasil pembagian data
print("=== HASIL TRAIN TEST SPLIT ===")
print("Jumlah data keseluruhan :", len(data))
print("Data training          :", len(X_train))
print("Data testing           :", len(X_test))
print("Jumlah fitur           :", X_train.shape[1])
# ==========================================
# MODELING - RANDOM FOREST REGRESSOR
# ==========================================

from sklearn.ensemble import RandomForestRegressor

# Membuat model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# Melatih model menggunakan data training
model.fit(X_train, y_train)

print("\n=== MODELING SELESAI ===")
print("Model Random Forest berhasil dilatih.")
# ==========================================
# EVALUASI MODEL
# ==========================================

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# Melakukan prediksi pada data testing
y_pred = model.predict(X_test)

# Menghitung nilai evaluasi
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("\n=== HASIL EVALUASI MODEL ===")
print("MAE  :", round(mae, 2))
print("RMSE :", round(rmse, 2))
print("R²   :", round(r2, 2))
# ==========================================
# MENYIMPAN MODEL
# ==========================================

import joblib

# Menyimpan model dan nama fitur
model_data = {
    "model": model,
    "features": X.columns.tolist()
}

joblib.dump(model_data, "model/model_cireng isi.pkl")

print("\n=== MODEL DISIMPAN ===")
print("Model berhasil disimpan ke folder model.")