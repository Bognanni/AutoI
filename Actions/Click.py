import time
import pyautogui
import Movement


class Click:
    def __init__(self, path_image=""):
        self.path_image = path_image

    def click_by_image(self):
        if self.path_image == "CENTER":
            Movement.move_to_center()
            self.path_image = ""
        if self.path_image != "":
            if not Movement.move_to_by_image(self.path_image):
                return False
        time.sleep(0.5)
        pyautogui.click()

        return True

    def double_click_by_image(self):
        if self.path_image == "CENTER":
            Movement.move_to_center()
        if self.path_image != "":
            if not Movement.move_to_by_image(self.path_image):
                return False
        time.sleep(0.5)
        pyautogui.doubleClick()

        return True

    def left_click_by_image(self):
        if self.path_image == "CENTER":
            Movement.move_to_center()
        if self.path_image != "":
            if not Movement.move_to_by_image(self.path_image):
                return False
        time.sleep(0.5)
        pyautogui.leftClick()

        return True

    def get_path_image(self):
        return self.path_image

    def set_path_image(self, path_image):
        self.path_image = path_image
