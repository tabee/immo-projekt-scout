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
    default_zoom_this_page = 8
    default_is_expanded_this_page = False
    # end of repeated code


    # Stakeholder-Management
    st.title("stakeholder management")

    # Beziehungen zu Behörden und Regulierungsinstanzen
    st.subheader("Beziehungen zu Behörden und Regulierungsinstanzen")
    # TODO: add a streamlit or haystack agent to answer common questions.
    get_expander_box(title_text="Grundbuchinformationen (Amtliche Vermessung Schweiz)",
        list_of_layers = [
            "ch.swisstopo-vd.geometa-grundbuch",
    ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        hint="klappt nicht von selber auf, htmlPopup muss noch angepasst werden",
        height=200,
        is_expanded=default_is_expanded_this_page,
        display_map=False,
        )
    get_expander_box(title_text="Gemeindeinformationen (Amtliche Vermessung Schweiz)",
        list_of_layers = [
            "ch.swisstopo-vd.geometa-gemeinde",
        ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        hint=None,
        is_expanded=default_is_expanded_this_page,
        display_map=False,
        height=175
        )


    # Zusammenarbeit mit Beratern
    # @TODO: Lokale Partner wie Notare, Anwälte, Ingenieure, etc.
    st.subheader("Zusammenarbeit Beratern")
    get_expander_box(title_text="Öffentliche Energieberatungsstellen (Bundesamt für Energie BFE)",
        list_of_layers = [
            "ch.bfe.energieberatungsstellen",
        ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        hint="",
        height=320,
        is_expanded=default_is_expanded_this_page,
        display_map=False,
        )
    get_expander_box(title_text="Nachführungsgeometer/in",
        list_of_layers = [
            "ch.swisstopo-vd.geometa-nfgeom",
        ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        hint=None,
        description=None,
        display_map=False,
        height=170,
        is_expanded=default_is_expanded_this_page,
        )

    # Kommunikation mit Anwohnern und lokaler Gemeinschaft
    st.subheader("Kommunikation mit Anwohnern und lokaler Gemeinschaft")
    st.warning("Nicht implementiert.")
