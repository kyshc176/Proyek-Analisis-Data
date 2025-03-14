import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Load dataset
day_df = pd.read_csv("/Data/day.csv")
hour_df = pd.read_csv("/Data/hour.csv")

### Assessing Data
print(day_df.info())
print(day_df.describe())
print(hour_df.info())
print(hour_df.describe())

### Cleaning Data
# Menghapus duplikasi
day_df.drop_duplicates(inplace=True)
hour_df.drop_duplicates(inplace=True)

# Mengecek missing values
print(day_df.isnull().sum())
print(hour_df.isnull().sum())

## Exploratory Data Analysis (EDA)

### Melihat statistik deskriptif
print(day_df.describe())

# Melihat distribusi jumlah peminjaman sepeda
print("Distribusi jumlah peminjaman sepeda:")
print(day_df['cnt'].describe())

# Analisis Pengaruh Cuaca
print("Rata-rata jumlah peminjaman berdasarkan kondisi cuaca:")
print(day_df.groupby('weathersit')['cnt'].mean())

# Analisis Hari Kerja vs Akhir Pekan
print("Rata-rata jumlah peminjaman pada hari kerja dan akhir pekan:")
print(day_df.groupby('workingday')['cnt'].mean())

## Visualization & Explanatory Analysis
# Streamlit Dashboard
st.title("Dashboard Analisis Peminjaman Sepeda")

# Statistik Dasar
st.subheader("Statistik Dasar")
st.write(day_df.describe())

# Visualisasi Pengaruh Cuaca terhadap Peminjaman Sepeda
st.subheader("Total Peminjaman Sepeda berdasarkan Kondisi Cuaca")
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x='weathersit', y='cnt', data=day_df, estimator=sum, ci=None, palette='Blues', ax=ax)
ax.set_xlabel("Kondisi Cuaca")
ax.set_ylabel("Total Peminjaman")
st.pyplot(fig)

# Visualisasi Peminjaman Sepeda pada Hari Kerja vs Akhir Pekan
st.subheader("Distribusi Peminjaman Sepeda pada Hari Kerja dan Akhir Pekan")
fig, ax = plt.subplots(figsize=(10, 5))
sns.histplot(data=day_df, x='cnt', hue='workingday', kde=True, bins=30, palette='coolwarm', ax=ax)
ax.set_xlabel("Jumlah Peminjaman")
ax.set_ylabel("Frekuensi")
st.pyplot(fig)

# if day is neither weekend nor holiday is 1, otherwise is 0.
