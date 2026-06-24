import pathlib
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="GPS Attendance & Field Tracking", layout="wide")

# Load the standalone HTML app (must sit next to this file in the repo)
html = pathlib.Path(__file__).parent.joinpath("attendance-pro.html").read_text(encoding="utf-8")

# Render it full-height. scrolling=True lets the inner page scroll.
components.html(html, height=1100, scrolling=True)
