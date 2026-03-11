import uiautomation as auto


class Combobox:
    def __init__(self, name):
        self.name = name
        self.checkbox = auto.ComboBoxControl(Name=name)

    def click(self):
        if self.checkbox.Exists():
            self.checkbox.Click()
        else:
            print(f"Checkbox '{self.name}' non trovato")
