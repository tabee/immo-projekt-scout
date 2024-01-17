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

    st.title("Marktanalyse und Standortbewertung")

    # Demografische Daten
    st.subheader("Demografische Daten")
    st.warning("Nicht implementiert")

    # Wirtschaftliche Faktoren
    st.subheader("Wirtschaftliche Faktoren")
    st.warning("Nicht implementiert")

    # Wettbewerbsanalyse
    st.subheader("Wettbewerbsanalyse")
    st.warning("Nicht implementiert")

    # Zugang zu Märkten und Handelszentren
    st.subheader("Zugang zu Märkten und Handelszentren")
    st.warning("Nicht implementiert")

    # Historische Wertentwicklung
    st.subheader("Historische Wertentwicklung")
    st.warning("Nicht implementiert")
