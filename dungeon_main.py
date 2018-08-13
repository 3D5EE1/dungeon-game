from colorama import init, Fore, Back, Style
from dungeon_draw import canvas, Draw
from dungeon_pictures import pictures
from dungeon_logic import Menu, game_exit
import random


def run_game():
    run = True
    while run:
        game = Draw(canvas(random.choice([pictures(0), pictures(1)]), pictures(2)))
        game.window_size()
        game.draw()
        menu = Menu(1, 3, game)
        menu_choice = menu.check_choice()
        if menu_choice == 1:
            pass
        elif menu_choice == 2:
            pass
        elif menu_choice == 3:
            run = game_exit()


if __name__ == '__main__':
    # init()
    run_game()
