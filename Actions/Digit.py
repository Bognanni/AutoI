import pyautogui
import Movement
import time


class Digit:
    def __init__(self, path_image=""):
        self.path_image = path_image

    def special_key_n_times(self, content, n=1):
        if self.path_image != "":
            if not Movement.move_to_by_image(self.path_image):
                return False
        time.sleep(0.5)
        pyautogui.click()
        for i in range(n):
            pyautogui.press(content)
        return True

    def write_by_image(self, string):
        if self.path_image != "":
            if not Movement.move_to_by_image(self.path_image):
                return False
        time.sleep(0.5)
        pyautogui.click()
        pyautogui.write(string)
        return True

    def get_path_image(self):
        return self.path_image

    def set_path_image(self, path_image):
        self.path_image = path_image
