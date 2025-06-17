import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Load dataset
day_df = pd.read_csv("/Users/tika/Documents/CC DICODING/Proyek Analisis Data/Data/day.csv")

### Cleaning Data
# Menghapus duplikasi
day_df.drop_duplicates(inplace=True)

# Mengecek missing values
missing_values = day_df.isnull().sum()

## Streamlit Dashboard
st.title("Dashboard Analisis Peminjaman Sepeda")

# Statistik Dasar
st.subheader("Statistik Dasar")
st.write(day_df.describe())

# Menampilkan jumlah missing values
st.subheader("Missing Values")
st.write(missing_values)

## === Fitur Interaktif === ##
st.sidebar.header("Filter Data")

# Filter berdasarkan musim (season)
season_options = {
    1: "Spring",
    2: "Summer",
    3: "Fall",
    4: "Winter"
}
selected_season = st.sidebar.selectbox("Pilih Musim:", options=list(season_options.keys()), format_func=lambda x: season_options[x])

# Filter berdasarkan cuaca (weathersit)
weather_options = {
    1: "Clear, Few clouds, Partly cloudy",
    2: "Mist + Cloudy / Broken clouds / Few clouds / Mist",
    3: "Light Snow, Light Rain + Thunderstorm + Scattered clouds",
    4: "Heavy Rain + Ice Pellets + Thunderstorm + Mist, Snow + Fog"
}
selected_weather = st.sidebar.multiselect("Pilih Kondisi Cuaca:", options=list(weather_options.keys()), format_func=lambda x: weather_options[x])

# Filter berdasarkan hari kerja atau akhir pekan
workingday_options = {
    1: "Hari Kerja (Bukan Akhir Pekan atau Libur)",
    0: "Akhir Pekan atau Hari Libur"
}
selected_workingday = st.sidebar.radio("Pilih Jenis Hari:", options=list(workingday_options.keys()), format_func=lambda x: workingday_options[x])

# Filter dataset berdasarkan pilihan pengguna
filtered_df = day_df[(day_df["season"] == selected_season) & (day_df["workingday"] == selected_workingday)]

# Jika pengguna memilih lebih dari satu kondisi cuaca, lakukan filter
if selected_weather:
    filtered_df = filtered_df[filtered_df["weathersit"].isin(selected_weather)]

# Tampilkan data yang sudah difilter
st.subheader("Data Setelah Difilter")
st.write(filtered_df)

# Visualisasi Total Peminjaman Sepeda Berdasarkan Kondisi Cuaca
st.subheader("Total Peminjaman Sepeda berdasarkan Kondisi Cuaca")

fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(
    x='weathersit',
    y='cnt',
    data=filtered_df,
    estimator=sum,
    ci=None,
    palette='Blues',
    ax=ax
)
ax.set_xlabel("Kondisi Cuaca")
ax.set_ylabel("Total Peminjaman")

# Menambahkan keterangan di bawah grafik
deskripsi_cuaca = """
**Keterangan Kondisi Cuaca:**
- **1**: Clear, Few clouds, Partly cloudy, Partly cloudy  
- **2**: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist  
- **3**: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds  
"""

st.pyplot(fig)
st.markdown(deskripsi_cuaca)

# Visualisasi Peminjaman Sepeda pada Hari Kerja vs Akhir Pekan
st.subheader("Distribusi Peminjaman Sepeda pada Hari Kerja dan Akhir Pekan")
fig, ax = plt.subplots(figsize=(10, 5))
sns.histplot(data=filtered_df, x='cnt', kde=True, bins=30, palette='coolwarm', ax=ax)
ax.set_xlabel("Jumlah Peminjaman")
ax.set_ylabel("Frekuensi")
st.pyplot(fig)
