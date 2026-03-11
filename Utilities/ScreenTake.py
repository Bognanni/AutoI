from PIL import Image
import pytesseract
import pyautogui
import time

time.sleep(3)

# Cattura uno screenshot dello schermo
screenshot = pyautogui.screenshot()

# Salva l'immagine su disco (temporaneamente)
screenshot.save('screenshot.png')

# Utilizza Tesseract per estrarre il testo dall'immagine
testo_estratto = pytesseract.image_to_string(Image.open('screenshot.png'))

# Stampa il testo estratto
print(testo_estratto)
