''' States and Components for the Streamlit App '''
import requests
from io import BytesIO
import base64
from pathlib import Path
from requests.exceptions import RequestException
from io import BytesIO
from requests.exceptions import RequestException
import streamlit as st
from streamlit_searchbox import st_searchbox
from utils import get_bbox, get_wohnungsregister, set_featureid, search_function

def _download_pdf(url):
    ''' Herunterladen und Speichern des PDFs im Speicher. '''
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Löst eine Ausnahme aus, wenn der Statuscode kein 200 ist
        return BytesIO(response.content)
    except RequestException as e:
        print(f"Fehler beim Herunterladen des PDFs: {e}")
        return None
    
def display_pdf(url, iframe_width):
    ''' Anzeigen des PDFs im Streamlit-App. '''
    
    with st.spinner('Lade Daten...'):
        try:
            pdf_in_memory = _download_pdf(url)
            # Lesen Sie die Daten aus dem BytesIO-Objekt und kodieren Sie sie in Base64
            base64_pdf = base64.b64encode(pdf_in_memory.getvalue()).decode("utf-8")
        except:
            st.error("Fehler beim Herunterladen des PDFs. Bitte versuchen Sie es später erneut.")
    
    # Überprüfen Sie, ob das PDF erfolgreich heruntergeladen wurde
    if pdf_in_memory is not None:
        try:
            base64_pdf = base64.b64encode(pdf_in_memory.getvalue()).decode("utf-8")
            pdf_display = f"""
                <iframe src="data:application/pdf;base64,{base64_pdf}" width="{iframe_width+10}px" height="2100px" type="application/pdf"></iframe>
            """
            st.markdown(pdf_display, unsafe_allow_html=True)
        except:
            st.error("Fehler beim Anzeigen des PDFs.")

def get_address():
    searchbox_text = st_searchbox(
        search_function, 
        key="box_to_search", 
        clear_on_submit=False, 
        placeholder=st.session_state['searchbox_placeholder_text'],
        default_options=[
            "Bergackerstrasse 11, Freimettigen",
            "Bundesplatz 3 Bern",
            "Emmentalstrasse 151b Oberburg",
            "Waldstrasse 39 Utzenstorf",
            ])
    
    st.info("Bitte oben eine Adresse eingeben.", icon="ℹ️")

    if searchbox_text:
        st.session_state['ch.bfs.gebaeude_wohnungs_register.label'] = searchbox_text
        st.session_state['ch.bfs.gebaeude_wohnungs_register.egaid'] = set_featureid(searchbox_text)
        wohnungsregister = get_wohnungsregister(st.session_state["ch.bfs.gebaeude_wohnungs_register.egaid"])
        st.session_state['ch.bfs.gebaeude_wohnungs_register.egrid'] = wohnungsregister['feature']['attributes']['egrid']
        e_gebäude_koord = wohnungsregister['feature']['attributes']['gkode']
        n_gebäude_koord = wohnungsregister['feature']['attributes']['gkodn']
        st.session_state['e_gebäude_koord'] = e_gebäude_koord
        st.session_state['n_gebäude_koord'] = n_gebäude_koord
        st.session_state['bbox'] = get_bbox(st.session_state["ch.bfs.gebaeude_wohnungs_register.egaid"])
        st.rerun()

def set_sessions_state():
    #Session State

    if 'bbox' not in st.session_state:
        st.session_state['bbox'] = None

    if 'searchbox_placeholder_text' not in st.session_state:
        st.session_state['searchbox_placeholder_text'] = "Adresse suchen"

    if 'ch.bfs.gebaeude_wohnungs_register.egaid' not in st.session_state:
        st.session_state['ch.bfs.gebaeude_wohnungs_register.egaid'] = None

    if 'ch.bfs.gebaeude_wohnungs_register.egrid' not in st.session_state:
        st.session_state['ch.bfs.gebaeude_wohnungs_register.egrid'] = None

    if 'ch.bfs.gebaeude_wohnungs_register.label' not in st.session_state:
        st.session_state['ch.bfs.gebaeude_wohnungs_register.label'] = None

    if 'e_gebäude_koord' not in st.session_state:
        st.session_state['e_gebäude_koord'] = None

    if 'n_gebäude_koord' not in st.session_state:
        st.session_state['n_gebäude_koord'] = None

    if 'iframe_width' not in st.session_state:
        st.session_state['iframe_width'] = 680

def get_sidebar():
    with st.sidebar:
        if st.session_state["ch.bfs.gebaeude_wohnungs_register.label"]:
            st.write(st.session_state["ch.bfs.gebaeude_wohnungs_register.label"])
            st.markdown(f"[URL (ÖREB-Kataster – Kanton Bern)](https://oerebview.apps.be.ch/#/d/{st.session_state['ch.bfs.gebaeude_wohnungs_register.egrid']})", unsafe_allow_html=True)
            st.markdown(f"[PDF (ÖREB-Kataster – Kanton Bern)](https://www.oereb2.apps.be.ch/extract/pdf?egrid={st.session_state['ch.bfs.gebaeude_wohnungs_register.egrid']}&lang=de)", unsafe_allow_html=True)            
            st.markdown(f"[Geoportal - Kanton Bern](https://www.map.apps.be.ch/pub/externalcall.jsp?query1=egrid&keyvalue1={st.session_state['ch.bfs.gebaeude_wohnungs_register.egrid']}&keyname1=EGRID&project=a42pub_oereb_oeffen_DE&language=de&userprofile=geo&client=auto)", unsafe_allow_html=True)
