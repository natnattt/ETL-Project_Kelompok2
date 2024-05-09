import pandas as pd
from sqlalchemy import create_engine

user      = 'postgres'
password  = 'postgres'
hostname  = '127.0.0.1'
database  = 'postgres'
port      = '5436'
conn_string = f'postgresql://{user}:{password}@{hostname}:{port}/{database}'
engine      = create_engine(conn_string)
conn        = engine.connect()

# Contoh 1: Import data CSV
df = pd.read_csv('https://raw.githubusercontent.com/natnattt/ETL-Project/main/database/final_dataset.csv')

# Memuat data dari URL ke dalam DataFrame
df = pd.read_csv(url)

# Transform: Mengganti kolom 'BMIcase' dengan format normal
df['BMIcase'] = df['BMIcase'].str.capitalize()

# Transform: Melakukan pembulatan tanpa koma pada kolom 'Weight', 'Height', dan 'BMI' dan menambahkan 'kg' dan 'm'
df['Weight'] = df['Weight'].round().astype(int).astype(str) + ' kg'
df['Height'] = df['Height'].round().astype(int).astype(str) + ' m'
df['BMI'] = df['BMI'].round(0).astype(int)

# Load ke SQL
df.to_sql("database",engine, if_exists='replace')

# Contoh 2: Mengambil data dari database menjadi dataframe 
query   = "SELECT * FROM pet"
df_read = pd.read_sql(query,engine)
df_read.head()
