import streamlit as st

# =====================
# CONFIG
# =====================
st.set_page_config(page_title="SehatJiwa", layout="wide")

# =====================
# STYLE
# =====================
st.markdown("""
<style>
body { background-color: #f6fbfb; }

.container {
    max-width: 1200px;
    margin: auto;
}

.hero {
    padding: 80px 60px;
    border-radius: 28px;
    background: linear-gradient(120deg,#e6fffb,#f0fdfa);
    margin-bottom: 50px;
}

.hero h1 {
    font-size: 52px;
    line-height: 1.15;
}
.hero span { color: #14b8a6; }

.section-title {
    font-size: 28px;
    font-weight: 700;
    margin-bottom: 20px;
}

.card {
    background: white;
    border-radius: 18px;
    padding: 16px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.06);
    margin-bottom: 25px;
}

.article-img {
    width: 40%;
    height: 40px;        /* 🔒 KUNCI UKURAN DI SINI */
    overflow: hidden;
    border-radius: 14px;
    margin-bottom: 12px;
}

.article-img img {
    width: 40%;
    height: 40%;
    object-fit: cover;   /* POTONG RAPI */
    display: block;
}


.badge {
    font-size: 11px;
    padding: 4px 10px;
    border-radius: 999px;
    background: #e6fffb;
    color: #0f766e;
    display: inline-block;
    margin-bottom: 6px;
}

.meta {
    font-size: 13px;
    color: #64748b;
    margin-bottom: 6px;
}

.article-title {
    font-size: 18px;
    font-weight: 600;
    margin-bottom: 6px;
}

.video-card iframe {
    border-radius: 14px;
    height: 220px !important;
}
</style>
""", unsafe_allow_html=True)

# =====================
# DATA
# =====================
articles = [
    {
        "title": "Mengenal Kecemasan (Anxiety)",
        "author": "Tim SehatJiwa",
        "date": "18 Januari 2026",
        "image": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",
        "summary": "Kecemasan adalah respons alami terhadap stres, namun perlu dikenali sejak dini.",
        "content": """
Kecemasan merupakan reaksi alami tubuh terhadap situasi yang dianggap mengancam.
Namun, ketika rasa cemas muncul secara berlebihan dan terus-menerus, hal ini dapat
mengganggu aktivitas sehari-hari.

Mengenali tanda awal kecemasan membantu individu mengambil langkah preventif
dan mencari dukungan yang tepat.
"""
    },
    {
        "title": "Pentingnya Tidur untuk Kesehatan Mental",
        "author": "Kontributor Pemuda",
        "date": "20 Januari 2026",
        "image": "https://images.unsplash.com/photo-1511295742362-92c96b1cf484",
        "summary": "Tidur berkualitas berperan penting dalam stabilitas emosi dan fokus.",
        "content": """
Tidur yang cukup tidak hanya berdampak pada kesehatan fisik,
tetapi juga berpengaruh besar terhadap keseimbangan emosional
dan kemampuan kognitif seseorang.

Kurang tidur dapat meningkatkan risiko stres, kecemasan, dan depresi.
"""
    },
    {
        "title": "Strategi Praktis Mengelola Stres Harian",
        "author": "Tim Edukasi",
        "date": "22 Januari 2026",
        "image": "https://images.unsplash.com/photo-1506126613408-eca07ce68773",
        "summary": "Stres dapat dikelola melalui kebiasaan sederhana dan konsisten.",
        "content": """
Pengelolaan stres dapat dimulai dari langkah kecil seperti
mengatur waktu istirahat, melakukan aktivitas fisik ringan,
dan menjaga keseimbangan antara pekerjaan dan kehidupan pribadi.
"""
    },
    {
        "title": "Burnout pada Remaja dan Dewasa Muda",
        "author": "Tim SehatJiwa",
        "date": "24 Januari 2026",
        "image": "https://images.unsplash.com/photo-1529333166437-7750a6dd5a70",
        "summary": "Burnout tidak hanya dialami pekerja profesional.",
        "content": """
Burnout ditandai dengan kelelahan emosional, sinisme,
dan penurunan motivasi. Kondisi ini semakin banyak
dialami oleh pelajar dan mahasiswa akibat tekanan akademik.
"""
    },
    {
        "title": "Peran Dukungan Sosial dalam Kesehatan Mental",
        "author": "Kontributor Pemuda",
        "date": "26 Januari 2026",
        "image": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e",
        "summary": "Lingkungan sosial yang suportif memperkuat resiliensi.",
        "content": """
Dukungan dari keluarga, teman, dan komunitas
membantu individu merasa didengar, dipahami,
dan tidak menghadapi masalah sendirian.
"""
    },
    {
        "title": "Mindfulness untuk Menenangkan Pikiran",
        "author": "Tim Edukasi",
        "date": "28 Januari 2026",
        "image": "https://images.unsplash.com/photo-1504198453319-5ce911bafcde",
        "summary": "Mindfulness membantu fokus pada momen saat ini.",
        "content": """
Latihan mindfulness mengajarkan individu
untuk menyadari pikiran dan emosi tanpa menghakimi,
sehingga membantu mengurangi tekanan mental.
"""
    },
    {
        "title": "Media Sosial dan Dampaknya bagi Kesehatan Mental",
        "author": "Tim SehatJiwa",
        "date": "30 Januari 2026",
        "image": "https://images.unsplash.com/photo-1515378791036-0648a3ef77b2",
        "summary": "Media sosial memiliki dampak positif dan negatif.",
        "content": """
Penggunaan media sosial secara berlebihan
dapat memicu perbandingan sosial dan stres.
Penggunaan yang bijak dapat menjaga kesehatan mental.
"""
    },
    {
        "title": "Mengelola Emosi Secara Sehat",
        "author": "Tim Edukasi",
        "date": "1 Februari 2026",
        "image": "https://images.unsplash.com/photo-1508214751196-bcfd4ca60f91",
        "summary": "Kemampuan mengenali emosi penting bagi kesejahteraan psikologis.",
        "content": """
Mengelola emosi tidak berarti menekan perasaan,
melainkan memahami dan mengekspresikannya
secara sehat dan adaptif.
"""
    },
    {
        "title": "Kapan Harus Mencari Bantuan Profesional?",
        "author": "Tim SehatJiwa",
        "date": "3 Februari 2026",
        "image": "https://images.unsplash.com/photo-1520975916090-3105956dac38",
        "summary": "Mencari bantuan adalah langkah berani, bukan kelemahan.",
        "content": """
Apabila stres atau kecemasan berlangsung lama
dan mengganggu fungsi harian,
bantuan profesional perlu dipertimbangkan.
"""
    },
    {
        "title": "Membangun Resiliensi di Era Digital",
        "author": "Kontributor Pemuda",
        "date": "5 Februari 2026",
        "image": "https://images.unsplash.com/photo-1496307042754-b4aa456c4a2d",
        "summary": "Resiliensi membantu individu beradaptasi dengan perubahan.",
        "content": """
Resiliensi merupakan kemampuan untuk bangkit
dari tekanan dan tantangan hidup,
terutama di era digital yang serba cepat.
"""
    }
]


