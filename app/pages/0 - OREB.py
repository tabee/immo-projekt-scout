import base64
from pathlib import Path
import requests
from io import BytesIO
import streamlit as st

from requests.exceptions import RequestException
from io import BytesIO
import streamlit as st
from app_utils import set_sessions_state, get_address, get_sidebar, download_pdf
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
    
    # OREB PDF
    st.subheader("OREB")
 





    # URL des PDFs
    pdf_url = f"https://www.oereb2.apps.be.ch/extract/pdf?egrid={st.session_state['ch.bfs.gebaeude_wohnungs_register.egrid']}&lang=de"

    # Herunterladen und Speichern des PDFs im Speicher
    pdf_in_memory = download_pdf(pdf_url)

    # Lesen Sie die Daten aus dem BytesIO-Objekt und kodieren Sie sie in Base64
    base64_pdf = base64.b64encode(pdf_in_memory.getvalue()).decode("utf-8")
    
    # Überprüfen Sie, ob das PDF erfolgreich heruntergeladen wurde
    if pdf_in_memory is not None:
        base64_pdf = base64.b64encode(pdf_in_memory.getvalue()).decode("utf-8")
        pdf_display = f"""
            <iframe src="data:application/pdf;base64,{base64_pdf}" width="{iframe_width}px" height="2100px" type="application/pdf"></iframe>
        """
        st.markdown(pdf_display, unsafe_allow_html=True)
    else:
        st.write("Fehler beim Herunterladen des PDFs.")