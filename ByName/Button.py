import time
import uiautomation as auto


class Button:
    def __init__(self, name):
        self.name = name
        self.button = auto.ButtonControl(Name=name)

    def click(self):
        if self.button.Exists():
            self.button.Click()
        else:
            print(f"Pulsante '{self.name}' non trovato")

    def scroll(self, n_scroll):
        if self.button.Exists():
            self.button.SendKeys("{PGDN}")

        else:
            print(f"Pulsante '{self.name}' non trovato")
