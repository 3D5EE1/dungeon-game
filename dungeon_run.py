from dungeon_game_2 import *


def game_run():
    start = StartMenu().menu()
    start.draw()
    next_menu = ChoiceMenu([1, 2, 3, 5, 6, 7, 8], start).choice()
    if next_menu == 1:
        Head()
        print('начать новую игру')
    elif next_menu == 2:
        Head()
        print('продолжить игру')



if __name__ == '__main__':
    game_run()