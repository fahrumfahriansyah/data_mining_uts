import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# Baca dataset
data_startup = pd.read_csv('50_Startups.csv')

# Lakukan analisis mengenai field yang memiliki data kosong (NaN) dan isi dengan nilai mean
nan_columns = data_startup.columns[data_startup.isna().any()].tolist()
imputer = SimpleImputer(strategy='mean')
data_startup[nan_columns] = imputer.fit_transform(data_startup[nan_columns])

# Lakukan OneHotEncoder ke field 'State'
state_encoded = pd.get_dummies(data_startup['State'], drop_first=True)
data_startup = pd.concat([data_startup, state_encoded], axis=1)
data_startup.drop(columns=['State'], inplace=True)

# Buat field baru yaitu Tax
data_startup['Tax'] = (data_startup['Profit'] + data_startup['Marketing Spend'] + data_startup['Administration']) * 0.05

# Jalankan StandardScaler untuk field-field tersebut
scaler = StandardScaler()
data_startup[['R&D Spend', 'Administration', 'Marketing Spend', 'Profit', 'Tax']] = scaler.fit_transform(data_startup[['R&D Spend', 'Administration', 'Marketing Spend', 'Profit', 'Tax']])

# Tampilkan beberapa contoh data setelah pre-processing
print(data_startup.head())

# Simpan data yang telah diproses ke dalam file CSV jika diperlukan
data_startup.to_csv('preprocessed_startup_data.csv', index=False)
