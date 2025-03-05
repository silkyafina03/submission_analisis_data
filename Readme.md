🚴‍♂️ Bike Sharing Analysis Dashboard
📊 Analisis Data Penyewaan Sepeda dengan RFM Analysis & Streamlit Dashboard

📌 Deskripsi Proyek
Proyek ini menganalisis data penyewaan sepeda untuk memahami pola penggunaan berdasarkan faktor-faktor seperti hari kerja, libur, dan kondisi cuaca. Selain itu, dilakukan RFM Analysis untuk mengelompokkan pelanggan berdasarkan Recency, Frequency, dan Monetary. Dashboard interaktif dibangun menggunakan Streamlit.

📂 Dataset
Dataset yang digunakan adalah Bike Sharing Dataset dari UCI Machine Learning Repository. Dataset ini berisi informasi jumlah penyewaan sepeda harian beserta faktor-faktor seperti cuaca, suhu, dan hari kerja.

- Nama Dataset: `day_df`
- Kolom Utama:
  - `dteday`: Tanggal transaksi
  - `cnt`: Total penyewaan sepeda
  - `weekday`: Hari dalam seminggu
  - `holiday`: Indikator hari libur
  - `workingday`: Indikator hari kerja
  - `temp`: Suhu rata-rata
  - `hum`: Kelembapan rata-rata
  - `windspeed`: Kecepatan angin rata-rata

📈 Metode Analisis
1. Analisis Exploratory Data Analysis (EDA)
   - Visualisasi tren penyewaan sepeda harian.
   - Korelasi faktor cuaca dengan jumlah penyewaan.
2. RFM Analysis
   - Recency: Seberapa lama sejak penyewaan terakhir.
   - Frequency: Seberapa sering penyewaan terjadi.
   - Monetary: Total penyewaan dalam periode tertentu.
   - Skoring RFM untuk mengelompokkan tipe pengguna.
3. Visualisasi dalam Dashboard
   - Grafik interaktif tren penyewaan sepeda.
   - Heatmap hubungan antara cuaca dan penyewaan.
   - Distribusi skor RFM pengguna.

📌 Author
👩‍💻 Silky Afina Saly
📍 6th-Semester Information Systems Student
💡 Passionate in Data Science & Machine Learning
