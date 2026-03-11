import pyautogui
import time
import Movement


class Scroll:
    def __init__(self, path_image_start="", path_image_point=""):
        self.path_image_start = path_image_start
        self.path_image_point = path_image_point

    # scroll spostandosi su un determinato punto, se non specificato effettua scroll dall'ultima posizione del mouse
    def scroll(self, n):
        if self.path_image_start != "":
            if not Movement.move_to_by_image(self.path_image_start):
                return False
        time.sleep(0.5)

        pyautogui.scroll(n)
        return True

    # iterazione fino al raggiungimento di un punto
    def scroll_to_point(self, n, confidence=0.8):
        first = True
        confidence_var = confidence
        while True:
            try:
                location = pyautogui.locateOnScreen(self.path_image_point, confidence=confidence_var)
                if location:
                    print("Fine della pagina raggiunta.")
                    break

            except pyautogui.ImageNotFoundException:
                print("Immagine finale non trovata con confidenza: " + str(confidence_var))
                confidence_var = confidence_var - 0.1
                if confidence_var < 0.8:
                    print("Confidenza minima raggiunta")
                    confidence_var = confidence
                    if first:
                        if self.scroll(n):
                            first = False
                            self.set_path_image_start("")
                        else:
                            return False
                    else:
                        self.scroll(n)
                    time.sleep(0.5)

            except Exception as e:
                print(f"Si è verificato un errore: {e}")
                break
        return True

    def get_path_image_point(self):
        return self.path_image_point

    def set_path_image_point(self, path_image_point):
        self.path_image_point = path_image_point

    def get_path_image_start(self):
        return self.path_image_start

    def set_path_image_start(self, path_image_start):
        self.path_image_start = path_image_start
