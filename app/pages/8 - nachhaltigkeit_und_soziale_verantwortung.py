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
    default_zoom_this_page = 14
    default_is_expanded_this_page = False
    # end of repeated code


    # Nachhaltigkeit und soziale Verantwortung
    st.title("Nachhaltigkeit und soziale Verantwortung")

    # Umweltverträglichkeit
    st.subheader("Umweltverträglichkeit")
    st.warning("Nicht implementiert")

    # Energie- und Ressourceneffizienz
    st.subheader("Energie- und Ressourceneffizienz")
    st.warning("Nicht implementiert")


    # Energieeffizienz und Nachhaltigkeit
    st.subheader("Energieeffizienz und Nachhaltigkeit")
    # TODO: Erdwärmesonden (Bewilligung)
    get_expander_box(title_text="Solarenergieeignung",
        list_of_layers = [
            "ch.bfe.elektrizitaetsproduktionsanlagen",
            "ch.bfe.solarenergie-eignung-daecher",
            #"ch.bfe.solarenergie-eignung-fassaden",
            ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        height=220,
        is_expanded=default_is_expanded_this_page,
        zoom=default_zoom_this_page,
        display_map=True,
        hint="",
    )
    get_expander_box(title_text="Thermische Netze",
        list_of_layers = [
                "ch.bfe.thermische-netze",
            ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        height=280,
        is_expanded=default_is_expanded_this_page,
        zoom=8,
        display_map=True,
        hint="",
    )
    get_expander_box(title_text="Geothermiepotenzial",
        list_of_layers = [
                "ch.swisstopo.geologie-geologische_3dmodelle",
                "ch.swisstopo.geologie-geothermische_potenzialstudien_regional",
            ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        height=165,
        is_expanded=default_is_expanded_this_page,
        zoom=11,
        display_map=False,
        hint="",
    )
    get_expander_box(title_text="Windenenergiepotenzial",
        list_of_layers = [
                "ch.bfe.windenergie-geschwindigkeit_h75",
            ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        height=530,
        is_expanded=default_is_expanded_this_page,
        zoom=7,
        display_map=True,
        hint="",
    )
    get_expander_box(title_text="Windenergie Einschränkungen",
        list_of_layers = [
                "ch.are.windenergie-bundesinteressen",
            ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        height=220,
        is_expanded=default_is_expanded_this_page,
        zoom=7,
        display_map=True,
        hint="",
    )

    # Beitrag zur lokalen Gemeinschaft
    st.subheader("Beitrag zur lokalen Gemeinschaft")
    st.warning("Nicht implementiert")
    
    # Langfristige Wertstabilität
    st.subheader("Langfristige Wertstabilität")
    st.warning("Nicht implementiert")