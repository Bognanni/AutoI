import pyautogui
import time
import random

# Ottieni le dimensioni dello schermo
screen_width, screen_height = pyautogui.size()

# Numero di clic
num_clicks = 1

for _ in range(num_clicks):
    # Genera coordinate casuali per lo spostamento del mouse
    # x = random.randint(0, screen_width)
    # y = random.randint(0, screen_height)

    # Sposta il mouse alle coordinate
    pyautogui.moveTo(589, 0, duration=0.5)  # Durata del movimento: 0.5 secondi
    
    # Fai un clic
    pyautogui.click()
    
    # si posiziona più sopra così da poter scrollare
    pyautogui.moveTo(849, 692, duration=0.5)  # Durata del movimento: 0.5 secondi
    pyautogui.scroll(-100)

    # time.sleep(1)  # Attendi 1 secondo prima di muovere il mouse di nuovo