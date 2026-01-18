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
    height: 170px;
    overflow: hidden;
    border-radius: 14px;
    margin-bottom: 12px;
}

.article-img img {
    width: 100%;
    height: 100%;
    object-fit: cover;
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
        "title": f"Mengenal Kesehatan Mental #{i}",
        "author": "Tim SehatJiwa",
        "date": "Januari 2026",
        "image": "https://images.unsplash.com/photo-1506126613408-eca07ce68773",
        "summary": "Pemahaman dasar mengenai kesehatan mental dan pentingnya kesadaran diri.",
        "content": "Kesehatan mental adalah kondisi kesejahteraan psikologis yang memengaruhi cara berpikir, merasa, dan bertindak."
    } for i in range(1,11)
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
