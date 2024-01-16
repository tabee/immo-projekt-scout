''' Configuration file for the streamlit app. '''
import os

current_file_path = os.path.abspath(__file__)

class AppConfig:
    ''' Configuration class for the streamlit app. '''
    def __init__(self):
        self.server_name = "127.0.0.1" if str(current_file_path).startswith('c:') else "fastapi"
