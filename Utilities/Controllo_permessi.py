import pyautogui

try:
    screenshot = pyautogui.screenshot()
    screenshot.save('screenshot_test.png')
    print("Screenshot catturato e salvato con successo.")
except Exception as e:
    print("Errore durante la cattura dello screenshot:", e)