from colorama import init, Fore, Back, Style
from dungeon_draw import canvas, Draw
from dungeon_pictures import pictures
from dungeon_logic import Menu, game_exit
from dungeon_new_game import Game
import random


def run_game():
    run = True
    while run:
        game = Draw(canvas(random.choice([pictures(0), pictures(1)]), pictures(2)))
        game.window_size()
        game.draw()
        menu_choice = Menu(1, 3, game).check_choice()
        if menu_choice == 1:
            name = True
            while name:
                game = Draw(canvas(pictures(4), pictures(5)), 5)
                game.draw()
                check_name = Game(draw_repeat=game).check_name()
                game = Game(picture=pictures(7), text={'canvas4c': check_name})
                draw = Draw(canvas(game.print_text(), pictures(6)), 7)
                draw.draw()
                menu_choice1 = Menu(1, 2, draw).check_choice()
                if menu_choice1 == 1:
                    name = False
                elif menu_choice == 2:
                    pass
            run = game_exit()
        elif menu_choice == 2:
            pass
        elif menu_choice == 3:
            run = game_exit()


if __name__ == '__main__':
    init()
    run_game()
