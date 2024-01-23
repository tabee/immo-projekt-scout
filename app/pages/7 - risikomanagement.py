import streamlit as st
from app_utils import set_sessions_state, get_address, get_sidebar
from utils import get_expander_box

# Session State
set_sessions_state()

# Sidebar
get_sidebar()

# Hauptinhalt der Seite (OHNE egaid)
if not st.session_state['ch.bfs.gebaeude_wohnungs_register.egaid']:
    get_address()

# Hauptinhalt der Seite (MIT egaid)   
if st.session_state["ch.bfs.gebaeude_wohnungs_register.egaid"]:
    e_gebäude_koord = st.session_state['e_gebäude_koord']
    n_gebäude_koord = st.session_state['n_gebäude_koord']
    iframe_width = st.session_state['iframe_width']
    # end of repeated code

    # Risikomanagement
    st.title("Risikomanagement")

    # Markt- und Liquiditätsrisiken
    st.subheader("Markt- und Liquiditätsrisiken")
    st.warning("Markt- und Liquiditätsrisiken")

    # Bau- und Entwicklungsrisiken
    st.subheader("Bau- und Entwicklungsrisiken")
    st.warning("Bau- und Entwicklungsrisiken")
    # TODO: Gewässerschutz

    # Rechtliche und regulatorische Risiken
    st.subheader("Rechtliche und regulatorische Risiken")
    st.warning("Rechtliche und regulatorische Risiken")

    # Umweltrisiken
    st.subheader("Umweltrisiken")
    st.warning("Umweltrisiken")

    # Politische und soziale Risiken
    st.subheader("Politische und soziale Risiken")
    st.warning("Politische und soziale Risiken")
