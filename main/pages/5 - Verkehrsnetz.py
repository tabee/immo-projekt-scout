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
    
    # Strassennetz
    st.subheader("Strassennetz")
    get_expander_box(
        title_text="Strassennetz",
        list_of_layers = [
            "ch.astra.unfaelle-personenschaeden_alle",
            "ch.are.belastung-personenverkehr-strasse_zukunft",
            "ch.astra.hauptstrassennetz,ch.are.erreichbarkeit-miv",
            "ch.astra.nationalstrassenachsen",
            "ch.swisstopo.vec200-transportation-strassennetz",
            "ch.swisstopo.amtliches-strassenverzeichnis",
            "ch.astra.strassenverkehrszaehlung-uebergeordnet",
            "ch.are.belastung-personenverkehr-strasse",
            ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        description=None,
        height=150,
        display_map=True,
        zoom=6,
        is_expanded=False,
        hint="",
    )

    # Wanderrouten
    st.subheader("Wanderrouten")
    get_expander_box(
        title_text="Wanderwege",
        list_of_layers = [
            "ch.bafu.bundesinventare-amphibien_wanderobjekte",
            "ch.bafu.gewaesserschutz-biologischer_zustand_fische",
            "ch.swisstopo.swisstlm3d-wanderwege",
            "ch.astra.wanderland",
            "ch.bafu.amphibienwanderung-verkehrskonflikte",
            "ch.astra.wanderland-sperrungen_umleitungen",
            "ch.bafu.wrz-wildruhezonen_portal",
            "ch.bafu.wrz-jagdbanngebiete_select",
            ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        description=None,
        height=150,
        display_map=True,
        zoom=7,
        #is_expanded=False,
        hint="",
    )

    # Velorouten
    st.subheader("Velorouten")
    get_expander_box(
        title_text="Velorouten",
        list_of_layers = [
            "ch.astra.veloland",
            "ch.astra.veloland-sperrungen_umleitungen",
            "ch.astra.mountainbikeland",
            "ch.astra.skatingland-sperrungen_umleitungen",
            "ch.astra.skatingland",
            "ch.astra.unfaelle-personenschaeden_fahrraeder",
            ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        description=None,
        height=150,
        display_map=True,
        zoom=6,
        is_expanded=False,
        hint="",
    )
