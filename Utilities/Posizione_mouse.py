import pyautogui
import time

#5 secondi di tempo per posizionarsi
time.sleep(10)

# Ottieni le coordinate attuali del cursore
current_mouse_x, current_mouse_y = pyautogui.position()

# Stampa le coordinate
print(f"Coordinate attuali del cursore: ({current_mouse_x}, {current_mouse_y})")