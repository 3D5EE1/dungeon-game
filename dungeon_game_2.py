from colorama import init, Fore, Back, Style
from dungeon_logic import game_exit
from dungeon_pictures import pictures
from dungeon_draw import canvas, Draw, cls
import random


class HeadMenu:

    def __init__(self):
        Draw(canvas(pictures(26)), 2, pictures(0)['canvas2a'][1:]).draw()


class StartMenu(HeadMenu):

    def __init__(self):
        super().__init__()

    def menu(self):
        return Draw(canvas(random.choice([pictures(0), pictures(1)]), pictures(2)))


class Head:

    def __init__(self):
        Draw(canvas(pictures(27)), 2, pictures(0)['canvas2a'][1:]).draw()


class ChoiceMenu:

    def __init__(self, menu_numbers, repeat):
        self.menu_numbers = menu_numbers
        self.repeat = repeat

    def choice(self):
        try:
            number = int(input(Fore.LIGHTGREEN_EX + '\n введите чисо: ' + Style.RESET_ALL))
            if number in self.menu_numbers:
                if number == 1:
                    return 1
                elif number == 2:
                    return 2
                elif number == 3:
                    return 3
                elif number == 4:
                    return 4
                elif number == 7:
                    cls()
                    start = StartMenu().menu()
                    start.draw()
                    print(Fore.LIGHTRED_EX + '\n вы вернулись в главное меню' + Style.RESET_ALL)
                    ChoiceMenu(self.menu_numbers, self.repeat).choice()
                elif number == 8:
                    cls()
                    game_exit()
            else:
                cls()
                HeadMenu()
                self.repeat.draw()
                print(Fore.LIGHTRED_EX + '\n вы выбрали несуществующий пунк меню')
                ChoiceMenu(self.menu_numbers, self.repeat).choice()
        except ValueError:
            cls()
            HeadMenu()
            self.repeat.draw()
            print(Fore.LIGHTRED_EX + '\n вы ввели не подходящее значение')
            ChoiceMenu(self.menu_numbers, self.repeat).choice()


if __name__ == '__main__':
    pass