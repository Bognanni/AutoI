import json
import time
import tkinter as tk
from tkinter import filedialog, messagebox

from Actions.Click import Click
from Actions.Scroll import Scroll
from Actions.Digit import Digit
from Actions.OpenFile import OpenFile


def choose_file():
    # Crea una finestra nascosta
    root = tk.Tk()
    root.withdraw()  # Nasconde la finestra principale

    # Apri una finestra di dialogo per selezionare il file
    file_path = filedialog.askopenfilename(
        title="Seleziona un file JSON",
        filetypes=[("File JSON", "*.json")]
    )

    if file_path:
        return file_path
    else:
        print("Nessun file selezionato.")


def show_correct_config():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Configurazione terminata", "La configurazione è terminata con successo!")
    root.destroy()


def show_wrong_config():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Configurazione fallita", "La configurazione non è andata a buon fine!")
    root.destroy()


def main():
    file_json = choose_file()
    with open(file_json, 'r') as file:
        data = json.load(file)

    repeat = data["repeat"]
    time.sleep(2)
    for i in range(repeat):
        do_actions(data)

    time.sleep(1)
    show_correct_config()


def do_actions(data):
    for action in data['actions']:
        action_type = action['action_type']

        if action_type == 'OPEN_FILE':
            path_exe = action['path_exe']
            open_file = OpenFile(path_exe)
            if not open_file.exe_file():
                show_wrong_config()
                return
            time.sleep(1)


        click = Click()
        if action_type == 'CLICK':
            style = action['style']
            mode = action['mode']

            if style == 'IMAGE':
                path_image = action['path_image']
                click.set_path_image(path_image)

                if mode == 'SINGLE':
                    if not click.click_by_image():
                        show_wrong_config()
                        return
                elif mode == 'DOUBLE':
                    if not click.double_click_by_image():
                        show_wrong_config()
                        return
                elif mode == 'LEFT':
                    if not click.left_click_by_image():
                        show_wrong_config()
                        return
            time.sleep(1)


        scroll = Scroll()
        if action_type == 'SCROLL':
            style = action['style']
            n_scrolls = action['n_scrolls']
            mode = action['mode']

            if style == 'IMAGE':
                path_start_image = action['path_start_image']
                scroll.set_path_image_start(path_start_image)

                if mode == 'TO_POINT':
                    path_point_image = action['path_point_image']
                    scroll.set_path_image_point(path_point_image)
                    if not scroll.scroll_to_point(n_scrolls):
                        show_wrong_config()
                        return

                else:
                    if not scroll.scroll(n_scrolls):
                        show_wrong_config()
            time.sleep(1)


        digit = Digit()
        if action_type == 'WRITE':
            style = action['style']
            type_action = action['type']
            content = action['content']

            if style == 'IMAGE':
                path_image = action['path_image']
                digit.set_path_image(path_image)

            if type_action == 'KEY':
                n_times = action['n_times']

                if not digit.special_key_n_times(content, n_times):
                    show_wrong_config()
                    return

            elif type_action == 'STRING':
                if not digit.write_by_image(content):
                    show_wrong_config()
                    return
            time.sleep(1)


if __name__ == "__main__":
    main()
