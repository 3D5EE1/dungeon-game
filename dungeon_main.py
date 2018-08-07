from colorama import init, Fore, Back, Style
from dungeon_draw import Draw, colors_no_black
import random
from dungeon_rooms import draw_game, draw_skull, draw_start_menu, draw_game_5_1, \
                          draw_game_5_2, enter_you_name_5_1, enter_you_name_5_2, text_0, text_0_1, text_1

from dungeon_logic import Menu, game_exit
from dungeon_new_game import Game
#from dungeon_continue_game import ContinueGame



def rungame():
    run = True
    while run:
        random_color1 = random.choice(colors_no_black)
        random_color2 = random.choice(colors_no_black)
        draw = Draw(draw_game, Fore.LIGHTCYAN_EX, draw_skull, draw_start_menu, random_color1, random_color2)
        draw.window_size()
        draw.draw()
        menu = Menu(1, 3, draw)
        menu_choice = menu.check_choice()
        if menu_choice == 1:
            game = Game(enter_you_name_5_1, enter_you_name_5_2, text_0, text_0_1, None)
            game.change_start()
            draw1 = Draw(draw_game_5_1, Fore.LIGHTCYAN_EX, enter_you_name_5_1,
                         enter_you_name_5_2, Fore.GREEN, Fore.GREEN)
            draw1.draw()



            run = game_exit()
        elif menu_choice == 2:
            run = game_exit()
        elif menu_choice == 3:
            run = game_exit()



if __name__ == '__main__':
    # init()
    rungame()
