import streamlit as st
import streamlit.components.v1 as components
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

    # Finanzielle Analyse und Bewertung
    st.title("finanzielle analyse und bewertung")

    # Kostenanalyse
    st.subheader("Kostenanalyse")
    st.info("Daten gehen an Baloise und UBS. Login erforderlich.")
    with st.expander(("Online berechnen"), expanded=False):
        components.iframe("https://app.houzy.ch/landing?startOnBoarding=hv&language=de-CH", width=iframe_width, height=800, scrolling=True)


    # Finanzierungsquellen und -strukturen
    st.subheader("Finanzierungsquellen und -strukturen")
    st.warning("Nicht implementiert")

    # Rentabilitäts- und Cashflow-Projektionen
    st.subheader("Rentabilitäts- und Cashflow-Projektionen")
    st.warning("Nicht implementiert")

    # Steuerliche Aspekte
    st.subheader("Steuerliche Aspekte")
    st.warning("Nicht implementiert")

    # Risikobewertung
    st.subheader("Risikobewertung")
    st.warning("Nicht implementiert")
