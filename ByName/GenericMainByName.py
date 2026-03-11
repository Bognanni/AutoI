import json
import OpenFile
import time
from AutoI.ByName.Button import Button
from AutoI.ByName.Combobox import Combobox
from ListItem import ListItem
from AutoI.ByName.Document import Document

with open('../Es2_Tesi.json', 'r') as file:
    data = json.load(file)

for action in data['actions']:
    action_type = action['action_type']
    if action_type == 'OPEN_FILE':
        path_exe = action['path_exe']
        OpenFile.open_file(path_exe)
        time.sleep(1)

    element = action['element']

    if element == 'BUTTON':
        style = action['style']
        if style == 'NAME':
            button = Button(action['name'])
            if action_type == 'CLICK':
                button.click()
                time.sleep(1)

    if element == 'COMBOBOX':
        style = action['style']
        if style == 'NAME':
            combobox = Combobox(action['name'])
            if action_type == 'CLICK':
                combobox.click()
                time.sleep(1)

    if element == 'LISTITEM':
        style = action['style']
        if style == 'NAME':
            listItem = ListItem(action['name'])
            if action_type == 'CLICK':
                listItem.click()
                time.sleep(1)

    if element == 'DOCUMENT':
        style = action['style']
        document = Document(action['window_name'])
        if action_type == 'SCROLL':
            if style == 'DOWN':
                document.scroll_down_ntimes(action['n_scrolls'])
                time.sleep(1)
            elif style == 'UP':
                document.scroll_up_ntimes(action['n_scrolls'])
                time.sleep(1)
