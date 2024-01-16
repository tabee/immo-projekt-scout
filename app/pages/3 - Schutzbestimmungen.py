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
    
    st.subheader("Archäologische Inventar")
    st.warning("Nicht implementiert")

    st.subheader("Bauinventar")
    st.warning("Nicht implementiert")

    # Kulturgüterschutzinventar (KGS)
    st.subheader("Kulturgüterschutzinventar (KGS)")
    get_expander_box(
        title_text="Kulturgüterschutzinventar (KGS)",
        list_of_layers = [
            "ch.babs.kulturgueter"],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        hint="klappt nicht von selber auf, htmlPopup muss noch angepasst werden",
        description="Als Kulturgüter von nationaler Bedeutung im Inventar von 2021 gelten rund 3400 Objekte (Einzelbauten / Sammlungen in Museeen, Archiven und Bibliotheken sowie Archäologie)."
        )
    
    # Steininventar
    st.subheader("Steininventar")
    get_expander_box(
        title_text="Geologische Vektordatensätze GeoCover (Bundesamt für Landestopografie swisstopo)",
        list_of_layers = [
            "ch.swisstopo.geologie-geocover"],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        height=260,
    )
    
    # Historischer Verkehrsweg
    st.subheader("Historischer Verkehrsweg")
    get_expander_box(
        title_text="Inventar der historischen Verkehrswege",
        list_of_layers = [
            "ch.astra.ivs-reg_loc"],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        is_expanded=False,
        zoom=8,
        hint="",
    )

    # Ortsbild (ISOS, Ordsbildperimeter)
    st.subheader("Ortsbild (ISOS, Ordsbildperimeter)")
    st.warning("Nicht implementiert")

    # Heckend und Feldgehölze
    st.subheader("Heckend und Feldgehölze")

    # Hecken und Bäume
    get_expander_box(
        title_text="Hecken und Bäume",
        list_of_layers = [
            "ch.swisstopo.vec25-heckenbaeume"],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width,
        zoom=8,
        description="Die Ebene Hecken und Bäume (Abkürzung heb) umfasst Punkt- und Linienobjekte der Vegetation. Die Objekte werden aufgrund des Kartenbildes teilautomatisiert erfasst.",
    )

    # Flach- Hoch- und Übergangsmoore
    st.subheader("Flach- Hoch- und Übergangsmoore")
    st.warning("Nicht implementiert")

    # Naturschutzgebiet
    st.subheader("Naturschutzgebiet")
    st.warning("Nicht implementiert")

    # Bundesinventar der Landschaften und Naturdenkmäler von nationaler Bedeutung (BLN)
    st.subheader("Bundesinventar der Landschaften und Naturdenkmäler von nationaler Bedeutung (BLN)")
    st.warning("Nicht implementiert")

    # Moorlandschaft
    get_expander_box(
        title_text="Moorlandschaft",
        list_of_layers = [
             "ch.bafu.bundesinventare-moorlandschaften",
            "ch.bafu.bundesinventare-hochmoore",
            "ch.bafu.bundesinventare-flachmoore"],
        e_gebäude_koord=e_gebäude_koord,
        n_gebäude_koord=n_gebäude_koord,
        iframe_width=iframe_width)





    







   

    


    







    
    
    # # display html popup when we find one
    # selected_layers = [
    #     "ch.bafu.bundesinventare-moorlandschaften",
    #     "ch.bafu.bundesinventare-hochmoore",
    #     "ch.bafu.bundesinventare-flachmoore"]
    # bbox = get_bbox(st.session_state["ch.bfs.gebaeude_wohnungs_register.egaid"])
    # iframe_components = get_html_popup_layer_urls_candidates_by_bbox(bbox, selected_layers)
    # if iframe_components:
    #     is_expanded = True
    #     text = ""
    # else:
    #     is_expanded = False
    #     text = " - Keine Informationen vorhanden."
    
    # with st.expander(("Moorlandschaft" + text), expanded=is_expanded):
        
    #     for comp in iframe_components:
    #         components.iframe(comp, width=iframe_width, height=145, scrolling=True)

    #     # display map
    #     layers = "ch.bafu.bundesinventare-flachmoore,ch.bafu.bundesinventare-hochmoore,ch.bafu.schutzgebiete-aulav_moorlandschaften"
    #     components.iframe(f'https://map.geo.admin.ch/embed.html?E={e_gebäude_koord}&N={n_gebäude_koord}&time=None&lang=de&notooltip=false&topic=ech&crosshair=bowl&zoom=11&bgLayer=ch.swisstopo.pixelkarte-grau&layers={layers}', width=iframe_width, height=420)




    # with st.expander("Kontakt Leitbehörden", expanded=True):

    #     st.write("Nachführungsgeometer/in")
        
    #     selected_layers_bbox = [
    #         "ch.swisstopo-vd.geometa-nfgeom",
    #         ]
    #     bbox = get_bbox(st.session_state["ch.bfs.gebaeude_wohnungs_register.egaid"])
    #     foo = get_html_popup_layer_urls_candidates_by_bbox(bbox, selected_layers_bbox)
    #     for comp in foo:
    #         components.iframe(comp, width=680, height=170, scrolling=True)
        
