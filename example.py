import EasyConsole
import os  # per clear screen
import keyboard  # per prendere i tasti premuti (pip/pip3 install keyboard)
istanza = EasyConsole.EasyConsole()

istanza.menu_init(["ciao", "banana"])

os.system(istanza.clear)
istanza.refreshMenu()

while True:
    try:
        if keyboard.is_pressed("up"):
            istanza.passSelectionUP()
            os.system(istanza.clear)
            istanza.refreshMenu()
        elif keyboard.is_pressed("down"):
            istanza.passSelectionDOWN()
            os.system(istanza.clear)
            istanza.refreshMenu()
        elif keyboard.is_pressed("enter"):
            os.system(istanza.clear)
            break
    except KeyboardInterrupt:
        exit()

if istanza.getOptionSelect() == "ciao":
    print("Hai scelto ciao")
else:
    print("Hai scelto banana")