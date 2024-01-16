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


    # Exit-Strategien und Wertsteigerung
    st.title("Exit-Strategien und Wertsteigerung")

    # Verkaufsoptionen
    st.subheader("Verkaufsoptionen")
    st.warning("Verkaufsoptionen")

    # Refinanzierungsmöglichkeiten
    st.subheader("Refinanzierungsmöglichkeiten")
    st.warning("Refinanzierungsmöglichkeiten")

    # Langzeitvermietung
    st.subheader("Langzeitvermietung")
    st.warning("Langzeitvermietung")

    # Wertsteigerungsstrategien
    st.subheader("Wertsteigerungsstrategien")
    st.warning("Wertsteigerungsstrategien")
