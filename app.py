import streamlit as st

# =========================
# CONFIG
# =========================
st.set_page_config(layout="wide", page_title="SehatJiwa")

if "page" not in st.session_state:
    st.session_state.page = "Beranda"
if "article_id" not in st.session_state:
    st.session_state.article_id = None

# =========================
# STYLE
# =========================
st.markdown("""
<style>
body { background-color: #f6fbfb; }

.nav {
    display:flex;
    justify-content:space-between;
    align-items:center;
    padding:14px 30px;
    background:white;
    border-radius:14px;
    box-shadow:0 2px 8px rgba(0,0,0,0.05);
    margin-bottom:30px;
}
.nav a {
    margin-right:22px;
    font-weight:500;
    color:#334155;
    text-decoration:none;
}
.nav a:hover { color:#14b8a6; }

.cta {
    background:#14b8a6;
    color:white;
    padding:10px 18px;
    border-radius:999px;
    font-weight:600;
}

.hero {
    padding:90px 60px;
    border-radius:28px;
    background:linear-gradient(120deg,#e6fffb,#f0fdfa);
    margin-bottom:50px;
}
.hero h1 {
    font-size:56px;
    line-height:1.1;
}
.hero span { color:#14b8a6; }

.card {
    background:white;
    border-radius:18px;
    padding:18px;
    box-shadow:0 6px 18px rgba(0,0,0,0.06);
    margin-bottom:30px;
}
.card img {
    width:100%;
    height:190px;
    object-fit:cover;
    border-radius:14px;
}

.badge {
    display:inline-block;
    font-size:12px;
    padding:4px 10px;
    border-radius:999px;
    background:#e6fffb;
    color:#0f766e;
    margin-bottom:8px;
}
.meta {
    font-size:13px;
    color:#64748b;
}

.button {
    color:#14b8a6;
    font-weight:600;
    cursor:pointer;
}
</style>
""", unsafe_allow_html=True)

# =========================
# NAVBAR
# =========================
col1, col2 = st.columns([3,2])
with col1:
    st.markdown("""
    <div class="nav">
      <div><strong>SehatJiwa</strong></div>
      <div>
        <a onclick="window.location.reload()">Beranda</a>
        <a>Artikel</a>
        <a>Video</a>
        <a>Cek Mandiri</a>
        <a>Layanan & Komunitas</a>
      </div>
    </div>
    """, unsafe_allow_html=True)

# =========================
# DATA ARTIKEL (10)
# =========================
articles = [
    {
        "id": i,
        "title": f"Mengenal Kesehatan Mental #{i}",
        "author": "Tim SehatJiwa",
        "date": "Januari 2026",
        "image": "https://images.unsplash.com/photo-1506126613408-eca07ce68773",
        "summary": "Pemahaman dasar mengenai kesehatan mental dan pentingnya kesadaran diri.",
        "content": """
Kesehatan mental adalah kondisi kesejahteraan psikologis yang memungkinkan individu
mengelola stres, bekerja produktif, dan berkontribusi di masyarakat.

Kurangnya literasi kesehatan mental sering menyebabkan stigma dan keterlambatan
dalam mencari bantuan profesional.
"""
    } for i in range(1,11)
]

# =========================
# BERANDA
# =========================
if st.session_state.page == "Beranda" and st.session_state.article_id is None:
    st.markdown("""
    <div class="hero">
      <h1>Kesehatan Mental<br>Dimulai dari <span>Kesadaran</span></h1>
      <p>Media edukasi digital yang akurat, inklusif, dan bersahabat.</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Artikel Pilihan")
    cols = st.columns(3)
    for i, art in enumerate(articles[:3]):
        with cols[i]:
            st.markdown(f"""
            <div class="card">
              <img src="{art['image']}">
              <div class="badge">EDUKASI</div>
              <h4>{art['title']}</h4>
              <div class="meta">{art['date']} • 5 menit baca</div>
              <p>{art['summary']}</p>
              <div class="button">Baca Selengkapnya</div>
            </div>
            """, unsafe_allow_html=True)

# =========================
# ARTIKEL LIST
# =========================
st.subheader("Semua Artikel")
cols = st.columns(3)
for i, art in enumerate(articles):
    with cols[i % 3]:
        if st.button(art["title"], key=art["id"]):
            st.session_state.article_id = art["id"]

# =========================
# DETAIL ARTIKEL
# =========================
if st.session_state.article_id:
    art = articles[st.session_state.article_id - 1]
    st.image(art["image"], use_container_width=True)
    st.markdown(f"### {art['title']}")
    st.caption(f"{art['author']} • {art['date']}")
    st.write(art["content"])
    if st.button("Kembali"):
        st.session_state.article_id = None
