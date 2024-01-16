''' In this file we prepare the data for the streamlit app. '''
import asyncio
import requests
import json
import streamlit as st
import streamlit.components.v1 as components


from config import AppConfig
from data_fetcher import DataFetcher

app_config = AppConfig()
data_fetcher_api = DataFetcher()

def pretty_print_json(json_data):
    ''' Pretty print a json object '''
    print(json.dumps(json_data, sort_keys=True, indent=1))

def search_function(search_text):
    """Führt eine Suche durch und gibt Adressvorschläge zurück."""
    addresses = []
    try:
        responses = asyncio.run(data_fetcher_api.search_addresses(search_text))
        for response in responses['results']:
            addresses.append(response['attrs']['label'])
        return addresses
    except requests.RequestException as e:
        st.error(f"Fehler bei der Anfrage: {e} oder beim Parsen der Antwort.")
    return None
    
def set_featureid(address):
    """Führt eine Suche durch und gibt rinr feature_id oder None zurück."""
    if not address:
        return None
    try:
        responses = asyncio.run(data_fetcher_api.search_addresses(address))
        return responses['results'][0]['attrs']['feature_id']
    except requests.RequestException as e:
        st.error(f"Fehler bei der Anfrage: {e}")
    return None

def get_wohnungsregister(feature_id):
    """Gibt das Wohnungsregister zurück. """
    if not feature_id:
        return None
    try:
        responses = asyncio.run(data_fetcher_api.get_wohnungsregister(feature_id))
        return responses
    except requests.RequestException as e:
        st.error(f"Fehler bei der Anfrage: {e}")
        return addresses

def get_html_popup_layer_urls_candidates_by_bbox(bbox, list):
    """Gibt alle Layer zurück, die in der BBox liegenund evtl. htmlPopup haben."""
    try:
        responses = asyncio.run(data_fetcher_api.get_html_popup_layer_urls_by_bbox(bbox, list))
        return responses
    except requests.RequestException as e:
        st.error(f"Fehler bei der Anfrage: {e}")
        return None

def get_html_popup_layer_urls_candidates_by_egid(egid, list):
    """Gibt alle Layer zurück, die in der BBox liegenund evtl. htmlPopup haben."""
    try:
        responses = asyncio.run(data_fetcher_api.get_html_popup_layer_urls_by_egid(egid, list))
        print(f"size: {len(responses)}")
        return responses
    except requests.RequestException as e:
        st.error(f"Fehler bei der Anfrage: {e}")
        return None

def get_bbox(feature_id):
    """Gibt die bbox des Wohnungsregisters zurück."""
    try:
        wohnungsregister = get_wohnungsregister(feature_id)
        bbox = wohnungsregister['feature']['bbox']
        return bbox
    except requests.RequestException as e:
        st.error(f"Fehler bei der get_bbox ({feature_id}) Anfrage: {e}")
        return None



def get_expander_box(title_text, list_of_layers, e_gebäude_koord, n_gebäude_koord, iframe_width, hint = " - Keine Informationen vorhanden.", description = None, height=150, display_map=True, is_expanded=None, zoom=11):
    ''' Displays a map with the given layers and a html popup if available.'''

    # Die Elemente der Liste mit Kommas verbinden
    selected_layers_str = ",".join(list_of_layers)
    bbox = get_bbox(st.session_state["ch.bfs.gebaeude_wohnungs_register.egaid"])
    iframe_components = get_html_popup_layer_urls_candidates_by_bbox(bbox, list_of_layers)
    iframe_components2 = get_html_popup_layer_urls_candidates_by_egid(st.session_state["ch.bfs.gebaeude_wohnungs_register.egaid"], list_of_layers)

    if iframe_components:
        if is_expanded is False:
            pass
        else:
            is_expanded = True
        text = ""
    else:
        if is_expanded is True:
            text = ""
            pass
        else:
            is_expanded = False
            text = "" + hint
    
    

    with st.expander((title_text + text), expanded=is_expanded):
        # display html popup when we find one
        for comp in iframe_components:
            #st.write(comp,"bbox")
            components.iframe(comp, width=iframe_width, height=height, scrolling=True)
        for comp in iframe_components2:
            #st.write(comp,"egid")
            components.iframe(comp, width=iframe_width, height=height, scrolling=True)
        if display_map:
            components.iframe(f'https://map.geo.admin.ch/embed.html?E={e_gebäude_koord}&N={n_gebäude_koord}&time=None&lang=de&notooltip=false&topic=ech&crosshair=bowl&zoom={zoom}&bgLayer=ch.swisstopo.pixelkarte-grau&layers={selected_layers_str}', width=iframe_width, height=420)
        if description:
            st.write(description)







if __name__ == "__main__":

    addresses = search_function("Bergackerstrasse 11 Freimettigen")

    print("\n\nAddresse:")
    pretty_print_json(addresses)

    print("\n\feature_id:")
    feature_id = set_featureid(addresses[0])
    pretty_print_json(feature_id)
            
    print("\n\nWohnungsregister:")
    wohnungsregister = get_wohnungsregister(feature_id)
    pretty_print_json(wohnungsregister)

    print("\n\nbbox:")
    bbox = wohnungsregister['feature']['bbox']
    print(bbox)

    print("\n\nLayer mit htmlPopup:")
    urls_to_iframe = get_html_popup_layer_urls_candidates_by_bbox(bbox, list = None)
    pretty_print_json(urls_to_iframe)

    # print("\n\nLayer mit htmlPopup:")
    # urls_to_iframe = get_html_popup_layer_urls_candidates_by_egid(bbox)
    # pretty_print_json(urls_to_iframe)

    # https://oerebview.apps.be.ch/#/d/CH594684343570
    # https://www.oereb2.apps.be.ch/extract/pdf?egrid=CH594684343570&lang=de
    # https://www.map.apps.be.ch/pub/externalcall.jsp?query1=egrid&keyvalue1=CH594684343570&keyname1=EGRID&project=a42pub_oereb_oeffen_DE&language=de&userprofile=geo&client=auto


    # https://grudis-public.apps.be.ch/grudis-public/ui/grundstueck/es?egrid=CH594684343570&language=de   
    # https://www.map.apps.be.ch/pub/externalcall.jsp?project=a42pub_oereb_oeffen_DE&x=2614964.65&y=1208778.7000000002&scale=1000&rotation=0&view=Ansicht_Standard&basemapview=HK_AV_grau&client=core&language=de
    # https://www.map.apps.be.ch/pub/synserver?project=a42pub_oereb_oeffen_DE&x=2614964.65&y=1208778.7000000002&scale=1000&rotation=0&view=Ansicht_Standard&basemapview=HK_AV_grau&client=core&language=de