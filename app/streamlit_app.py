import streamlit as st
import streamlit.components.v1 as components
from app_utils import set_sessions_state, get_address, get_sidebar
from utils import get_expander_box, get_wohnungsregister

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

    # Eidg. Gebäude- und Wohnungsregister: Gebäudestatus
    st.subheader("Gebäudestatus")
    get_expander_box(
        title_text="Eidg. Gebäude- und Wohnungsregister",
        list_of_layers = [
            "ch.bfs.gebaeude_wohnungs_register",
        ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        height=1300,
        display_map=True,
        is_expanded=True,
        )
    
    # todo: https://api3.geo.admin.ch/rest/services/api/MapServer/ch.swisstopo-vd.amtliche-vermessung/1518578194/htmlPopup?lang=de
    # https://api3.geo.admin.ch/rest/services/api/MapServer/ch.swisstopo-vd.stand-oerebkataster/1025996/htmlPopup?lang=de

    # Agglomerationsgrenzen (G1 und G2)
    st.subheader("Agglomerationsgrenzen (G1 und G2)")
    get_expander_box(
        title_text="Agglomerationsgrenzen (G1 und G2)",
        list_of_layers = [
            "ch.bfs.gebaeude_wohnungs_register_waermequelle_heizung",
            "ch.bfs.generalisierte-grenzen_agglomerationen_g1",
            "ch.bfs.generalisierte-grenzen_agglomerationen_g2",
        ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        hint="klappt nicht von selber auf, htmlPopup muss noch angepasst werden",
        height=150,
        display_map=False,
        )
