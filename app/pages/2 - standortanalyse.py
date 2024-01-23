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


    st.title("Standortanalyse")

    # Geografische Lage
    st.subheader("Geografische Lage")
    st.warning("Geografische Lage, Topologie, ISOS, Ordsbildperimeter, etc.")

    # Verkehrsanbindung und Infrastruktur
    st.subheader("Verkehrsanbindung und Infrastruktur")
    st.warning("Verkehrsanbindung und Infrastruktur")

    # Strassennetz
    st.subheader("Strassennetz")
    get_expander_box(title_text="Strassennetz",
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
        zoom=default_zoom_this_page,
        is_expanded=default_is_expanded_this_page,
        hint="",
    )
    get_expander_box(title_text="Wanderwege",
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
        zoom=default_zoom_this_page,
        is_expanded=default_is_expanded_this_page,
        hint="",
    )
    get_expander_box(title_text="Velorouten",
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
        zoom=default_zoom_this_page,
        is_expanded=default_is_expanded_this_page,
        hint="",
    )
    get_expander_box(title_text="Inventar der historischen Verkehrswege",
        list_of_layers = [
            "ch.astra.ivs-reg_loc"],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        display_map=True,
        zoom=default_zoom_this_page,
        is_expanded=default_is_expanded_this_page,
        hint="",
    )

    # Nähe zu wichtigen Einrichtungen
    st.subheader("Nähe zu wichtigen Einrichtungen")
    st.warning("Nähe zu wichtigen Einrichtungen  (z.B. Schulen, Krankenhäuser)")

    # Umgebungsqualität
    st.subheader("Umgebungsqualität")
    st.warning("Nicht fertig implementiert(Schulen, Dorfleistungen, etc.)") 
    get_expander_box(title_text="Festnetz-Dienstanbieter",
        list_of_layers = [
            "ch.bakom.anbieter-eigenes_festnetz",
        ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        hint="",
        height=90,
        display_map=False,
        zoom=default_zoom_this_page,
        is_expanded=default_is_expanded_this_page,
        )
    get_expander_box(title_text="Glasfaser und Downlink 1000",
        list_of_layers = [
            "ch.bakom.anschlussart-glasfaser",
            "ch.bakom.downlink1000",
        ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        hint="",
        height=150,
        display_map=True,
        zoom=default_zoom_this_page,
        is_expanded=default_is_expanded_this_page,
        )
    
    # Landwirschaft aussenhalb der Bauzone    
    st.subheader("Ausserhalb der Bauzone")
    get_expander_box(title_text="Landwirtschaftliche Zonengrenzen der Schweiz (Bundesamt für Landwirtschaft BLW)",
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
        height=320,
        display_map=True,
        zoom=default_zoom_this_page,
        is_expanded=default_is_expanded_this_page,
        hint="",
        )
    get_expander_box(title_text="Klimaeignungskarte für die Landwirtschaft (Kulturland / Fruchtfolgeflächen)",
        list_of_layers = [
            "ch.blw.klimaeignung-typ",
        ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        height=90,
        display_map=True,
        zoom=default_zoom_this_page,
        is_expanded=default_is_expanded_this_page,
        hint="",
        )
