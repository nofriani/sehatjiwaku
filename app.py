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
# STYLE
# =====================
st.markdown("""
<style>
body {
    background-color: #f4f9f9;
}
.block {
    background-color: white;
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
    margin-bottom: 30px;
}
.title {
    font-size: 42px;
    font-weight: 800;
    color: #2aa198;
}
.subtitle {
    font-size: 18px;
    color: #555;
}
</style>
""", unsafe_allow_html=True)

# =====================
# SIDEBAR NAVIGATION
# =====================
st.sidebar.title("🧠 SehatJiwa")
menu = st.sidebar.radio(
    "Menu",
    ["Beranda", "Artikel Edukasi", "Video Edukasi", "Tes Kesehatan Mental", "Dukungan"]
)

# =====================
# BERANDA
# =====================
if menu == "Beranda":
    st.markdown("<div class='block'>", unsafe_allow_html=True)
    st.markdown("<div class='title'>SehatJiwa</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Website Edukasi Kesehatan Mental Berbasis Pemuda</div>", unsafe_allow_html=True)

    st.markdown("""
    **SehatJiwa** merupakan website edukasi kesehatan mental yang dikembangkan oleh pemuda
    sebagai media digital yang **akurat, komprehensif, mudah dipahami, dan inklusif** bagi masyarakat.

    Website ini bertujuan meningkatkan **literasi kesehatan mental** melalui konten edukatif
    yang terstruktur, ramah pengguna, dan berbasis bukti.
    """)
    st.info("👉 Gunakan menu di samping untuk membaca artikel, menonton video, dan melakukan tes refleksi diri.")
    st.markdown("</div>", unsafe_allow_html=True)

# =====================
# ARTIKEL EDUKASI
# =====================
elif menu == "Artikel Edukasi":
    st.markdown("<div class='block'>", unsafe_allow_html=True)
    st.header("📖 Artikel Edukasi Kesehatan Mental")

    with st.expander("🧠 Apa Itu Kesehatan Mental?"):
        st.write("""
        Kesehatan mental adalah kondisi kesejahteraan ketika seseorang mampu mengenali
        potensi dirinya, mengelola stres kehidupan sehari-hari, bekerja secara produktif,
        serta berkontribusi di lingkungan sosial.

        Menjaga kesehatan mental sama pentingnya dengan menjaga kesehatan fisik,
        karena keduanya saling berkaitan.
        """)

    with st.expander("😔 Depresi, Kecemasan, dan Stres"):
        st.write("""
        Depresi ditandai dengan perasaan sedih berkepanjangan dan kehilangan minat.
        Kecemasan muncul dalam bentuk rasa takut atau khawatir berlebihan,
        sedangkan stres adalah respons tubuh terhadap tekanan.

        Ketiganya dapat dikelola dengan edukasi, dukungan sosial, dan bantuan profesional.
        """)

    with st.expander("🌱 Strategi Mengelola Stres dan Emosi"):
        st.write("""
        Beberapa strategi sederhana yang dapat dilakukan:
        - Mengatur waktu istirahat
        - Melakukan aktivitas fisik ringan
        - Berbicara dengan orang terpercaya
        - Membatasi paparan media sosial
        """)

    st.markdown("</div>", unsafe_allow_html=True)

# =====================
# VIDEO EDUKASI
# =====================
elif menu == "Video Edukasi":
    st.markdown("<div class='block'>", unsafe_allow_html=True)
    st.header("🎥 Video Edukasi Kesehatan Mental")

    st.write("Video berikut membantu memahami kesehatan mental secara sederhana dan mudah dipahami.")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Kesehatan Mental Itu Penting")
        st.video("https://www.youtube.com/watch?v=oxx564hMBUI")

    with col2:
        st.subheader("Cara Mengelola Stres")
        st.video("https://www.youtube.com/watch?v=hnpQrMqDoqE")

    st.markdown("</div>", unsafe_allow_html=True)

# =====================
# TES KESEHATAN MENTAL
# =====================
elif menu == "Tes Kesehatan Mental":
    st.markdown("<div class='block'>", unsafe_allow_html=True)
    st.header("📝 Tes Kesehatan Mental (Refleksi Diri)")
    st.warning("Tes ini bukan diagnosis medis, hanya refleksi awal.")

    q1 = st.radio("Saya merasa cemas atau tertekan akhir-akhir ini", ["Tidak", "Kadang", "Sering"])
    q2 = st.radio("Saya sulit menikmati aktivitas sehari-hari", ["Tidak", "Kadang", "Sering"])
    q3 = st.radio("Saya merasa kelelahan secara emosional", ["Tidak", "Kadang", "Sering"])

    if st.button("Lihat Hasil"):
        skor = [q1, q2, q3].count("Sering")

        if skor == 0:
            st.success("Kondisi mental kamu relatif baik. Tetap jaga kesehatan jiwa 💚")
        elif skor <= 2:
            st.warning("Kamu mungkin sedang mengalami tekanan. Luangkan waktu untuk self-care.")
        else:
            st.error("Kamu membutuhkan dukungan lebih lanjut. Jangan ragu mencari bantuan profesional.")

    st.markdown("</div>", unsafe_allow_html=True)

# =====================
# DUKUNGAN
# =====================
elif menu == "Dukungan":
    st.markdown("<div class='block'>", unsafe_allow_html=True)
    st.header("🤝 Komunitas & Dukungan")

    st.write("""
    SehatJiwa menyediakan informasi rujukan bantuan profesional sebagai
    bentuk dukungan kesehatan mental.
    """)

    st.success("🏫 Konselor Sekolah – Pendampingan awal")
    st.info("🧑‍⚕️ Psikolog / Konselor Profesional")
    st.warning("🚨 Jika darurat, segera hubungi layanan kesehatan terdekat")

    st.markdown("</div>", unsafe_allow_html=True)

# =====================
# FOOTER
# =====================
st.caption("© 2026 SehatJiwa | Youth-Led Mental Health Education")
