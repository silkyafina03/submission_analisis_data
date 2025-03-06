import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
@st.cache_data
def load_data():
    data = pd.read_csv('Dashboard/all_data.csv')  # Pastikan path sesuai
    data["dteday"] = pd.to_datetime(data["dteday"])
    return data

data = load_data()

# Sidebar: Filter Tanggal
st.sidebar.image("Dashboard/logo.png", width=150)  # Tambahkan logo (opsional)
st.sidebar.header("Filter Rentang Waktu")
start_date = st.sidebar.date_input("Start Date", data["dteday"].min())
end_date = st.sidebar.date_input("End Date", data["dteday"].max())

# Filter Data
filtered_data = data[(data["dteday"] >= pd.Timestamp(start_date)) & (data["dteday"] <= pd.Timestamp(end_date))]

# Header
st.title("Dashboard Penyewaan Sepeda 🚴‍♂️")

# Metrics (KPI)
col1, col2, col3 = st.columns(3)
col1.metric("Total Penyewaan", filtered_data["cnt"].sum())
col2.metric("Penyewaan Rata-rata", round(filtered_data["cnt"].mean(), 2))
col3.metric("Hari dengan Penyewaan Tertinggi", str(filtered_data.loc[filtered_data["cnt"].idxmax(), "dteday"].date()))


# Visualisasi Penyewaan Sepeda dengan Bar Chart
st.header("Tren Penyewaan Sepeda 📊")
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(filtered_data["dteday"], filtered_data["cnt"], color='skyblue')
ax.set_xlabel("Tanggal")
ax.set_ylabel("Jumlah Penyewaan")
ax.set_title("Tren Penyewaan Sepeda")
plt.xticks(rotation=45)
st.pyplot(fig)

# **Pengaruh Weekday, Working Day, dan Holiday terhadap Penyewaan Sepeda**
st.header("Pengaruh Weekday, Working Day, dan Holiday terhadap Penyewaan Sepeda 📅🚴‍♂️")

# **1. Jumlah Penyewaan: Hari Kerja vs Akhir Pekan**
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x='workingday', y='cnt', data=filtered_data, estimator=sum, ci=None, ax=ax)
ax.set_title("Jumlah Penyewaan Sepeda: Hari Kerja vs Akhir Pekan")
ax.set_xlabel("Hari Kerja (0 = Libur, 1 = Kerja)")
ax.set_ylabel("Total Jumlah Penyewaan")
st.pyplot(fig)

# **2. Jumlah Penyewaan Berdasarkan Hari dalam Seminggu**
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x='weekday', y='cnt', data=filtered_data, estimator=sum, palette="viridis", ax=ax)
ax.set_title("Jumlah Penyewaan Sepeda Berdasarkan Hari dalam Seminggu")
ax.set_xlabel("Hari dalam Seminggu (0 = Minggu, 6 = Sabtu)")
ax.set_ylabel("Total Penyewaan")
st.pyplot(fig)

#  Scatter plot: Rata-rata Penyewaan Berdasarkan Faktor Cuaca
st.header("Pengaruh Cuaca terhadap Penyewaan Sepeda🌞🚴‍♂️")

# Scatter plot: Hubungan Suhu dengan Penyewaan Sepeda
st.subheader("Hubungan Suhu dengan Jumlah Penyewaan Sepeda")
fig, ax = plt.subplots(figsize=(10, 5))
sns.scatterplot(x=filtered_data['temp'], y=filtered_data['cnt'], alpha=0.5, ax=ax)
ax.set_xlabel("Suhu")
ax.set_ylabel("Jumlah Penyewaan")
ax.set_title("Hubungan Suhu dengan Jumlah Penyewaan Sepeda")
st.pyplot(fig)


# **2.2: Pengaruh Kelembapan terhadap Penyewaan**
st.subheader("Hubungan Kelembapan dengan Jumlah Penyewaan Sepeda")
fig, ax = plt.subplots(figsize=(10, 5))
sns.scatterplot(x=filtered_data['hum'], y=filtered_data['cnt'], alpha=0.5, ax=ax)
ax.set_xlabel("Kelembapan")
ax.set_ylabel("Jumlah Penyewaan")
ax.set_title("Hubungan Kelembapan dengan Jumlah Penyewaan Sepeda")
st.pyplot(fig)

# **2.3: Pengaruh Kecepatan Angin terhadap Penyewaan**
st.subheader("Hubungan Kecepatan Angin dengan Jumlah Penyewaan Sepeda")
fig, ax = plt.subplots(figsize=(10, 5))
sns.scatterplot(x=filtered_data['temp'], y=filtered_data['cnt'], alpha=0.5, ax=ax)
ax.set_xlabel("Kecepatan Angin")
ax.set_ylabel("Jumlah Penyewaan")
ax.set_title("Hubungan Kecepatan Angin dengan Jumlah Penyewaan Sepeda")
st.pyplot(fig)

# **Tambahan: Tabel Data**
st.subheader("Data Penyewaan Sepeda")
st.dataframe(filtered_data)
