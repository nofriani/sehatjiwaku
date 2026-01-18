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
# CUSTOM STYLE
# =====================
st.markdown("""
<style>
body {
    background-color: #f2fbf9;
}
.hero {
    background: linear-gradient(120deg, #2aa198, #6cdbd1);
    padding: 60px;
    border-radius: 25px;
    color: white;
    text-align: center;
    margin-bottom: 40px;
}
.hero h1 {
    font-size: 52px;
    font-weight: 900;
}
.hero p {
    font-size: 20px;
}
.card {
    background: white;
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 8px 18px rgba(0,0,0,0.08);
    margin-bottom: 30px;
}
.section-title {
    color: #2aa198;
    font-size: 28px;
    font-weight: 800;
}
.badge {
    display: inline-block;
    background: #e6f7f5;
    color: #2aa198;
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 13px;
    margin-bottom: 10px;
}
.footer {
    text-align: center;
    color: #777;
    margin-top: 50px;
}
</style>
""", unsafe_allow_html=True)

# =====================
# SIDEBAR
# =====================
st.sidebar.title("🧠 SehatJiwa")
menu = st.sidebar.radio(
    "Navigasi",
    ["Beranda", "Artikel Edukasi", "Video Edukasi", "Tes Mental", "Dukungan"]
)

# =====================
# BERANDA
# =====================
if menu == "Beranda":
    st.markdown("""
    <div class="hero">
        <h1>SehatJiwa</h1>
        <p>Website Edukasi Kesehatan Mental Berbasis Pemuda<br>
        Akurat • Komprehensif • Inklusif</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <span class="badge">Tentang SehatJiwa</span>
        <p>
        <b>SehatJiwa</b> merupakan website edukasi kesehatan mental yang dikembangkan oleh pemuda
        sebagai media digital yang bertujuan meningkatkan literasi kesehatan mental masyarakat.
        </p>
        <p>
        Website ini menyajikan edukasi yang <b>mudah dipahami, berbasis bukti ilmiah, dan ramah pengguna</b>,
        sehingga dapat digunakan oleh berbagai kelompok masyarakat tanpa hambatan teknis.
        </p>
    </div>
    """, unsafe_allow_html=True)

# =====================
# ARTIKEL EDUKASI
# =====================
elif menu == "Artikel Edukasi":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📖 Artikel Edukasi Kesehatan Mental</div>', unsafe_allow_html=True)

    with st.expander("🧠 Kesehatan Mental: Pengertian dan Pentingnya"):
        st.write("""
        Kesehatan mental adalah kondisi kesejahteraan di mana individu mampu mengenali potensi dirinya,
        mengelola tekanan hidup, bekerja secara produktif, serta berkontribusi di lingkungan sosial.

        Menjaga kesehatan mental sangat penting karena gangguan mental dapat memengaruhi kualitas hidup,
        hubungan sosial, prestasi akademik, dan produktivitas kerja. Sama seperti kesehatan fisik,
        kesehatan mental perlu dijaga secara berkelanjutan.
        """)

    with st.expander("😔 Depresi: Lebih dari Sekadar Sedih"):
        st.write("""
        Depresi bukan sekadar perasaan sedih sementara, melainkan kondisi kesehatan mental yang ditandai
        dengan perasaan hampa berkepanjangan, kehilangan minat, kelelahan, serta gangguan tidur dan konsentrasi.

        Depresi dapat dialami siapa saja dan bukan tanda kelemahan. Dengan edukasi yang tepat dan dukungan
        profesional, kondisi ini dapat dikelola.
        """)

    with st.expander("😟 Kecemasan dan Dampaknya"):
        st.write("""
        Kecemasan adalah respons alami terhadap stres, namun kecemasan berlebihan dapat mengganggu aktivitas
        sehari-hari. Gejalanya meliputi rasa khawatir berlebihan, jantung berdebar, dan sulit berkonsentrasi.

        Mengelola kecemasan dapat dilakukan melalui teknik relaksasi, manajemen waktu, dan bantuan profesional
        bila diperlukan.
        """)

    with st.expander("🌱 Strategi Mengelola Stres dan Emosi"):
        st.write("""
        Beberapa strategi sederhana untuk menjaga kesehatan mental:
        - Mengatur waktu istirahat dan tidur yang cukup
        - Melakukan aktivitas fisik ringan
        - Membatasi penggunaan media sosial
        - Berbicara dengan orang terpercaya
        - Melatih mindfulness dan pernapasan
        """)

    with st.expander("🧩 Kapan Harus Mencari Bantuan Profesional?"):
        st.write("""
        Bantuan profesional perlu dipertimbangkan ketika stres, kecemasan, atau kesedihan
        berlangsung lama dan mulai mengganggu aktivitas sehari-hari.

        Mencari bantuan bukan tanda kegagalan, melainkan langkah berani untuk menjaga kesehatan jiwa.
        """)

    st.markdown("</div>", unsafe_allow_html=True)

# =====================
# VIDEO EDUKASI
# =====================
elif menu == "Video Edukasi":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🎥 Video Edukasi</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Mengapa Kesehatan Mental Penting?")
        st.video("https://www.youtube.com/watch?v=oxx564hMBUI")

    with col2:
        st.subheader("Cara Mengelola Stres Sehari-hari")
        st.video("https://www.youtube.com/watch?v=hnpQrMqDoqE")

    st.markdown("</div>", unsafe_allow_html=True)

# =====================
# TES MENTAL
# =====================
elif menu == "Tes Mental":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📝 Tes Kesehatan Mental (Refleksi)</div>', unsafe_allow_html=True)

    st.warning("Tes ini bukan diagnosis medis.")

    q1 = st.slider("Saya merasa cemas atau tertekan", 0, 3, 1)
    q2 = st.slider("Saya kehilangan minat pada aktivitas sehari-hari", 0, 3, 1)
    q3 = st.slider("Saya merasa kelelahan secara emosional", 0, 3, 1)

    if st.button("Lihat Hasil"):
        total = q1 + q2 + q3
        if total <= 2:
            st.success("Kondisi mental relatif baik. Tetap jaga kesehatan jiwa 💚")
        elif total <= 6:
            st.warning("Kamu mungkin sedang mengalami tekanan. Lakukan self-care.")
        else:
            st.error("Kamu membutuhkan dukungan lebih lanjut.")

    st.markdown("</div>", unsafe_allow_html=True)

# =====================
# DUKUNGAN
# =====================
elif menu == "Dukungan":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🤝 Dukungan & Rujukan</div>', unsafe_allow_html=True)

    st.write("""
    SehatJiwa menyediakan informasi rujukan sebagai bentuk dukungan kesehatan mental:
    - Konselor sekolah
    - Psikolog dan konselor profesional
    - Fasilitas layanan kesehatan terdekat
    """)

    st.info("Jika kondisi darurat, segera hubungi layanan kesehatan terdekat.")
    st.markdown("</div>", unsafe_allow_html=True)

# =====================
# FOOTER
# =====================
st.markdown('<div class="footer">© 2026 SehatJiwa | Youth-Led Mental Health Education</div>', unsafe_allow_html=True)
