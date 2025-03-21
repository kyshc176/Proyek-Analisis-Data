import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Load dataset
day_df = pd.read_csv("Dashboard/day.csv")

# Sidebar Filtering
season_options = ['All Season', 'Spring', 'Summer', 'Fall', 'Winter']
season = st.selectbox("Pilih Musim:", season_options)

work_options = ['All', 'Workday', 'Weekend']
workday = st.selectbox("Pilih Hari Kerja atau Akhir Pekan:", work_options)

# Filtering Data
filtered_df = day_df.copy()
if season != 'All Season':
    season_map = {'Spring': 1, 'Summer': 2, 'Fall': 3, 'Winter': 4}
    filtered_df = filtered_df[filtered_df['season'] == season_map[season]]

if workday != 'All':
    work_map = {'Workday': 1, 'Weekend': 0}
    filtered_df = filtered_df[filtered_df['workingday'] == work_map[workday]]

# Visualisasi: Total Peminjaman Sepeda berdasarkan Kondisi Cuaca
st.subheader("Total Peminjaman Sepeda berdasarkan Kondisi Cuaca")
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x='weathersit', y='cnt', data=filtered_df, estimator=sum, ci=None, palette='Blues', ax=ax)
ax.set_title('Total Peminjaman Sepeda berdasarkan Kondisi Cuaca')
ax.set_xlabel('Kondisi Cuaca')
ax.set_ylabel('Total Peminjaman')
ax.grid(True)
st.pyplot(fig)

# Visualisasi: Distribusi Peminjaman Sepeda pada Hari Kerja dan Akhir Pekan
st.subheader("Distribusi Peminjaman Sepeda pada Hari Kerja dan Akhir Pekan")
fig, ax = plt.subplots(figsize=(10, 5))
workingday_labels = {1: "Workday", 0: "Weekend"}
filtered_df['workingday_label'] = filtered_df['workingday'].map(workingday_labels)
sns.histplot(data=filtered_df, x='cnt', hue='workingday_label', kde=True, bins=30, palette={"Workday": "#1f77b4", "Weekend": "#ff7f0e"}, ax=ax)
ax.set_title('Distribusi Peminjaman Sepeda pada Hari Kerja dan Akhir Pekan')
ax.set_xlabel('Jumlah Peminjaman')
ax.set_ylabel('Frekuensi')
ax.grid(True)
st.pyplot(fig)
