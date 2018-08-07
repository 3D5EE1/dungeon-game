from colorama import init, Fore, Back, Style
from dungeon_draw import colors_no_black, picture, Draw
from dungeon_pictures import draw_skull, draw_skull_text
import random


def rungame():
    run = True
    while run:
        random_color1 = random.choice(colors_no_black)
        random_color2 = random.choice(colors_no_black)
        game = Draw(picture(), None)


if __name__ == '__main__':
    # init()
    rungame()
