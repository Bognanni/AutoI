import uiautomation as auto
import time
import pyautogui


class Document:
    def __init__(self, name_window):
        self.name = name_window
        self.window = auto.WindowControl(searchDepth=1, Name=name_window)
        self.document = self.window.DocumentControl()

    def click(self):
        if self.document.Exists():
            self.document.Click()
        else:
            print(f"document '{self.name}' non trovato")

    def scroll_down_ntimes(self, n):
        self.window.SetFocus()

        for _ in range(n):
            pyautogui.press('pagedown')
            time.sleep(0.5)

    def scroll_up_ntimes(self, n):
        self.window.SetFocus()

        for _ in range(n):
            pyautogui.press('pageup')
            time.sleep(0.5)
