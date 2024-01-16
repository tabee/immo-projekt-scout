import streamlit as st
import streamlit.components.v1 as components
from streamlit_searchbox import st_searchbox
from utils import search_function, set_featureid, get_html_popup_layer_urls_candidates_by_egid, get_bbox, get_html_popup_layer_urls_candidates_by_bbox, get_wohnungsregister
import streamlit as st
from app_utils import set_sessions_state, get_address, get_sidebar
from utils import get_expander_box
from streamlit_searchbox import st_searchbox

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


    id = st.session_state["ch.bfs.gebaeude_wohnungs_register.egaid"]
    bbox = get_bbox(id)
    iframe_candidates = get_html_popup_layer_urls_candidates_by_bbox(bbox, list=None)
    for if_compontent in iframe_candidates:
        st.write(if_compontent)
        components.iframe(if_compontent, width=705, height=400, scrolling=True)
        #components.iframe(if_compontent)
    #st.write(bbox)
    #bbox = get_bbox(st.session_state["ch.bfs.gebaeude_wohnungs_register.egaid"])
    #st.write(bbox)
    #components.iframe(f"https://api3.geo.admin.ch/rest/services/ech/MapServer/ch.bfs.gebaeude_wohnungs_register/{st.session_state['ch.bfs.gebaeude_wohnungs_register.egaid']}/extendedHtmlPopup?lang=de", width=705, height=1000, scrolling=True)
