import streamlit as st
import random

st.set_page_config(page_title="emrezurnaci", layout="centered")

# Sayfa state
if "page" not in st.session_state:
    st.session_state.page = "home"


def random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))


# -------------------------
# SAYFA 1 (HOME)
# -------------------------
def home():
    c1, c2, c3 = random_color(), random_color(), random_color()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background: linear-gradient(135deg, {c1}, {c2}, {c3});
            background-size: 400% 400%;
            animation: gradient 8s ease infinite;
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
            margin-top: 100px;
            backdrop-filter: blur(10px);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="box">
        <h1>emrezurnaci 🚀</h1>
        <p>Home Page</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Random Path'e Git"):
        st.session_state.page = "random"
        st.rerun()


# -------------------------
# SAYFA 2 (RANDOM)
# -------------------------
def random_page():
    st.title("Random Path 😄")
    st.write("Burası ikinci sayfa")

    if st.button("Geri dön"):
        st.session_state.page = "home"
        st.rerun()


# -------------------------
# ROUTER
# -------------------------
if st.session_state.page == "home":
    home()
else:
    random_page()
