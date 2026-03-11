import pyautogui


def move_to_by_image(path_image, confidence=0.8):
    while confidence > 0.5:
        try:
            res = pyautogui.locateOnScreen(path_image, confidence=confidence)
            pos = pyautogui.center(res)
            x = pos.x
            y = pos.y
            pyautogui.moveTo(x, y, duration=0.5)
            return True

        except pyautogui.ImageNotFoundException:
            print("Immagine non trovata")
            confidence = confidence - 0.1
            if confidence < 0.5:
                print("Immagine non presente")
                return False


def move_to_center():
    screen_width, screen_height = pyautogui.size()

    # Calcola le coordinate del centro dello schermo
    center_x = screen_width // 2
    center_y = screen_height // 2

    # Sposta il mouse al centro dello schermo
    pyautogui.moveTo(center_x, center_y)
