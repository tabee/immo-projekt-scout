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
    st.subheader("Gewässernetz")
    st.warning("Nicht implementiert")
    # pServer/ch.bafu.wasser-teileinzugsgebiete_2/140988/htmlPopup?lang=de

    # Gewässerschutz
    st.subheader("Gewässerschutz")
    st.warning("Nicht implementiert")

    # Grundwasservorkommen
    st.subheader("Grundwasservorkommen")
    get_expander_box(
        title_text="Grundwasser",
        list_of_layers = [
            "ch.swisstopo.geologie-hydrogeologische_karte-grundwasservulnerabilitaet",
            "ch.bafu.grundwasserkoerper",
            "ch.bafu.hydroweb-messstationen_grundwassertemperatur",
            "ch.bafu.hydroweb-messstationen_grundwasserzustand",
            "ch.blw.bodeneignung-vernaessung",
            "ch.bafu.naqua-grundwasser_voc",          
            ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        description=None,
        height=100,
        display_map=True,
        zoom=7,
        #is_expanded=False,
        hint="",
    )

    # Grundwassernutzung
    st.subheader("Grundwassernutzung, Gewässeranschlusskarte")
    get_expander_box(
        title_text="Gewaesseranschlusskarte, Gewässerwärmepotential",
        list_of_layers = [
            "ch.blw.gewaesseranschlusskarte",
            "ch.blw.gewaesseranschlusskarte-direkt",
            "ch.bfe.waermepotential-gewaesser",
            ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        description=None,
        height=100,
        display_map=True,
        #is_expanded=False,
        hint="",
    )

    # Erdwärmesonden 
    st.subheader("Erdwärmesonden (Bewilligung)")
    st.warning("Nicht implementiert")

    # Versickerung
    st.subheader("Versickerung")
    get_expander_box(
        title_text="Feuchtflächenpotential der offenen Kulturlandschaft",
        list_of_layers = [
            "ch.agroscope.feuchtflaechenpotential-kulturlandschaft",  
            ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        description="Das Feuchtflächenpotential wurde anhand der Prozesse Wasserakkumulation und Versickerung beurteilt.",
        height=100,
        display_map=True,
        zoom=7,
        #is_expanded=False,
        hint="",
    )

