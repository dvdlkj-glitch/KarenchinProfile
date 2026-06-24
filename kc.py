"""
Karen Chin — Personal Business Development Webpage (Streamlit wrapper)
=====================================================================

Redesign pipeline behind this site:
  • web-scraper-agent concept — the source markup is the content source of
    truth: read, parsed, and re-served with the copy/structure intact. (See the
    companion ./web-scraper-agent harness used to capture page content.)
  • ui-ux-pro-max — design-intelligence pass driving the cinematic-dark +
    glassmorphism redesign: depth/lighting, glass surfaces, spring/back-out
    easing, staggered reveals, scroll-progress, magnetic CTAs, 3D tilt,
    and motion-safe fallbacks (prefers-reduced-motion respected end-to-end).
  • framer-motion — framer-motion is React-only and can't drive the plain DOM
    of a static page, so the redesign uses **Motion One** (motion.dev) —
    framer-motion's official vanilla-JS sibling, same API family
    (animate / scroll / inView / stagger). The animation choreography is baked
    directly into karen-chin.html (loaded from the Motion One CDN), so this
    wrapper just serves the page full-bleed.

Deploy:
    streamlit run kc.py

Files that must sit in the SAME folder as kc.py:
    - karen-chin.html      (the redesigned personal page, self-contained)
    - hrdf-landing.html    (the ongoing HRDF programme page)

Routing:
    /            -> Karen's personal page
    /?page=hrdf  -> the HRDF programme page (with a "Back to Karen" button)
"""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

# ---- Page config ----
st.set_page_config(
    page_title="Karen Chin — Corporate Training Sourcing | Kota Kinabalu",
    page_icon="🤝",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---- Strip Streamlit chrome & make the iframe fill the whole viewport.
#      The page scrolls INSIDE the iframe so all scroll animations
#      (reveals, timeline fill, parallax, tilt) keep working. ----
st.markdown(
    """
    <style>
      header[data-testid="stHeader"] {display:none;}
      [data-testid="stToolbar"] {display:none;}
      footer {visibility:hidden;}
      #MainMenu {visibility:hidden;}
      .block-container {padding:0 !important; max-width:100% !important;}
      [data-testid="stAppViewContainer"] {overflow:hidden;}
      .stApp iframe {
        height: 100vh !important;
        height: 100dvh !important;   /* correct height on mobile browsers */
        width: 100% !important;
        display: block;
        border: none;
      }
      html, body {margin:0; padding:0; overflow:hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

BASE = Path(__file__).parent

# Floating back button injected into the HRDF page
BACK_BUTTON = """
<a href="?" target="_top" style="position:fixed;top:18px;left:18px;z-index:999;
   background:rgba(8,11,18,.82);color:#f4e8cf;border:1px solid rgba(224,169,63,.5);
   font:700 14px/1 Manrope,sans-serif;text-decoration:none;border-radius:999px;
   padding:11px 20px;backdrop-filter:blur(8px);">&#8592; Back to Karen</a>
</body>"""


def load(name: str) -> str:
    return (BASE / name).read_text(encoding="utf-8")


page = st.query_params.get("page", "home")

if page == "hrdf":
    # The HRDF page keeps its own design; just add a way back.
    html = load("hrdf-landing.html").replace("</body>", BACK_BUTTON, 1)
else:
    # The redesigned page self-contains its Motion One choreography.
    # Repoint the in-iframe spotlight link to the routed HRDF page.
    html = load("karen-chin.html").replace(
        'href="hrdf-landing.html" target="_blank"',
        'href="?page=hrdf" target="_top"',
        1,
    )

# Height is overridden to 100vh by the CSS above; scrolling happens inside.
components.html(html, height=900, scrolling=True)
