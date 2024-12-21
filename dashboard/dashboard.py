import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Konfigurasi tema Streamlit
st.set_page_config(page_title="Analisis Kualitas Udara Tiantan by Alf-Anas", layout="wide")
sns.set(style='dark')

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("./tiantan_data.csv")

tiantan_data = load_data()

# Konversi kolom datetime ke format datetime
tiantan_data['datetime'] = pd.to_datetime(tiantan_data['datetime'])

# ===================================================== Sidebar =======================================================
st.sidebar.title("Filter Data")
view_options = st.sidebar.selectbox(
    "Pilih Analisis yang Ingin Dilihat",
    [
        "Tren Kualitas Udara - Tahunan",
        "Tren Kualitas Udara - Bulanan",
        "Korelasi Antar Polutan",
        "Korelasi Cuaca dan Kualitas Udara",
        "Distribusi Kategori PM2.5"
    ]
)

# ===================================================== Tren Kualitas Udara =======================================================

if view_options == "Tren Kualitas Udara - Tahunan":
    exclude_columns = ['No', 'month', 'day', 'hour']
    tiantan_data_yearly = tiantan_data.drop(columns=exclude_columns)
    
    st.header("Tren Tahunan Kualitas Udara di Stasiun Tiantan")

    # Plot untuk PM2.5, PM10, SO2, NO2, dan O3
    st.subheader("Tren Polutan (PM2.5, PM10, SO2, NO2, O3)")
    fig, ax = plt.subplots(figsize=(10, 6))
    columns_to_plot = ['PM2.5', 'PM10', 'SO2', 'NO2', 'O3']
    for col in columns_to_plot:
        sns.lineplot(x='year', y=col, data=tiantan_data_yearly, label=col, ax=ax)
    ax.set_xlabel("Year")
    ax.set_ylabel("Konsentrasi (µg/m³)")
    ax.set_title("Trend Tahunan Polusi Udara")
    ax.legend()
    st.pyplot(fig)

    # Plot untuk CO
    st.subheader("Tren Polutan CO")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x='year', y='CO', data=tiantan_data_yearly, label='CO', color='red', ax=ax)
    ax.set_xlabel("Year")
    ax.set_ylabel("Konsentrasi (mg/m³)")
    ax.set_title("Trend Tahunan Polusi Udara CO")
    ax.legend()
    st.pyplot(fig)

# ===================================================== Tren Bulanan =======================================================
elif view_options == "Tren Kualitas Udara - Bulanan":
    exclude_columns = ['No', 'year', 'day', 'hour']
    tiantan_data_monthly = tiantan_data.drop(columns=exclude_columns)
    tiantan_data_monthly_avg = tiantan_data_monthly.groupby("month").mean(numeric_only=True)

    st.header("Tren Bulanan Kualitas Udara di Stasiun Tiantan")

    # Plot untuk PM2.5, PM10, SO2, NO2, dan O3
    st.subheader("Tren Polutan (PM2.5, PM10, SO2, NO2, O3)")
    fig, ax = plt.subplots(figsize=(12, 6))
    for col in ['PM2.5', 'PM10', 'SO2', 'NO2', 'O3']:
        sns.lineplot(x='month', y=col, data=tiantan_data_monthly_avg, label=col, ax=ax)
    ax.set_xticks(range(1, 13))
    ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    ax.set_xlabel("Month")
    ax.set_ylabel("Konsentrasi (µg/m³)")
    ax.set_title("Trend Bulanan Polusi Udara")
    ax.legend()
    st.pyplot(fig)

    # Plot untuk CO
    st.subheader("Tren Polutan CO")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(x='month', y='CO', data=tiantan_data_monthly_avg, label='CO', color='red', ax=ax)
    ax.set_xticks(range(1, 13))
    ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    ax.set_xlabel("Month")
    ax.set_ylabel("Konsentrasi (mg/m³)")
    ax.set_title("Trend Bulanan Polusi Udara CO")
    ax.legend()
    st.pyplot(fig)

# ===================================================== Korelasi Antar Polutan =======================================================
elif view_options == "Korelasi Antar Polutan":
    st.header("Korelasi Antar Polutan di Stasiun Tiantan")
    pollutants = tiantan_data[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']]
    correlation_matrix = pollutants.corr(method='pearson')

    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", vmin=-1, vmax=1, ax=ax)
    ax.set_title("Korelasi Antar Polutan")
    st.pyplot(fig)

# ===================================================== Korelasi Cuaca dan Kualitas Udara =======================================================
elif view_options == "Korelasi Cuaca dan Kualitas Udara":
    st.header("Korelasi antara Cuaca dan Kualitas Udara di Stasiun Tiantan")
    pollutants_weather = tiantan_data[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'TEMP', 'PRES', 'DEWP', 'RAIN', 'WSPM']]
    correlation_matrix_weather = pollutants_weather.corr(method='pearson')

    fig, ax = plt.subplots(figsize=(12, 8))
    sns.heatmap(correlation_matrix_weather, annot=True, cmap='coolwarm', fmt=".2f", vmin=-1, vmax=1, ax=ax)
    ax.set_title("Korelasi Cuaca dan Kualitas Udara")
    st.pyplot(fig)

# ===================================================== Distribusi Kategori PM2.5 =======================================================
elif view_options == "Distribusi Kategori PM2.5":
    st.header("Distribusi Kategori PM2.5 berdasarkan EPA Airwatch")

    # Kategori PM2.5
    def pm25_category(value):
        if value < 25:
            return 'Good'
        elif 25 <= value <= 50:
            return 'Fair'
        elif 51 <= value <= 100:
            return 'Poor'
        elif 101 <= value <= 300:
            return 'Very Poor'
        else:
            return 'Extremely Poor'

    tiantan_data['PM2.5_Category'] = tiantan_data['PM2.5'].apply(pm25_category)

    # Plot distribusi kategori
    st.subheader("Distribusi Kategori PM2.5")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(data=tiantan_data, x='PM2.5_Category', order=['Good', 'Fair', 'Poor', 'Very Poor', 'Extremely Poor'], palette='coolwarm', ax=ax)
    ax.set_title("Distribusi PM2.5 Berdasarkan Kategori")
    ax.set_xlabel("Kategori PM2.5")
    ax.set_ylabel("Frekuensi")
    st.pyplot(fig)
