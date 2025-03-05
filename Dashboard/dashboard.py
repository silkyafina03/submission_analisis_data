import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
@st.cache_data
def load_data():
    data = pd.read_csv("D:\SUBMISSION ANALISIS DATA\Data\day.csv")  # Pastikan path sesuai
    data["dteday"] = pd.to_datetime(data["dteday"])
    return data

data = load_data()

# Sidebar: Filter Tanggal
st.sidebar.image("D:\SUBMISSION ANALISIS DATA\Dashboard\logo.png", width=150)  # Tambahkan logo (opsional)
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


# Visualisasi Penyewaan Sepeda
st.subheader("Tren Penyewaan Sepeda 📈")
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(filtered_data["dteday"], filtered_data["cnt"], marker='o', linestyle='-')
ax.set_xlabel("Tanggal")
ax.set_ylabel("Jumlah Penyewaan")
ax.set_title("Tren Penyewaan Sepeda")
plt.xticks(rotation=45)
st.pyplot(fig)

# Tambahan: Tabel Data
st.subheader("Data Penyewaan Sepeda")
st.dataframe(filtered_data)


# Hitung Recency (jumlah hari sejak terakhir rental)
max_date = data["dteday"].max()
data["days_since_rental"] = (max_date - data["dteday"]).dt.days

# Hitung Frequency dan Monetary berdasarkan minggu
df_rfm = data.resample('W', on='dteday').agg({
    'cnt': ['sum', 'count']  # 'sum' untuk Monetary, 'count' untuk Frequency
})

# Beri nama ulang kolom
df_rfm.columns = ['Monetary', 'Frequency']
df_rfm = df_rfm.reset_index()

# Recency: Ambil nilai minimum days_since_rental per minggu
df_recency = data.groupby(pd.Grouper(key='dteday', freq='W'))["days_since_rental"].min().reset_index()
df_recency = df_recency.rename(columns={"days_since_rental": "Recency"})

# Gabungkan semua metrik RFM
df_rfm = df_rfm.merge(df_recency, on="dteday")

# Buat skor RFM (pembagian kuantil 1-4)
df_rfm["R_Score"] = df_rfm["Recency"].rank(pct=True).apply(lambda x: int(x * 4) + 1)
df_rfm["F_Score"] = df_rfm["Frequency"].rank(pct=True).apply(lambda x: int(x * 4) + 1)
df_rfm["M_Score"] = df_rfm["Monetary"].rank(pct=True).apply(lambda x: int(x * 4) + 1)

# Gabungkan skor menjadi satu nilai
df_rfm["RFM_Score"] = df_rfm["R_Score"].astype(str) + df_rfm["F_Score"].astype(str) + df_rfm["M_Score"].astype(str)

st.subheader("RFM Analysis")
# Buat layout kolom untuk menampilkan RFM Metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Recency (hari)", df_rfm["Recency"].mean().round(2))

with col2:
    st.metric("Frequency (rata-rata per minggu)", df_rfm["Frequency"].mean().round(2))

with col3:
    st.metric("Monetary (total sewa per minggu)", df_rfm["Monetary"].mean().round(2))

# Tambahkan visualisasi distribusi skor RFM
st.subheader("Distribusi Skor RFM")

# Pie chart untuk distribusi pelanggan berdasarkan RFM Score
rfm_counts = df_rfm["RFM_Score"].value_counts().reset_index()
rfm_counts.columns = ["RFM Score", "Count"]

st.bar_chart(rfm_counts.set_index("RFM Score"))

# Menampilkan tabel hasil segmentasi
st.subheader("Detail RFM Score")
st.dataframe(df_rfm[["dteday", "Recency", "Frequency", "Monetary", "RFM_Score"]])

