import pyautogui

# Carica l'immagine dell'icona che desideri cercare e cliccare
icon_path = 'C:\\Users\\Bogna\\Desktop\\File_uni\\TRIENNALE\\TERZO_ANNO\\TESI\\AutoI\\Utilities\\icon_cartella.png'

# Trova la posizione dell'icona sullo schermo
try:
    icon_location = pyautogui.locateOnScreen(icon_path, confidence=0.8)
    if icon_location is not None:
        # Se trova l'icona, ottieni le coordinate del centro dell'icona
        icon_center = pyautogui.center(icon_location)
        # Fai clic sull'icona
        pyautogui.moveTo(icon_center.x, icon_center.y, duration=1)
        pyautogui.click()
    else:
        print("Icona non trovata")
except Exception as e:
    print(f"Si è verificato un errore: {e}")