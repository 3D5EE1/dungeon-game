from dungeon_draw import Draw, cls
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
                print(Fore.GREEN + '\n выш выбор: ', end='')
                player_choice = int(input())
                cls()
                if self.x <= player_choice <= self.y:
                    return player_choice
                else:
                    raise ValueError
            except (TypeError, ValueError):
                cls()
                self.draw_repeat.draw()
                print(Style.BRIGHT + Fore.LIGHTCYAN_EX + f'\n введите цифру от {self.x} до {self.y}', Style.RESET_ALL)


def game_exit():
    cls()
    print(Style.BRIGHT + Fore.GREEN + 'спасибо за игру, всего вам хорошего!!!')
    time.sleep(2.5)
    os.system('exit')
    return False


if __name__ == '__main__':
    # init()
    pass
