

import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
day_df = pd.read_csv("/content/day.csv")
hour_df = pd.read_csv("/content/hour.csv")

### Assessing Data
print(day_df.info())
print(day_df.describe())
print(hour_df.info())
print(hour_df.describe())


### Cleaning Data

# - Cek missing values dan duplikasi
day_df.drop_duplicates(inplace=True)
hour_df.drop_duplicates(inplace=True)

# - Cek missing values
print(day_df.isnull().sum())
print(hour_df.isnull().sum())

## Exploratory Data Analysis (EDA)

### Explore

# Melihat statistik deskriptif
display(day_df.describe())

# Melihat distribusi jumlah peminjaman sepeda
print("Distribusi jumlah peminjaman sepeda:")
display(day_df['cnt'].describe())

# Analisis Pengaruh Cuaca
print("Rata-rata jumlah peminjaman berdasarkan kondisi cuaca:")
display(day_df.groupby('weathersit')['cnt'].mean())

# Analisis Hari Kerja vs Akhir Pekan
print("Rata-rata jumlah peminjaman pada hari kerja dan akhir pekan:")
display(day_df.groupby('workingday')['cnt'].mean())
#if day is neither weekend or holiday is 1, otherwise is 0.

## Visualization & Explanatory Analysis

### Pertanyaan 1: Bagaimana pengaruh Cuaca terhadap Peminjaman Sepeda?

plt.figure(figsize=(10, 5))
sns.barplot(x='weathersit', y='cnt', data=day_df, estimator=sum, ci=None, palette='Blues')
plt.title('Total Peminjaman Sepeda berdasarkan Kondisi Cuaca')
plt.xlabel('Kondisi Cuaca')
plt.ylabel('Total Peminjaman')
plt.grid(True)
plt.show()

## Pertanyaan 2: Bagaiaman perbandingan Peminjaman Sepeda antara Hari Kerja dan Akhir Pekan?"""

plt.figure(figsize=(10, 5))
sns.histplot(data=day_df, x='cnt', hue='workingday', kde=True, bins=30, palette='coolwarm')
plt.title('Distribusi Peminjaman Sepeda pada Hari Kerja dan Akhir Pekan')
plt.xlabel('Jumlah Peminjaman')
plt.ylabel('Frekuensi')
plt.grid(True)
plt.show()
# if day is neither weekend nor holiday is 1, otherwise is 0.
