# Jalankan aplikasi dengan perintah `streamlit run filename.py`

import streamlit as st
import math
from streamlit_option_menu 
import option_menu
st.set_page_config(page_title="Kalkulator pH", page_icon=":1234:", layout="wide")

# Halaman utama untuk pilihan
with st.sidebar:
    selected = option_menu(
        menu_title = "Menu",
        options = ["Beranda", 
            "Konsentrasi Asam", 
            "Konsentrasi Basa",
            "Massa dan Volume Asam",
            "Massa dan Volume Basa",
            "Tentang Aplikasi"],
        icons = ["house-door", "calculator", "calculator", "calculator", "calculator", "exclamation-circle"],
        styles = {
        "icon": {"font-size": "20px"}, 
        "nav-link": {"font-size": "20px", "text-align": "left", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "green"}}
    )

if selected == "Beranda":
    st.markdown("<h1 style='text-align: center; color: green;'>SELAMAT DATANG</h1>", unsafe_allow_html=True)
    left, mid, right = st.columns(3)
    with mid:
        st.image("D:\kalkulator_ph_larutan\logoapp.gif")    
    st.markdown('---')
    st.markdown('<div style="text-align: center;">Kalkulator pH Larutan adalah alat online gratis yang dirancang untuk memudahkan pengguna dalam menghitung pH suatu larutan. Silakan pilih metode perhitungan yang sesuai, kemudian ikuti perintah yang ditampilkan di layar!</div>', unsafe_allow_html=True)
    st.markdown('---')
    st.markdown('<h2 style="color: green; ">DIBUAT OLEH:</h2>', unsafe_allow_html=True)
    st.write('KELOMPOK 3 (1c - ANALISIS KIMIA)')
    st.write('''
1. Fairuz Zahrany De Shaula    (2360122)
2. Kesya Melia Andriani        (2360156)
3. Reza Imelda                 (2360238) 
4. Riska Maulidya Ainy         (2360242) 
5. Talitha Syahla Kurniawan    (2360275)
''')
    st.markdown('---')
