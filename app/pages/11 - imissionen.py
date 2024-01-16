import streamlit as st
from app_utils import set_sessions_state, get_address, get_sidebar, display_pdf
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
    default_zoom_this_page = 8
    default_is_expanded_this_page = False
    # end of repeated code

    st.title("immissionen")
    
    # Verkehrsbelastung
    st.subheader("Verkehrsbelastung")
    get_expander_box(title_text="Personenverkehr (Strasse und Schiene)",
        list_of_layers = [
            "ch.astra.strassenverkehrszaehlung-uebergeordnet",
            "ch.are.belastung-personenverkehr-strasse",
            "ch.are.belastung-personenverkehr-bahn",
        ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        height=320,
        zoom=default_zoom_this_page,
        hint="",
        is_expanded=default_is_expanded_this_page,
        display_map=True,
    )

    # Lärmquellen
    st.subheader("Lärmquellen")
    get_expander_box(title_text="Strassenlärm (Tag)",
        list_of_layers = [
            "ch.bafu.laerm-strassenlaerm_tag",
        ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        height=320,
        zoom=default_zoom_this_page,
        hint="",
        is_expanded=default_is_expanded_this_page,
        display_map=True,
    )
    get_expander_box(title_text="Strassenlärm (Nacht)",
        list_of_layers = [
            "ch.bafu.laerm-strassenlaerm_nacht",
        ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        height=320,
        zoom=default_zoom_this_page,
        hint="",
        is_expanded=default_is_expanded_this_page,
        display_map=True,
    )
    get_expander_box(title_text="Eisenbahn (Tag)",
        list_of_layers = [
            "ch.bafu.laerm-bahnlaerm_tag",
            "ch.bav.laermbelastung-eisenbahn_effektive_immissionen_tag",
        ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        height=320,
        zoom=default_zoom_this_page,
        hint="",
        is_expanded=default_is_expanded_this_page,
        display_map=True,
    )
    get_expander_box(title_text="Eisenbahn (Nacht)",
        list_of_layers = [
            "ch.bav.laermbelastung-eisenbahn_effektive_immissionen_nacht",
            "ch.bafu.laerm-bahnlaerm_nacht",
        ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        height=320,
        zoom=default_zoom_this_page,
        hint="",
        is_expanded=default_is_expanded_this_page,
        display_map=True,
    )

    # Antennenstandorte / Richtfunkverbindungen
    st.subheader("Hochfrequenzstrahlung (HF-Strahlung)")
    get_expander_box(
        title_text="Antennenstandorte / Richtfunkverbindungen",
        list_of_layers = [
            "ch.bakom.richtfunkverbindungen",
            "ch.bakom.mobil-antennenstandorte-gsm",
            "ch.bakom.mobil-antennenstandorte-umts",
            "ch.bakom.mobil-antennenstandorte-lte",
            "ch.bakom.mobil-antennenstandorte-5g",
        ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        height=320,
        zoom=default_zoom_this_page,
        hint="",
        is_expanded=default_is_expanded_this_page,
        display_map=True,
    )

    # Hochspannungsleitungen
    st.subheader("Hochspannungsleitungen")
    get_expander_box(title_text="Elektrische Anlagen mit einer Nennspannung von über 36",
        list_of_layers = [
            "ch.bfe.elektrische-anlagen_ueber_36",
        ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        height=320,
        zoom=default_zoom_this_page,
        hint="",
        is_expanded=default_is_expanded_this_page,
        display_map=True,
    )
