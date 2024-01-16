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
    

    st.subheader("Baurechtliche Grundordnung")
    st.warning("Nicht implementiert")

    st.subheader("Baubebewilligungskompetenz")
    
    # Energieberatungsstellen
    get_expander_box(
        title_text="Öffentliche Energieberatungsstellen (Bundesamt für Energie BFE)",
        list_of_layers = [
            "ch.bfe.energieberatungsstellen",
        ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        hint="klappt nicht von selber auf, htmlPopup muss noch angepasst werden",
        height=320,
        display_map=False,
        )


    # Grundbuchinformationen (Amtliche Vermessung Schweiz)
    get_expander_box(
        title_text="Grundbuchinformationen (Amtliche Vermessung Schweiz)",
        list_of_layers = [
            "ch.swisstopo-vd.geometa-grundbuch",
    ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        hint="klappt nicht von selber auf, htmlPopup muss noch angepasst werden",
        height=200,
        display_map=False,
        )
    
    # ÖREB-Kataster
    get_expander_box(
        title_text="ÖREB-Kataster: Verfügbarkeit der Informationen (Bundesamt für Landestopografie swisstopo)",
        list_of_layers = [
            "ch.swisstopo-vd.stand-oerebkataster",
        ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        hint="klappt nicht von selber auf, htmlPopup muss noch angepasst werden",
        height=350,
        display_map=False,
        )

    st.subheader("Kontakt Leitbehörden")
    
    # Nachführungsgeometer/in
    get_expander_box(
        title_text="Nachführungsgeometer/in",
        list_of_layers = [
            "ch.swisstopo-vd.geometa-nfgeom",
        ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        hint=None,
        description=None,
        display_map=False,
        height=170
        )

    # Gemeindeinformationen (Amtliche Vermessung Schweiz)
    get_expander_box(
        title_text="Gemeindeinformationen (Amtliche Vermessung Schweiz)",
        list_of_layers = [
            "ch.swisstopo-vd.geometa-gemeinde",
        ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        hint=None,
        description=None,
        display_map=False,
        height=175
        )