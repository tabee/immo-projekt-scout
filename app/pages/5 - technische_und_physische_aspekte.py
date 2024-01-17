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


    # Technische und physische Aspekte
    st.title("Technische und physische Aspekte")

    st.subheader("Geologische und topografische Aspekte")
    get_expander_box(title_text="Steine",
        list_of_layers = [
            "ch.swisstopo.geologie-geocover"],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        height=260,
        is_expanded=default_is_expanded_this_page,
        zoom=default_zoom_this_page,
        display_map=True,
        hint="",
    )

    # Bauzustand und -qualität
    st.subheader("Bauzustand und -qualität")
    st.warning("Bauzustand und -qualität")

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
        zoom=11,
        display_map=True,
        hint="",
    )
    get_expander_box(title_text="Energieberatungsstelle",
        list_of_layers = [
                "ch.bfe.energieberatungsstellen",
            ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        height=280,
        is_expanded=default_is_expanded_this_page,
        zoom=default_zoom_this_page,
        display_map=False,
        hint="",
    )


    # Zugänglichkeit und Barrierefreiheit
    st.subheader("Zugänglichkeit und Barrierefreiheit")
    st.warning("Zugänglichkeit und Barrierefreiheit")

    # Notwendige Sanierungen oder Umbauten
    st.subheader("Notwendige Sanierungen oder Umbauten")
    st.warning("Notwendige Sanierungen oder Umbauten")

    # Bodenbeschaffenheit und geologische Risiken
    st.subheader("Bodenbeschaffenheit und geologische Risiken")
    st.warning("Bodenbeschaffenheit und geologische Risiken")




    # Naturgefahrenereignisse
    st.subheader("Naturgefahrenereignisse")
    # TODO: Erdbeben   
    get_expander_box(title_text="Radon",
        list_of_layers = [
            "ch.bag.radonkarte",
            ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        description=None,
        height=150,
        display_map=False,
        is_expanded=default_is_expanded_this_page,
    )
    get_expander_box(title_text="Uran",
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
        is_expanded=default_is_expanded_this_page,
    )
    

    # Wasser
    st.subheader("Wasser")
    # TODO: Versickerung
    get_expander_box(title_text="Grundwasser",
        list_of_layers = [
            "ch.bafu.grundwasserkoerper",
            "ch.bafu.hydroweb-messstationen_grundwassertemperatur",
            ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        description=None,
        height=200,
        display_map=True,
        is_expanded=default_is_expanded_this_page,
        zoom=default_zoom_this_page,
        hint="",
    )
    get_expander_box(title_text="Vernässung",
        list_of_layers = [
            "ch.blw.bodeneignung-vernaessung", 
            ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        height=90,
        display_map=True,
        is_expanded=default_is_expanded_this_page,
        zoom=default_zoom_this_page,
        description="Wenn ausser dem Niederschlagswasser noch Fremdwasser (Hang- oder Grundwasser) im Boden vorhanden ist",
        hint="",
    )
    get_expander_box(title_text="Gewaesseranschlusskarte",
        list_of_layers = [
            "ch.blw.gewaesseranschlusskarte",
            "ch.blw.gewaesseranschlusskarte-direkt",
            ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        description=None,
        height=100,
        display_map=True,
        is_expanded=default_is_expanded_this_page,
        zoom=default_zoom_this_page,
        hint="",
    )
    get_expander_box(title_text="Wärmeentzug und Wärmeeinleitung",
        list_of_layers = [
            "ch.bfe.waermepotential-gewaesser",
            ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        description=None,
        height=100,
        display_map=True,
        is_expanded=default_is_expanded_this_page,
        zoom=default_zoom_this_page,
        hint="",
    )
    get_expander_box(title_text="Oberflächenabfluss",
        list_of_layers = [
            "ch.bafu.gefaehrdungskarte-oberflaechenabfluss"],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
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
        is_expanded=default_is_expanded_this_page,
        zoom=default_zoom_this_page,
        hint="",
    )


    # Altlasten
    st.subheader("Altlasten")
    st.warning("Nicht implementiert")