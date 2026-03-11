import json
from pynput import mouse, keyboard
import time
import pyautogui
import os

# Classe per creare il file json a partire dalle azioni effettuate dopo l'esecuzione
# Per ora inutile, NON IMPLEMENTARE

# Inizializza il dizionario per il JSON
actions_log = {
    "software_name": "gimp",
    "software_version": "2.10.36",
    "actions": []
}

# Crea la cartella 'images' se non esiste
folder_path = '../Images'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

def save_to_json():
    with open('actions.json', 'w') as f:
        json.dump(actions_log, f, indent=4)


# Funzione per registrare il click del mouse
def on_click(x, y, button, pressed):
    if pressed:
        # Cattura screenshot dell'area intorno al click
        screenshot = pyautogui.screenshot(region=(x - 50, y - 50, 200, 100))
        screenshot_path = os.path.join(folder_path, f'screenshot_{time.time()}.png')
        screenshot.save(screenshot_path)

        actions_log["actions"].append({'action_type': 'CLICK',
                                       'style': 'IMAGE',
                                       'path_image': screenshot_path})


# Funzione per registrare lo scroll del mouse
def on_scroll(x, y, dx, dy):
    actions_log["actions"].append({'action': 'scroll',
                                   'x': x, 'y': y, 'dx': dx, 'dy': dy, 'time': time.time()})


# Funzione per registrare i tasti premuti sulla tastiera
def on_press(key):
    try:
        actions_log["actions"].append({'action': 'key_press', 'key': key.char, 'time': time.time()})
    except AttributeError:
        actions_log["actions"].append({'action': 'key_press', 'key': str(key), 'time': time.time()})


# apertura file (per ora non generico)
actions_log["actions"].append({'action_type': 'OPEN_FILE',
                               'path_exe': "C:\\Users\\Bogna\\Desktop\\gimp-2.10.36-setup-1"})

# Listener per il mouse
mouse_listener = mouse.Listener(on_click=on_click, on_scroll=on_scroll)
mouse_listener.start()

# Listener per la tastiera
keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()

# Aspetta l'input dall'utente per fermare la registrazione
input("Premi Invio per fermare la registrazione...\n")

# Ferma i listener e salva le azioni
mouse_listener.stop()
keyboard_listener.stop()
save_to_json()
