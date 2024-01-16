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
    
    # Verkehrsbelastung
    st.subheader("Verkehrsbelastung")
    st.warning("Nicht implementiert")

    # Lärmquellen
    st.subheader("Lärmquellen")
    get_expander_box(
        title_text="Eisenbahnverkehrslärm",
        list_of_layers = [
            "ch.bafu.laerm-bahnlaerm_nacht",
            "ch.bafu.laerm-bahnlaerm_tag",
            "ch.bav.laermbelastung-eisenbahn_festgelegte_emissionen_nacht",
            "ch.bav.laermbelastung-eisenbahn_festgelegte_emissionen_tag",
        ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        height=320,
        zoom=8,
        hint="",
        is_expanded=True,
        display_map=True,
    )

    # Mobilfunk
    st.subheader("Mobilfunk")
    st.warning("Nicht implementiert")

    # Hochspannungsleitungen
    st.subheader("Hochspannungsleitungen")
    get_expander_box(
        title_text="Elektrische Anlagen mit einer Nennspannung von über 36",
        list_of_layers = [
            "ch.bfe.elektrische-anlagen_ueber_36",
        ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        height=320,
        zoom=4,
        hint="",
        is_expanded=True,
        display_map=True,
    )

    # Bahn
    st.subheader("Bahn")
    st.warning("Nicht implementiert")

    # ÖREB-Kataster
    st.subheader("ÖREB-Kataster")
    st.warning("Nicht implementiert")

    # Waldinformationen
    st.subheader("Waldinformationen")
    st.warning("Nicht implementiert")
