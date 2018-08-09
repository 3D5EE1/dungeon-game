from colorama import init, Fore, Back, Style
from dungeon_draw import picture, Draw
from dungeon_pictures import figure



def run_game():
    run = True
    while run:
        game = Draw(picture(figure(0)), None, None)
        game.draw()
        run = False


if __name__ == '__main__':
    # init()
    run_game()