videos = [
    "https://www.youtube.com/embed/oxx564hMBUI",
    "https://www.youtube.com/embed/hnpQrMqDoqE",
    "https://www.youtube.com/embed/MB5IX-np5fE",
    "https://www.youtube.com/embed/9yjZpBq1XBE",
    "https://www.youtube.com/embed/2pLT-olgUJs"
]

# =====================
# MAIN
# =====================
st.markdown('<div class="container">', unsafe_allow_html=True)

# HERO
st.markdown("""
<div class="hero">
  <h1>Kesehatan Mental<br>Dimulai dari <span>Kesadaran</span></h1>
  <p>Media edukasi digital yang akurat, inklusif, dan bersahabat.</p>
</div>
""", unsafe_allow_html=True)

# =====================
# ARTIKEL
# =====================
st.markdown('<div class="section-title">Artikel Edukasi</div>', unsafe_allow_html=True)

cols = st.columns(3)
for i, art in enumerate(articles):
    with cols[i % 3]:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="article-img">', unsafe_allow_html=True)
        st.image(art["image"], use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="badge">EDUKASI</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="article-title">{art["title"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="meta">{art["author"]} • {art["date"]}</div>', unsafe_allow_html=True)
        st.write(art["summary"])

        with st.expander("Baca Selengkapnya"):
            st.write(art["content"])

        st.markdown('</div>', unsafe_allow_html=True)

# =====================
# VIDEO
# =====================
st.markdown('<div class="section-title">Video Edukasi</div>', unsafe_allow_html=True)

vcols = st.columns(3)
for i, v in enumerate(videos):
    with vcols[i % 3]:
        st.markdown('<div class="card video-card">', unsafe_allow_html=True)
        st.video(v)
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
