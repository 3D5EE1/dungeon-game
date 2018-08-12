from colorama import init, Fore, Back, Style
from dungeon_draw import picture, Draw
from dungeon_pictures import figure
import random


def run_game():
    run = True
    while run:
        game = Draw(picture(figure(0), random.choice([None, figure(1)])), None, None)
        game.draw()
        run = False


if __name__ == '__main__':
    # init()
    run_game()
