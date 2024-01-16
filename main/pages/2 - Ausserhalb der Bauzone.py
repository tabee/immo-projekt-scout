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

    st.subheader("Telekommunikation (Festnetz-Dienstanbieter)")
   
    get_expander_box(
        title_text="Dienstanbieter und Downlink 1000",
        list_of_layers = [
            "ch.bakom.anbieter-eigenes_festnetz",
            "ch.bakom.downlink1000",
        ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        hint="",
        height=150,
        display_map=True,
        zoom=7,
        is_expanded=False,
        )


    st.subheader("Landwirtschaftszone")
    
    # Landwirtschaftliche Zonengrenzen (blw,bafu)
    get_expander_box(
        title_text="Landwirtschaftliche Zonengrenzen der Schweiz (Bundesamt für Landwirtschaft BLW)",
        list_of_layers = [
            "ch.blw.landwirtschaftliche-zonengrenzen",
            "ch.bafu.ren-extensive_landwirtschaftsgebiete",
        ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        description=""" Der Geobasisdatensatz der 
                        landwirtschaftlichen Zonen und Gebiete besteht aus 
                        sechs landwirtschaftlichen Produktionszonen und dem 
                        Sömmerungsgebiet und bildet den landwirtschaftlichen 
                        Produktionskataster. Verschiedene Massnahmen im Bereich 
                        des Landwirtschaftsgesetzes sind auf die Zoneneinteilung 
                        abgestützt. Ein Teil der Direktzahlungen an die 
                        Landwirtschaft beispielsweise wird differenziert 
                        nach Zonenzugehörigkeit ausgerichtet. """,
        hint="klappt nicht von selber auf, htmlPopup muss noch angepasst werden",
        height=320,
        display_map=True,
        )


    st.subheader("Kulturland / Fruchtfolgeflächen")
    
    # Klimaeignungskarte für die Landwirtschaft
    get_expander_box(
        title_text="Klimaeignungskarte für die Landwirtschaft ",
        list_of_layers = [
            "ch.blw.klimaeignung-typ",
        ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        height=90,
        display_map=True,
        is_expanded=False,
        )

