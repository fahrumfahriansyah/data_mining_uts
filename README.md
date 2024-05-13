# Data Operations

### Deskripsi

File ini berisi definisi data perusahaan dan karyawan beserta fungsi-fungsi yang terkait dengan pengolahan data.

### Data

Data perusahaan dan karyawan didefinisikan dalam struktur data Python, termasuk nama perusahaan, detail klien, dan detail karyawan.

### Fungsi-Fungsi

1. `sort_company()`: Mendapatkan daftar semua perusahaan dan mengurutkannya berdasarkan domain perusahaan secara terbalik.
2. `get_company_domain()`: Mencetak nilai domain dalam setiap perusahaan bersama dengan jumlah klien.
3. `get_employees()`: Mengembalikan daftar karyawan beserta domain perusahaan tempat mereka bekerja.
4. `get_employees_by_company()`: Mengembalikan daftar perusahaan beserta daftar karyawan yang bekerja di setiap perusahaan.




# Preprocessing Data Start-up

## Deskripsi
Repo ini berisi skrip Python untuk melakukan preprocessing data pada dataset start-up. Preprocessing ini mencakup identifikasi dan pengisian nilai-nilai kosong (NaN), one-hot encoding untuk kolom State, perhitungan kolom baru Tax, dan penskalaan fitur menggunakan StandardScaler.

## Cara Penggunaan
1. Pastikan Python dan semua library yang diperlukan telah terinstal di lingkungan Anda.
2. Unduh dataset "50_Startups.csv" dan simpan dalam folder yang sama dengan skrip Python.
3. Jalankan skrip `preprocess_startup_data.py` dengan perintah `python preprocess_startup_data.py`.
4. Hasil pre-processing akan ditampilkan di konsol dan disimpan dalam file CSV baru bernama `preprocessed_startup_data.csv`.

## Penjelasan Kode
- `import pandas as pd`: Mengimpor library pandas untuk manipulasi data.
- `from sklearn.preprocessing import OneHotEncoder, StandardScaler`: Mengimpor class OneHotEncoder dan StandardScaler dari library scikit-learn untuk preprocessing.
- `from sklearn.impute import SimpleImputer`: Mengimpor class SimpleImputer dari scikit-learn untuk mengisi nilai kosong.
- `data_startup = pd.read_csv('50_Startups.csv', delimiter='\t')`: Membaca dataset dari file CSV menggunakan pandas, dengan menggunakan tab sebagai delimiter.
- `fields_with_nan = data_startup.columns[data_startup.isna().any()].tolist()`: Mengidentifikasi kolom-kolom yang memiliki nilai kosong (NaN).
- `imputer = SimpleImputer(strategy='mean')`: Membuat objek imputer untuk mengisi nilai kosong dengan nilai rata-rata.
- `data_startup[fields_with_nan] = imputer.fit_transform(data_startup[fields_with_nan])`: Mengisi nilai kosong dengan nilai rata-rata menggunakan metode fit_transform dari imputer.
- `encoder = OneHotEncoder()`: Membuat objek encoder untuk melakukan one-hot encoding.
- `state_encoded = encoder.fit_transform(data_startup[['State']])`: Melakukan one-hot encoding pada kolom State.
- `data_startup['Tax'] = (data_startup['Profit'] + data_startup['Marketing Spend'] + data_startup['Administration']) * 0.05`: Membuat kolom baru Tax yang dihitung sebagai 5% dari total Profit, Marketing Spend, dan Administration.
- `scaler = StandardScaler()`: Membuat objek scaler untuk melakukan penskalaan fitur.
- `data_startup[['R&D Spend', 'Administration', 'Marketing Spend', 'Profit', 'Tax']] = scaler.fit_transform(data_startup[['R&D Spend', 'Administration', 'Marketing Spend', 'Profit', 'Tax']])`: Melakukan penskalaan fitur menggunakan metode fit_transform dari scaler.
- `data_startup.to_csv('preprocessed_startup_data.csv', index=False)`: Menyimpan hasil pre-processing ke dalam file CSV baru bernama 'preprocessed_startup_data.csv' tanpa menyertakan indeks.

---

Anda dapat menyesuaikan penjelasan ini sesuai dengan kebutuhan Anda dan menambahkan informasi tambahan jika diperlukan.


