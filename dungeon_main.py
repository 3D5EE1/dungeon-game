from dungeon_draw import picture, Draw
from dungeon_pictures import draw_skull


def run_game():
    run = True
    while run:
        game = Draw(picture(draw_skull), None, draw_skull['canvas2a'][1:])
        game.draw()
        run = False


if __name__ == '__main__':
    # init()
    run_game()
