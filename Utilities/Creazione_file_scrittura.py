import pyautogui
import time

# Ottieni le dimensioni dello schermo
screen_width, screen_height = pyautogui.size()

# Sposta il mouse sulla barra di ricerca
pyautogui.moveTo(509, 1048, duration=1)  # Durata del movimento: 0.5 secondi
    
# Fai un clic
pyautogui.click()

#ricerca e apertura file
pyautogui.typewrite("Blocco note")
pyautogui.moveTo(712, 296, duration=1)
pyautogui.click()

#creazione file e scrittura
pyautogui.moveTo(1267, 181, duration=1)
pyautogui.click()
pyautogui.moveTo(304, 271, duration=1)
pyautogui.click()
pyautogui.typewrite("Prova scrittura")
