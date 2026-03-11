import uiautomation as auto


class ListItem:
    def __init__(self, name):
        self.name = name
        self.listItem = auto.ListItemControl(Name=name)

    def click(self):
        if self.listItem.Exists():
            self.listItem.Click()
        else:
            print(f"Elemento lista '{self.name}' non trovato")
