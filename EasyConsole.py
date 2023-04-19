import os
class EasyConsole:
    def __init__(self):
        self.menu = []
        self.NORMAL = "\u001b[0m"
        self.YELLOW_BG = "\u001b[43m"
        self.RED_BG = "\u001b[41m"
        self.BLUE_BG = "\u001b[44m"
        self.YELLOW_FG = "\u001b[33m"
        self.RED_FG = "\u001b[31m"
        self.BLUE_FG = "\u001b[34m"
        self.option_attual = 0
        self.max_option = 0
        self.color = self.YELLOW_FG
        self.color_selection = self.YELLOW_BG
        if os.name == "nt":
            self.clear = "cls"
        else:
            self.clear = "clear"
    def menu_init(self, menu: list, color: str="\u001b[33m", color_selection: str="\u001b[43m") -> bool:
        self.menu = menu
        self.max_option = len(menu)
        self.option_attual = 1
        self.color = color
        self.color_selection = color_selection
        return True
    def getOptionSelect(self) -> int:
        return self.menu[self.option_attual-1]
    def refreshMenu(self):
        for i in self.menu:
            try:
                if self.menu[self.option_attual-1] == i:
                    print(f"\t\t\t\t\t\t\t\t{self.color_selection}{i}{self.NORMAL}")
                else:
                    print(f"\t\t\t\t\t\t\t\t{self.color}{i}{self.NORMAL}")
            except:
                pass
        print(self.NORMAL)
    def passSelectionUP(self):
        if not (self.option_attual - 1) < 1:
            self.option_attual -= 1
    def passSelectionDOWN(self):
        if not (self.option_attual + 1) > self.max_option:
            self.option_attual += 1