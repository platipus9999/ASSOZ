from os import name, system

def Title(content: str):
    if name == 'nt':
        system(f'title {content}')
    else:
        pass

def Clear():
    if name == 'nt':
        system('cls')
    else: 
        system('clear')
class Vertical:      
    def yellow_to_red(text: str): 
        col = ""
        green = 250
        for line in text.splitlines():
            col += (f"\033[38;2;255;{green};0m{line}\033[0m\n")
            if not green == 0:
                green -= 25
                if green < 0:
                    green = 0
        return col
class Horizontal:
    def yellow_to_red(text: str): 
        col = ""
        green = 250
        for letters in [*text]:
            col += (f"\033[38;2;255;{green};0m{letters}\033[0m")
            if not green == 0:
                green -= 7
                if green < 0:
                    green = 0
        return col
