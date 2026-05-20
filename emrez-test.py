import streamlit as st
import random

st.set_page_config(
    page_title="emrezurnaci",
    page_icon="🎨",
    layout="centered"
)

def random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

c1, c2, c3 = random_color(), random_color(), random_color()

st.markdown(
    f"""
    <style>
    .stApp {{
        background: linear-gradient(135deg, {c1}, {c2}, {c3});
        background-size: 400% 400%;
        animation: gradient 10s ease infinite;
        color: white;
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
        margin-top: 80px;
        backdrop-filter: blur(10px);
        box-shadow: 0 0 25px rgba(0,0,0,0.3);
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
<div class="box">
    <h1>emrezurnaci 🚀</h1>
    <p>Streamlit random renkli sayfa</p>
</div>
""", unsafe_allow_html=True)

# ✅ GERÇEK ÇALIŞAN BUTON
if st.button("Random Path'e Git"):
    st.switch_page("pages/random.py")
