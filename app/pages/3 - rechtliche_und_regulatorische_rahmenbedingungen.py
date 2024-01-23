import streamlit as st
from app_utils import set_sessions_state, get_address, get_sidebar, display_pdf
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


    # Rechtliche und regulatorische Rahmenbedingungen
    st.title("rechtliche und regulatorische rahmenbedingungen")

    # Zoning und Landnutzungsvorschriften
    st.subheader("Landnutzungsvorschriften")
    get_expander_box(title_text="Bauzone",
        list_of_layers = [
            "ch.are.bauzonen",
        ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        hint="",
        height=200,
        display_map=True,
        )

    # Baurechtliche Bestimmungen
    st.subheader("Baurechtliche Bestimmungen")    
    
    # ÖREB-Kataster
    get_expander_box(title_text="ÖREB-Kataster: Verfügbarkeit der Informationen (Bundesamt für Landestopografie swisstopo)",
        list_of_layers = [
            "ch.swisstopo-vd.stand-oerebkataster",
        ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        hint="",
        height=350,
        display_map=True,
        )
    pdf_url_oreb_kanton_bern = f"https://www.oereb2.apps.be.ch/extract/pdf?egrid={st.session_state['ch.bfs.gebaeude_wohnungs_register.egrid']}&lang=de"
    st.write("ÖREB-Kataster (PDF):")
    display_pdf(pdf_url_oreb_kanton_bern, iframe_width+5)   

    # Umweltschutzauflagen
    st.subheader("Umweltschutzauflagen")
    # TODO: Archäologische Inventar
    st.info("Teilweise implementiert.\n (Archäologische Inventar, usw.)")
    get_expander_box(title_text="Wald",
        list_of_layers = [
            "ch.swisstopo.swisstlm3d-wald",
            "ch.bafu.waldreservate",
        ],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        is_expanded=False,
        display_map=True,
        hint="",
        )
    get_expander_box(title_text="Moorlandschaft",
        list_of_layers = [
             "ch.bafu.bundesinventare-moorlandschaften",
            "ch.bafu.bundesinventare-hochmoore",
            "ch.bafu.bundesinventare-flachmoore"],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        is_expanded=False,
        display_map=True,
        hint="",
        )


    # Denkmalschutz
    st.subheader("Denkmalschutz")
    # TODO: Denkmalschutz, umfangreichere Liste finden.
    get_expander_box(title_text="Kulturgüterschutzinventar (KGS)",
        list_of_layers = [
            "ch.babs.kulturgueter"],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        hint="",
        description="Als Kulturgüter von nationaler Bedeutung im Inventar von 2021 gelten rund 3400 Objekte (Einzelbauten / Sammlungen in Museeen, Archiven und Bibliotheken sowie Archäologie).",
        height=350,
        display_map=True,
        )
    st.info("Teilweise implementiert.\n Muss umfangreicher sein.")

    # Dienstbarkeiten
    st.subheader("Dienstbarkeiten")
    st.warning("Nicht implementiert")

    st.subheader("Bauinventar")
    st.warning("Nicht fertig implementiert")
    get_expander_box(title_text="Hecken und Bäume",
        list_of_layers = [
            "ch.swisstopo.vec25-heckenbaeume"],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        is_expanded=False,
        display_map=True,
        hint="",
        description="Die Ebene Hecken und Bäume (Abkürzung heb) umfasst Punkt- und Linienobjekte der Vegetation. Die Objekte werden aufgrund des Kartenbildes teilautomatisiert erfasst.",
    )


    # Eigentumsverhältnisse und Grundbuchangelegenheiten
    st.subheader("Eigentumsverhältnisse und Grundbuchangelegenheiten")
    #  TODO: get number of the parcel (from ch.swisstopo-vd.stand-oerebkataster by bbox or feature_id)? )
    st.markdown(f"""
                Diesen Link anklicken:
                [Geoportal - Kanton Bern](https://www.map.apps.be.ch/pub/externalcall.jsp?query1=egrid&keyvalue1={st.session_state['ch.bfs.gebaeude_wohnungs_register.egrid']}&keyname1=EGRID&project=a42pub_oereb_oeffen_DE&language=de&userprofile=geo&client=auto)
                und dort auf den Button 'Auskunft geben' klicken. Dann auf die Parzell klicken und das CAPTCHA ausfüllen.""", unsafe_allow_html=True)



