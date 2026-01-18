import streamlit as st

# =====================
# KONFIGURASI HALAMAN
# =====================
st.set_page_config(
    page_title="SehatJiwa",
    page_icon="🧠",
    layout="wide"
)

# =====================
# DATA ARTIKEL
# =====================
ARTIKEL = [
    {
        "id": 1,
        "judul": "Apa Itu Kesehatan Mental?",
        "ringkas": "Pengertian kesehatan mental menurut WHO.",
        "isi": """
Kesehatan mental adalah kondisi kesejahteraan
di mana individu mampu menyadari potensinya,
mengelola tekanan hidup, bekerja secara produktif,
dan berkontribusi secara bermakna dalam masyarakat.

WHO menegaskan bahwa kesehatan mental
bukan sekadar ketiadaan gangguan mental.
"""
    },
    {
        "id": 2,
        "judul": "Depresi pada Remaja",
        "ringkas": "Depresi merupakan gangguan mental yang umum dialami remaja.",
        "isi": """
Depresi ditandai dengan perasaan sedih berkepanjangan,
kehilangan minat, kelelahan emosional,
dan gangguan fungsi sehari-hari.

Data I-NAMHS menunjukkan remaja
merupakan kelompok paling rentan.
"""
    },
    {
        "id": 3,
        "judul": "Pentingnya Literasi Kesehatan Mental",
        "ringkas": "Literasi mental membantu mengenali dan mencegah gangguan.",
        "isi": """
Literasi kesehatan mental membantu individu:
- Mengenali gejala awal gangguan mental
- Mengurangi stigma
- Mendorong pencarian bantuan profesional

Rendahnya literasi meningkatkan risiko misinformasi.
"""
    }
]

# =====================
# SESSION STATE
# =====================
if "page" not in st.session_state:
    st.session_state.page = "Beranda"

if "artikel_id" not in st.session_state:
    st.session_state.artikel_id = None

# =====================
# SIDEBAR NAVIGASI
# =====================
menu = st.sidebar.radio(
    "📌 Menu",
    [
        "Beranda",
        "Artikel Edukasi",
        "Video Edukasi",
        "Tes Mental",
        "Pelayanan"
    ]
)

# =====================
# BERANDA
# =====================
if menu == "Beranda":
    st.title("🧠 SehatJiwa")
    st.subheader("Website Edukasi Kesehatan Mental")

    st.markdown("""
    **SehatJiwa** adalah platform edukasi kesehatan mental
    yang menyajikan informasi akurat, mudah dipahami,
    dan inklusif bagi masyarakat.

    🎯 Tujuan:
    - Meningkatkan literasi kesehatan mental  
    - Mengurangi stigma  
    - Mendorong perilaku mencari bantuan  
    """)

    st.info("Gunakan menu di samping untuk menjelajahi fitur SehatJiwa.")

# =====================
# ARTIKEL EDUKASI
# =====================
elif menu == "Artikel Edukasi":

    # ===== HALAMAN DETAIL ARTIKEL =====
    if st.session_state.page == "detail":
        artikel = next(
            (a for a in ARTIKEL if a["id"] == st.session_state.artikel_id),
            None
        )

        if artikel:
            st.title("📖 Detail Artikel")
            st.header(artikel["judul"])
            st.write(artikel["isi"])

            if st.button("⬅ Kembali ke Daftar Artikel"):
                st.session_state.page = "list"
        else:
            st.error("Artikel tidak ditemukan.")

    # ===== HALAMAN LIST ARTIKEL =====
    else:
        st.session_state.page = "list"
        st.title("📚 Artikel Edukasi")

        for a in ARTIKEL:
            st.subheader(a["judul"])
            st.write(a["ringkas"])

            if st.button("Baca Selengkapnya", key=a["id"]):
                st.session_state.artikel_id = a["id"]
                st.session_state.page = "detail"
                st.rerun()

# =====================
# VIDEO EDUKASI
# =====================
elif menu == "Video Edukasi":
    st.title("🎥 Video Edukasi Kesehatan Mental")

    st.video("https://www.youtube.com/watch?v=oxx564hMBUI")

    st.markdown("""
    Video ini membahas pentingnya menjaga kesehatan mental,
    mengenali stres, dan mengurangi stigma di masyarakat.
    """)

# =====================
# TES KESEHATAN MENTAL
# =====================
elif menu == "Tes Mental":
    st.title("📝 Tes Kesehatan Mental Sederhana")

    st.caption("⚠️ Tes ini bersifat skrining awal, bukan diagnosis.")

    q1 = st.radio("Saya sering merasa cemas berlebihan", [0, 1, 2, 3])
    q2 = st.radio("Saya sulit tidur atau sering terbangun", [0, 1, 2, 3])
    q3 = st.radio("Saya kehilangan minat terhadap hal yang biasa saya sukai", [0, 1, 2, 3])

    if st.button("Lihat Hasil"):
        skor = q1 + q2 + q3

        if skor <= 3:
            st.success("Kondisi mental Anda tergolong baik.")
        elif skor <= 6:
            st.warning("Terdapat tanda stres ringan.")
        else:
            st.error("Disarankan untuk berkonsultasi dengan tenaga profesional.")

# =====================
# PELAYANAN
# =====================
elif menu == "Pelayanan":
    st.title("📞 Pelayanan Kesehatan Mental")

    st.markdown("""
    **Layanan Darurat Indonesia**
    - 📞 **119 ext. 8 (SEJIWA)**
    - 📞 Hotline Kemenkes

    **Rujukan Bantuan**
    - Puskesmas terdekat
    - Psikolog
    - Psikiater
    """)

    st.info("Jika Anda atau orang di sekitar Anda membutuhkan bantuan, jangan ragu untuk menghubungi layanan di atas.")
