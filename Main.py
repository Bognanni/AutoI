import time
from AutoI.Actions import Click, OpenFile, Scroll
import pyautogui

'''
Eseguito su Pycharm con permessi da amministratore
Main per esecuzione sequenziale di test
'''


# 1) avvio file
OpenFile.open_file(r'./cartellaEseguibile/eseguibile.exe')

# 2) inizio setup
time.sleep(2)

# 2.1) click installazione a tutti gli utenti
Click.search_button_by_image(r'C:\Users\Bogna\Desktop\File_uni\TRIENNALE\TERZO_ANNO\TESI\AutoI\Images\Install_amm_button.png')

# 2.2) click tendina e selezione lingua italiana
time.sleep(2)
Click.search_button_by_image(r'C:\Users\Bogna\Desktop\File_uni\TRIENNALE\TERZO_ANNO\TESI\AutoI\Images\scroll_symbol.png')
time.sleep(1)
Click.search_button_by_image(r'C:\Users\Bogna\Desktop\File_uni\TRIENNALE\TERZO_ANNO\TESI\AutoI\Images\italiano_button.png')

# 2.3) click ok e installazione
time.sleep(1)
Click.search_button_by_image(r'C:\Users\Bogna\Desktop\File_uni\TRIENNALE\TERZO_ANNO\TESI\AutoI\Images\ok_button.png')

time.sleep(2)
Click.search_button_by_image(r'C:\Users\Bogna\Desktop\File_uni\TRIENNALE\TERZO_ANNO\TESI\AutoI\Images\personalizza_button.png')

time.sleep(2)
Scroll.scroll_to_point(-500, r'C:\Users\Bogna\Desktop\File_uni\TRIENNALE\TERZO_ANNO\TESI\AutoI\Images\end_conditions.png')

for i in range(4):
    time.sleep(1)
    Click.search_button_by_image(r'C:\Users\Bogna\Desktop\File_uni\TRIENNALE\TERZO_ANNO\TESI\AutoI\Images\avanti_button.png')
    pyautogui.moveRel(0, -50)

# Ultimo comando per l'installazione di GIMP
# time.sleep(1)
# Click.search_button_by_image(r'C:\Users\Bogna\Desktop\File_uni\TRIENNALE\TERZO_ANNO\TESI\AutoI\installa_button.png')




