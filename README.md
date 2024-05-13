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


# Preprocess Startup Data

### Cara Penggunaan

1. Pastikan Anda memiliki Python dan library yang diperlukan terinstal di lingkungan Anda.
    - Instalasi Pandas:
        ```bash
        pip install pandas
        ```
    - Instalasi scikit-learn:
        ```bash
        pip install scikit-learn
        ```

2. Download file `50_Startups.csv` dan pastikan file tersebut berada dalam direktori yang sama dengan `preprocess_startup_data.py`.

3. Jalankan skrip `preprocess_startup_data.py` menggunakan Python:
    ```bash
    python preprocess_startup_data.py
    ```

### Deskripsi

Skrip ini digunakan untuk melakukan pra-pemrosesan data pada file `50_Startups.csv`. Langkah-langkah yang dilakukan antara lain:

1. Pembacaan dataset menggunakan Pandas.
2. Penanganan data yang kosong (NaN) dengan menggantinya menggunakan nilai mean.
3. Penerapan OneHotEncoder untuk kolom 'State' dan penghapusan kolom 'State' asli.
4. Pembuatan field baru yaitu 'Tax' yang dihitung berdasarkan rumus yang diberikan.
5. Penskalaan data menggunakan StandardScaler.
6. Tampilan beberapa contoh data setelah pra-pemrosesan.
7. Penyimpanan data yang telah diproses ke dalam file CSV dengan nama `preprocessed_startup_data.csv`.


