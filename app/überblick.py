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


    st.title("überblick")
    
    st.subheader("Allgemeine Informationen")
    get_expander_box(title_text="Gemeinde",
        list_of_layers = [
            "ch.are.wohnungsinventar-zweitwohnungsanteil",
        ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        hint="",
        height=295,
        is_expanded=False,
        display_map=False,
    )    
    get_expander_box(title_text="Bauzone",
        list_of_layers = [
            "ch.are.bauzonen",
             ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        display_map=True,
        height=190,
        zoom=default_zoom_this_page,
        hint="",
        is_expanded=default_is_expanded_this_page,
    )
    get_expander_box(title_text="ÖREB Auszug und Grundstückinformationen",
        list_of_layers = [
            "ch.swisstopo-vd.stand-oerebkataster",
             ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        is_expanded=default_is_expanded_this_page,
        display_map=True,
        height=330,
        zoom=14,
        hint="",
    )
    get_expander_box(title_text="Eidg. Gebäude- und Wohnungsregister",
        list_of_layers = [
            "ch.bfs.gebaeude_wohnungs_register",
            ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        is_expanded=False,
        display_map=True,
        height=800,
        hint="",
    )


    async def get_wohnungsregister(self, feature_id):
        ''' Get the wohnungsregister for a given feature id '''
        object_url = f"https://api3.geo.admin.ch/rest/services/api/MapServer/ch.bfs.gebaeude_wohnungs_register/{feature_id}"
        object_data = await self._fetch_object_data(object_url)
        return object_data