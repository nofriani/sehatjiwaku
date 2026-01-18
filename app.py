import streamlit as st

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
body { background-color: #f3f8f8; }

.hero {
    background-image: url('https://images.unsplash.com/photo-1494790108377-be9c29b29330');
    background-size: cover;
    background-position: center;
    padding: 70px;
    border-radius: 20px;
    color: white;
    margin-bottom: 40px;
}

.card {
    background-color: white;
    padding: 22px;
    border-radius: 16px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.08);
    margin-bottom: 25px;
}

.article-img img {
    height: 200px;
    object-fit: cover;
    border-radius: 12px;
}

.article-title {
    font-size: 22px;
    font-weight: 700;
    margin-top: 10px;
}

.article-meta {
    font-size: 14px;
    color: #666;
    margin-bottom: 10px;
}

.section-title {
    font-size: 30px;
    font-weight: 800;
    color: #2aa198;
    margin-bottom: 25px;
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
# DATA ARTIKEL
# =====================
articles = [
    {
        "title": "Memahami Kesehatan Mental di Era Digital",
        "author": "Tim SehatJiwa",
        "date": "12 Januari 2026",
        "image": "https://images.unsplash.com/photo-1506126613408-eca07ce68773",
        "summary": "Teknologi digital membawa peluang dan tantangan bagi kesehatan mental.",
        "content": "Perkembangan teknologi digital memengaruhi cara individu berinteraksi, belajar, dan bekerja. Paparan berlebihan terhadap media digital dapat meningkatkan tekanan psikologis apabila tidak diimbangi literasi kesehatan mental yang baik."
    },
    {
        "title": "Depresi: Lebih dari Sekadar Sedih",
        "author": "Kontributor Pemuda",
        "date": "14 Januari 2026",
        "image": "https://images.unsplash.com/photo-1517841905240-472988babdf9",
        "summary": "Depresi sering kali tidak disadari sejak dini.",
        "content": "Depresi ditandai dengan perasaan sedih berkepanjangan, kehilangan minat, dan kelelahan emosional. Edukasi dan dukungan profesional berperan penting dalam pencegahan."
    },
    {
        "title": "Mengenali Kecemasan dan Dampaknya",
        "author": "Tim Edukasi",
        "date": "16 Januari 2026",
        "image": "https://images.unsplash.com/photo-1529333166437-7750a6dd5a70",
        "summary": "Kecemasan berlebihan dapat mengganggu aktivitas sehari-hari.",
        "content": "Kecemasan merupakan respons alami terhadap stres, namun perlu dikelola agar tidak berkembang menjadi gangguan."
    },
    {
        "title": "Stres Akademik pada Remaja",
        "author": "Tim SehatJiwa",
        "date": "18 Januari 2026",
        "image": "https://images.unsplash.com/photo-1523050854058-8df90110c9f1",
        "summary": "Tekanan akademik menjadi faktor risiko kesehatan mental.",
        "content": "Tuntutan akademik yang tinggi dapat memicu stres dan kecemasan apabila tidak disertai strategi koping yang adaptif."
    },
    {
        "title": "Peran Dukungan Sosial",
        "author": "Kontributor Pemuda",
        "date": "20 Januari 2026",
        "image": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e",
        "summary": "Dukungan sosial memperkuat resiliensi individu.",
        "content": "Keluarga, teman, dan lingkungan sosial berperan penting dalam menjaga kesehatan mental."
    },
    {
        "title": "Mengelola Emosi Secara Sehat",
        "author": "Tim Edukasi",
        "date": "22 Januari 2026",
        "image": "https://images.unsplash.com/photo-1515378791036-0648a3ef77b2",
        "summary": "Pengelolaan emosi penting bagi kesejahteraan psikologis.",
        "content": "Kemampuan mengenali dan mengekspresikan emosi secara sehat membantu individu menghadapi tekanan hidup."
    },
    {
        "title": "Burnout di Usia Muda",
        "author": "Tim SehatJiwa",
        "date": "24 Januari 2026",
        "image": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",
        "summary": "Burnout tidak hanya dialami pekerja dewasa.",
        "content": "Burnout ditandai kelelahan emosional dan penurunan motivasi yang perlu ditangani sejak dini."
    },
    {
        "title": "Mindfulness untuk Kesehatan Mental",
        "author": "Tim Edukasi",
        "date": "26 Januari 2026",
        "image": "https://images.unsplash.com/photo-1506126613408-eca07ce68773",
        "summary": "Mindfulness membantu meningkatkan kesadaran diri.",
        "content": "Latihan mindfulness membantu individu fokus pada saat ini dan mengurangi stres."
    },
    {
        "title": "Media Sosial dan Kesehatan Mental",
        "author": "Kontributor Pemuda",
        "date": "28 Januari 2026",
        "image": "https://images.unsplash.com/photo-1517841905240-472988babdf9",
        "summary": "Media sosial memiliki dampak positif dan negatif.",
        "content": "Penggunaan media sosial yang bijak penting untuk menjaga keseimbangan mental."
    },
    {
        "title": "Kapan Harus Mencari Bantuan Profesional?",
        "author": "Tim SehatJiwa",
        "date": "30 Januari 2026",
        "image": "https://images.unsplash.com/photo-1529333166437-7750a6dd5a70",
        "summary": "Mencari bantuan adalah langkah berani.",
        "content": "Bantuan profesional perlu dipertimbangkan ketika kondisi mental mengganggu aktivitas sehari-hari."
    }
]

# =====================
# BERANDA
# =====================
if menu == "Beranda":
    st.markdown('<div class="hero"><h1>SehatJiwa</h1><p>Website Edukasi Kesehatan Mental Berbasis Pemuda</p></div>', unsafe_allow_html=True)

# =====================
# ARTIKEL EDUKASI
# =====================
elif menu == "Artikel Edukasi":
    st.markdown('<div class="section-title">Artikel Edukasi Kesehatan Mental</div>', unsafe_allow_html=True)

    for art in articles:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="article-img">', unsafe_allow_html=True)
        st.image(art["image"], use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown(f'<div class="article-title">{art["title"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="article-meta">Penulis: {art["author"]} | {art["date"]}</div>', unsafe_allow_html=True)
        st.write(art["summary"])

        with st.expander("Baca Detail Artikel"):
            st.write(art["content"])

        st.markdown('</div>', unsafe_allow_html=True)

# =====================
# VIDEO EDUKASI
# =====================
elif menu == "Video Edukasi":
    st.markdown('<div class="section-title">Video Edukasi Kesehatan Mental</div>', unsafe_allow_html=True)

    videos = [
        "https://www.youtube.com/watch?v=oxx564hMBUI",
        "https://www.youtube.com/watch?v=hnpQrMqDoqE",
        "https://www.youtube.com/watch?v=MB5IX-np5fE",
        "https://www.youtube.com/watch?v=9yjZpBq1XBE",
        "https://www.youtube.com/watch?v=2pLT-olgUJs"
    ]

    for v in videos:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.video(v)
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
    st.write("Informasi konselor sekolah, psikolog, dan layanan kesehatan terdekat.")
    st.markdown('</div>', unsafe_allow_html=True)

# =====================
# FOOTER
# =====================
st.markdown('<div class="footer">© 2026 SehatJiwa | Youth-Led Mental Health Education</div>', unsafe_allow_html=True)
