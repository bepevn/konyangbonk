from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(page_title='NEON VAULT', layout='wide', initial_sidebar_state='collapsed')
root = Path(__file__).parent / 'game'
read = lambda name: (root / name).read_text(encoding='utf-8')
page = read('index.html').replace('/*STYLE*/',read('style.css')).replace('/*GAME*/',read('game.js'))
components.html(page, height=680, scrolling=False)
