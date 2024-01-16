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
    
    # Altlasten
    st.subheader("Altlasten")
    st.warning("Nicht implementiert")

    # Zweitwohnungen
    st.subheader("Zweitwohnungen")
    get_expander_box(
        title_text="Wohnungsinventar / Zweitwohnungsanteil",
        list_of_layers = [
            "ch.are.wohnungsinventar-zweitwohnungsanteil",
        ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        hint="klappt nicht von selber auf, htmlPopup muss noch angepasst werden",
        height=320,
        display_map=False,
    )

    # Dienstbarkeiten
    st.subheader("Dienstbarkeiten")
    st.warning("Nicht implementiert")