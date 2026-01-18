import streamlit as st
from datetime import date

# =====================
# PAGE CONFIG
# =====================
st.set_page_config(
    page_title="SehatJiwa",
    layout="wide"
)

# =====================
# STYLE
# =====================
st.markdown("""
<style>
body {
    background-color: #f3f8f8;
}
.hero {
    background-image: url('https://images.unsplash.com/photo-1520975922284-7b958f0f22a0');
    background-size: cover;
    background-position: center;
    padding: 80px;
    border-radius: 20px;
    color: white;
    margin-bottom: 40px;
}
.hero h1 {
    font-size: 52px;
    font-weight: 800;
}
.hero p {
    font-size: 20px;
    max-width: 700px;
}
.card {
    background-color: white;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 6px 14px rgba(0,0,0,0.08);
    margin-bottom: 30px;
}
.article-card {
    border-left: 6px solid #2aa198;
}
.article-meta {
    font-size: 14px;
    color: #666;
    margin-bottom: 10px;
}
.article-title {
    font-size: 24px;
    font-weight: 700;
    color: #073642;
}
.section-title {
    font-size: 30px;
    font-weight: 800;
    color: #2aa198;
    margin-bottom: 20px;
}
.footer {
    text-align: center;
    color: #777;
    margin-top: 60px;
}
</style>
""", unsafe_allow_html=True)

# =====================
# SIDEBAR
# =====================
st.sidebar.title("SehatJiwa")
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
        <p>
        Website edukasi kesehatan mental yang dikembangkan oleh pemuda
        sebagai media digital yang akurat, komprehensif, mudah dipahami,
        dan inklusif bagi masyarakat.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <p>
        SehatJiwa bertujuan meningkatkan literasi kesehatan mental melalui
        konten edukatif terstruktur, berbasis bukti, dan ramah pengguna.
        Website ini dirancang agar dapat diakses lintas perangkat dan
        mendukung penguatan resiliensi individu serta masyarakat.
        </p>
    </div>
    """, unsafe_allow_html=True)

# =====================
# ARTIKEL EDUKASI
# =====================
elif menu == "Artikel Edukasi":
    st.markdown('<div class="section-title">Artikel Edukasi Kesehatan Mental</div>', unsafe_allow_html=True)

    # ---------- ARTICLE 1 ----------
    st.markdown('<div class="card article-card">', unsafe_allow_html=True)
    st.image(
        "https://images.unsplash.com/photo-1506126613408-eca07ce68773",
        use_container_width=True
    )
    st.markdown('<div class="article-title">Memahami Kesehatan Mental di Era Digital</div>', unsafe_allow_html=True)
    st.markdown('<div class="article-meta">Penulis: Tim SehatJiwa | 12 Januari 2026</div>', unsafe_allow_html=True)

    st.write("""
    Kesehatan mental merupakan aspek penting dalam kehidupan modern, terutama
    di tengah perkembangan teknologi dan media digital yang pesat.
    """)

    with st.expander("Baca Selengkapnya"):
        st.write("""
        Di era digital, individu menghadapi berbagai tekanan psikososial,
        mulai dari tuntutan akademik, pekerjaan, hingga paparan media sosial
        yang berlebihan. Kondisi ini dapat memengaruhi kesejahteraan psikologis
        apabila tidak diimbangi dengan literasi kesehatan mental yang memadai.

        Memahami kesehatan mental membantu individu mengenali kondisi diri,
        mengelola stres secara adaptif, serta mengambil langkah yang tepat
        ketika membutuhkan bantuan profesional.
        """)
    st.markdown('</div>', unsafe_allow_html=True)

    # ---------- ARTICLE 2 ----------
    st.markdown('<div class="card article-card">', unsafe_allow_html=True)
    st.image(
        "https://images.unsplash.com/photo-1517841905240-472988babdf9",
        use_container_width=True
    )
    st.markdown('<div class="article-title">Depresi dan Kecemasan: Mengenali Tanda Awal</div>', unsafe_allow_html=True)
    st.markdown('<div class="article-meta">Penulis: Kontributor Pemuda | 18 Januari 2026</div>', unsafe_allow_html=True)

    st.write("""
    Depresi dan kecemasan sering kali tidak disadari sejak dini,
    padahal pengenalan awal sangat penting dalam pencegahan.
    """)

    with st.expander("Baca Selengkapnya"):
        st.write("""
        Depresi ditandai dengan perasaan sedih berkepanjangan, kehilangan
        minat, serta kelelahan emosional. Sementara itu, kecemasan muncul
        dalam bentuk rasa khawatir berlebihan dan sulit berkonsentrasi.

        Mengenali tanda awal memungkinkan individu untuk segera melakukan
        strategi koping dan mencari dukungan yang sesuai.
        """)
    st.markdown('</div>', unsafe_allow_html=True)

# =====================
# VIDEO EDUKASI
# =====================
elif menu == "Video Edukasi":
    st.markdown('<div class="section-title">Video Edukasi Kesehatan Mental</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=oxx564hMBUI")
    st.markdown('</div>', unsafe_allow_html=True)

# =====================
# TES MENTAL
# =====================
elif menu == "Tes Mental":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Tes Refleksi Kesehatan Mental</div>', unsafe_allow_html=True)

    q1 = st.slider("Saya merasa cemas atau tertekan", 0, 3, 1)
    q2 = st.slider("Saya kehilangan minat terhadap aktivitas harian", 0, 3, 1)
    q3 = st.slider("Saya merasa kelelahan secara emosional", 0, 3, 1)

    if st.button("Lihat Hasil"):
        total = q1 + q2 + q3
        if total <= 2:
            st.success("Kondisi mental relatif stabil.")
        elif total <= 6:
            st.warning("Terdapat indikasi tekanan psikologis ringan.")
        else:
            st.error("Disarankan untuk mencari dukungan profesional.")

    st.markdown('</div>', unsafe_allow_html=True)

# =====================
# DUKUNGAN
# =====================
elif menu == "Dukungan":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Dukungan dan Rujukan</div>', unsafe_allow_html=True)

    st.write("""
    SehatJiwa menyediakan informasi rujukan sebagai langkah awal
    untuk mendapatkan dukungan kesehatan mental yang tepat.
    """)

    st.markdown('</div>', unsafe_allow_html=True)

# =====================
# FOOTER
# =====================
st.markdown('<div class="footer">© 2026 SehatJiwa | Youth-Led Mental Health Education</div>', unsafe_allow_html=True)
