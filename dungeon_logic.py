from old_dungeon_draw import cls
from colorama import init, Fore, Back, Style
import time
import os


class Menu:

    def __init__(self, x, y, draw_repeat):
        """инициализация интервала пунктов меню"""
        self.x = x
        self.y = y
        self.draw_repeat = draw_repeat

    def check_choice(self):
        """метод проверки правельного выбора пуктов меню"""
        while True:
            try:
                print(Fore.GREEN + ' выш выбор: ', end='')
                player_choice = int(input())
                if self.x <= player_choice <= self.y:
                    return player_choice
                else:
                    raise ValueError
            except (TypeError, ValueError):
                cls()
                self.draw_repeat.draw()
                print(Style.BRIGHT + Fore.LIGHTCYAN_EX + f' введите цифру от {self.x} до {self.y}')
                print(Style.RESET_ALL)


def game_exit():
    cls()
    print(Style.BRIGHT + Fore.GREEN + 'спасибо за игру, всего вам хорошего!!!')
    time.sleep(2.5)
    os.system('exit')
    return False


if __name__ == '__main__':
    # init()
    from old_dungeon_draw import Draw, colors_no_black
    from dungeon_pictures import draw_skull, draw_start_menu, draw_game
    import random
    random_color1 = random.choice(colors_no_black)
    random_color2 = random.choice(colors_no_black)
    menu = Menu(1, 3, Draw(draw_game, Fore.LIGHTCYAN_EX, draw_skull, draw_start_menu, random_color1, random_color2))
    menu.check_choice()
