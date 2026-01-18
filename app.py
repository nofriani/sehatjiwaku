import streamlit as st

# =====================
# PAGE CONFIG
# =====================
st.set_page_config(
    page_title="SehatJiwa",
    page_icon="🧠",
    layout="wide"
)

# =====================
# SIDEBAR NAVIGATION
# =====================
st.sidebar.title("🧠 SehatJiwa")
menu = st.sidebar.radio(
    "Navigasi",
    ["Beranda", "Edukasi", "Tes Kesehatan Mental", "Dukungan"]
)

# =====================
# BERANDA
# =====================
if menu == "Beranda":
    st.title("🧠 SehatJiwa")
    st.subheader("Website Edukasi Kesehatan Mental Berbasis Pemuda")

    st.markdown("""
    **SehatJiwa** merupakan website edukasi kesehatan mental yang dikembangkan oleh pemuda
    sebagai media digital yang **akurat, komprehensif, mudah dipahami, dan inklusif**.

    Website ini bertujuan meningkatkan **literasi kesehatan mental** melalui konten edukatif
    yang terstruktur dan ramah pengguna.
    """)

    st.info("💡 Gunakan menu di samping untuk menjelajahi fitur SehatJiwa")

# =====================
# EDUKASI
# =====================
elif menu == "Edukasi":
    st.header("📚 Konten Edukatif & Komprehensif")

    with st.expander("📖 Artikel Edukatif"):
        st.write("""
        Artikel edukatif membahas:
        - Pengertian kesehatan mental  
        - Depresi, kecemasan, dan stres  
        - Pentingnya menjaga kesehatan jiwa  
        """)

    with st.expander("📊 Infografis Interaktif"):
        st.write("""
        Infografis membantu memahami:
        - Faktor risiko kesehatan mental  
        - Tanda awal gangguan mental  
        - Cara menjaga keseimbangan emosi  
        """)

    with st.expander("🎥 Video Edukasi"):
        st.write("""
        Video edukasi singkat yang mudah dipahami untuk meningkatkan
        kesadaran dan pemahaman kesehatan mental.
        """)

# =====================
# TES KESEHATAN MENTAL
# =====================
elif menu == "Tes Kesehatan Mental":
    st.header("📝 Tes Kesehatan Mental (Refleksi Diri)")

    st.warning("⚠️ Tes ini bukan diagnosis medis, hanya refleksi awal.")

    q1 = st.slider("Saya merasa cemas atau tertekan", 0, 3, 1)
    q2 = st.slider("Saya sulit menikmati aktivitas sehari-hari", 0, 3, 1)
    q3 = st.slider("Saya merasa kelelahan secara emosional", 0, 3, 1)

    if st.button("Lihat Hasil"):
        total = q1 + q2 + q3

        if total <= 2:
            st.success("Kondisi mental kamu relatif baik. Tetap jaga kesehatan jiwa 💚")
        elif total <= 6:
            st.warning("Kamu mungkin sedang mengalami tekanan. Luangkan waktu untuk self-care.")
        else:
            st.error("Kamu membutuhkan dukungan lebih lanjut. Jangan ragu mencari bantuan profesional.")

# =====================
# DUKUNGAN
# =====================
elif menu == "Dukungan":
    st.header("🤝 Komunitas & Dukungan")

    st.markdown("""
    SehatJiwa juga berfungsi sebagai **ruang dukungan** dengan menyediakan
    informasi rujukan bantuan profesional.
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.success("🏫 Konselor Sekolah\n\nPendampingan awal bagi pelajar.")

    with col2:
        st.info("🧑‍⚕️ Psikolog & Tenaga Profesional\n\nDukungan kesehatan mental lanjutan.")

    st.markdown("Jika kondisi darurat, segera hubungi layanan kesehatan terdekat.")

# =====================
# FOOTER
# =====================
st.caption("© 2026 SehatJiwa | Youth-Led Mental Health Education")

