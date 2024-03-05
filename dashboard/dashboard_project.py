import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

df_concat = pd.read_csv('dashboard\df_concat.csv')

def dfpertanyaan1(data):
    data_hasil = data.groupby(by = ['year'], as_index = False).agg({
        'PM2.5' : 'mean',
        'PM10' : 'mean',
        'SO2' : 'mean',
        'NO2' : 'mean',
        'CO' : 'mean',
        'O3' : 'mean',
    })
    return data_hasil

def dfpertanyaan2(data):
    data_hasil = data.groupby(by = ['month_year'], as_index = False).agg({
        'RAIN': 'mean'
    })
    return data_hasil

df1 = dfpertanyaan1(df_concat)
df2 = dfpertanyaan2(df_concat)

st.header('Dicoding Project (Analisis Air Quality Dataset)')

st.subheader('Bagaimana Konsentrasi Polutan Udara (PM2.5, PM10, CO, SO2, NO2, dan O3) dari 2013 - 2017?')

fig, ax = plt.subplots(figsize=(12,5))
ax.plot(df1['year'], df1['PM10'], label='PM 10', color='orange')
ax.plot(df1['year'], df1['SO2'], label='SO2', color='magenta')
ax.plot(df1['year'], df1['NO2'], label='NO2', color='brown')
ax.plot(df1['year'], df1['O3'], label='O3', color='lightblue')
ax.plot(df1['year'], df1['PM2.5'], label='PM 2.5', color='red')
ax.set_title('Konsentrasi Polutan Udara', size=20)
ax.set_xlabel('Year',size=15)
ax.set_ylabel('Konsentrasi (μg/m³)',size=15)
ax.legend()
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(12,5))
ax.plot(df1['year'], df1['CO'], label='CO', color='red')
ax.set_title('Konsentrasi Polutan Udara', size=20)
ax.set_xlabel('Year',size=15)
ax.set_ylabel('Konsentrasi (μg/m³)',size=15)
ax.legend()
st.pyplot(fig)

st.write(
    """Semua Konsentrasi Polutan Udara menurun dari tahun 2014 sampai awal tahun 2016. setelah awal 2016 hampir semua konsentrasi polutan udara meningkat kecuali O3 (Ozon)"""
)

st.subheader('Bagaimana Perkembangan Curah Hujan per Bulannya?')
fig, ax = plt.subplots(figsize=(12,5))
ax.plot(df2['month_year'], df2['RAIN'], label='Curah Hujan', color='blue')
ax.set_title('Curah Hujan', size=20)
ax.set_xlabel('Month Year',size=15)
ax.set_ylabel('mm/hari',size=15)
ax.tick_params(axis='x', rotation=45, labelsize=8)
ax.legend()
st.pyplot(fig)

st.write(
    """Curah Hujan selalu turun di awal tahun dan meningkat di pertengahan sampai akhir tahun, dan akan turun lagi setelah itu. Namun yang unik adalah terdapat peningkatan dari "peningkatan yang terjadi di pertengahan sampai akhir tahun" dari tahun 2014 sampai 2016."""
)
