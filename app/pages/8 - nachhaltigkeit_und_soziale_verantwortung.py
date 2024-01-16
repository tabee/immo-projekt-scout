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


    # Nachhaltigkeit und soziale Verantwortung
    st.title("Nachhaltigkeit und soziale Verantwortung")

    # Umweltverträglichkeit
    st.subheader("Umweltverträglichkeit")
    st.warning("Nicht implementiert")

    # Energie- und Ressourceneffizienz
    st.subheader("Energie- und Ressourceneffizienz")
    st.warning("Nicht implementiert")

    # Beitrag zur lokalen Gemeinschaft
    st.subheader("Beitrag zur lokalen Gemeinschaft")
    st.warning("Nicht implementiert")
    
    # Langfristige Wertstabilität
    st.subheader("Langfristige Wertstabilität")
    st.warning("Nicht implementiert")