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
    
    # Naturgefahren
    st.subheader("Naturgefahren")
    st.warning("Nicht implementiert")

    # Oberflächenabfluss
    st.subheader("Oberflächenabfluss")
    get_expander_box(
        title_text="Oberflächenabfluss",
        list_of_layers = [
            "ch.bafu.gefaehrdungskarte-oberflaechenabfluss"],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        hint="",
        description=""" Die in der Gefährdungskarte Oberflächenabfluss dargestellten 
                        Überschwemmungsgebiete wurden über das gesamte Gebiet der 
                        Schweiz und von Liechtenstein mit einer einheitlichen Methode 
                        erstellt. Sie beruhen auf einer Modellierung ohne Verifizierung 
                        oder Plausibilisierung im Gelände. Sie kennzeichnen diejenigen 
                        Gebiete, die bei seltenen bis sehr seltenen Ereignissen potenziell 
                        beroffen sind. Sie geben eine grobe Gesamtübersicht über die 
                        Gefährdung durch Oberflächenabfluss. Sie kennzeichnen nicht die 
                        Gebiete, die durch Überschwemmung aus Fliessgewässern betroffen 
                        sind und berücksichtigen keine Schutzbauten oder 
                        Strassenunterführungen oder Durchlässe in Bahndämmen (so erscheinen 
                        bspw. SBB-Dämme im DTM als durchgehender Damm ohne Durchlass). 
                        Diese Karte erlaubt eine Grobaschätzung über die Gefährdung durch 
                        Oberflächenabfluss, sofern keine detaillierte Gefahrenkarte vorhanden 
                        ist. Die geschätzte Wiederkehrperiode ist grösser als 100 Jahre, das 
                        heisst, dass über lange Sicht gesehen ein solches Ereignis im Mittel 
                        einmal in hundert Jahren auftritt. Es ist nicht auszuschliessen, dass 
                        Oberflächenabfluss auch auf Flächen auftritt, die in der Karte als nicht 
                        betroffen erscheinen. Sie darf nicht in einem Massstab verwendet werden, 
                        der detaillierter als 1:12‘500 (Liechtenstein: 1: 10'000) ist, um Fehler 
                        in der Interpretation von betroffenen und nicht betroffenen Gebieten zu 
                        vermeiden. Die Karte hat keine Rechtsverbindlichkeit, es steht aber den 
                        Kantonen frei, sie als Gefahrenhinweiskarte in ihre Gefahrengrundlagen 
                        zu übernehmen und sie im kantonalen Geoportal zu publizieren.""",
        height=320,
        display_map=True,
    )

    # Naturgefahrenereignisse
    st.subheader("Naturgefahrenereignisse")
    st.warning("Nicht implementiert")
    
    # Radon
    st.subheader("Radon")
    get_expander_box(
        title_text="Radon",
        list_of_layers = [
            "ch.bag.radonkarte",
            ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        description=None,
        height=150,
        display_map=False,
    )

    # Uran
    st.subheader("Uran")
    get_expander_box(
        title_text="Uran",
        list_of_layers = [
            "ch.bafu.geochemischer-bodenatlas_schweiz_uran",
            ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        description=None,
        height=150,
        hint="",
        zoom=1,
        display_map=True,
    )
    
    # Erdbeben
    st.subheader("Erdbeben")
    get_expander_box(
        title_text="Seismischen Baugrundklassen",
        list_of_layers = [
            "ch.bafu.gefahren-baugrundklassen",
            ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        description=None,
        height=100,
        display_map=True,
    )