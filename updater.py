import bpy
import requests
from .version import version

UPDATE_URL = "https://raw.githubusercontent.com/seeseal/AutoEXR/main/addon_version.json"  # Replace with your URL

def get_latest_version_info():
    try:
        response = requests.get(UPDATE_URL)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print(f"Failed to fetch update info: {e}")
    return None

def notify_update_available(latest_version):
    message = f"A new version {latest_version['version']} of Auto EXR Pass Setup is available. Download it from {latest_version['download_url']}."
    def draw(self, context):
        self.layout.label(text=message)
    bpy.context.window_manager.popup_menu(draw, title="Update Available", icon='INFO')

def check_for_update():
    current_version = version
    latest_version_info = get_latest_version_info()
    
    if latest_version_info and latest_version_info['version'] != current_version:
        notify_update_available(latest_version_info)

