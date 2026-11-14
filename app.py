from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

from builder import build_html

st.set_page_config(
    page_title="Paka Manohar | Mechanical Engineer",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

ROOT = Path(__file__).parent


@st.cache_data(show_spinner=False)
def load_page() -> str:
    return build_html(ROOT)


# Hide Streamlit's own chrome so the portfolio fills the whole screen.
st.markdown(
    """
    <style>
      #MainMenu, header, footer, [data-testid="stToolbar"],
      [data-testid="stDecoration"], [data-testid="stStatusWidget"] {display:none !important;}
      .block-container {padding:0 !important; max-width:100% !important;}
      [data-testid="stVerticalBlock"] {gap:0 !important;}
      [data-testid="stMain"], .main {overflow:hidden !important;}
      iframe {height:100vh !important; height:100dvh !important; width:100% !important; border:0 !important;}
    </style>
    """,
    unsafe_allow_html=True,
)

components.html(load_page(), height=900, scrolling=True)
