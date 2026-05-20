import streamlit as st
import random

st.set_page_config(
    page_title="emrezurnaci",
    page_icon="🎨",
    layout="centered"
)

# Rastgele renk üret
def random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

c1 = random_color()
c2 = random_color()
c3 = random_color()

# CSS
st.markdown(
    f"""
    <style>
    .stApp {{
        background: linear-gradient(135deg, {c1}, {c2}, {c3});
        background-size: 400% 400%;
        animation: gradient 10s ease infinite;
    }}

    @keyframes gradient {{
        0% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
        100% {{ background-position: 0% 50%; }}
    }}

    .box {{
        background: rgba(255,255,255,0.15);
        padding: 40px;
        border-radius: 20px;
        text-align: center;
        margin-top: 120px;
        backdrop-filter: blur(10px);
        color: white;
        box-shadow: 0 0 25px rgba(0,0,0,0.3);
    }}

    .btn {{
        display: inline-block;
        margin-top: 20px;
        padding: 12px 20px;
        border-radius: 12px;
        background: white;
        color: black;
        text-decoration: none;
        font-weight: bold;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Ana içerik
st.markdown(
    """
    <div class="box">
        <h1>emrezurnaci 🚀</h1>
        <p>Streamlit üzerinde çalışan random renkli sayfa</p>

        <a class="btn" href="/random-path">
            Random Path
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
