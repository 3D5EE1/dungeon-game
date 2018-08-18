from colorama import init, Fore, Back, Style
from dungeon_draw import canvas, Draw
from dungeon_pictures import pictures
from dungeon_logic import Menu, game_exit
from dungeon_game import Game
import random
import json


def run_game():
    run = True
    while run:
        draw = Draw(canvas(random.choice([pictures(0), pictures(1)]), pictures(2)))
        draw.window_size()
        draw.draw()
        menu_choice = Menu(1, 3, draw).check_choice()
        if menu_choice == 1:
            name_choice, hero, char_name, enemy_name = 1, True, None, None
            while hero:
                name = False
                while not name:
                    draw = Draw(canvas(pictures(4), pictures(5)), 5)
                    draw.draw()
                    char_name = Game(draw).check_name()
                    picture_name_approved = Game(picture=pictures(8), text={'canvas4c': char_name}).print_text()
                    picture_name = Game(picture=pictures(7), text={'canvas4c': char_name}).print_text()
                    draw = Draw(canvas(picture_name, pictures(6)), 9)
                    draw.draw()
                    name_choice = Menu(1, 3, draw).check_choice()
                    if name_choice == 1:
                        draw = Draw(canvas(picture_name_approved), 5)
                        name = Game(draw_repeat=draw, name=char_name).save_new_game()
                        draw = Draw(canvas(picture_name, pictures(6)), 9)
                        draw.draw()
                        approved_name_choice = Menu(1, 2, draw).check_choice()
                        if approved_name_choice == 1:
                            hero = False
                        elif approved_name_choice == 2:
                            name_choice = 3
                            break
                    elif name_choice == 2:
                        pass
                    elif name_choice == 3:
                        hero = False
                        break
            if name_choice != 3:
                sex = Game(picture=pictures(4), text={'canvas2c': '      Выберите пол вашего персонажа!!!'}).print_text()
                draw = Draw(canvas(sex, pictures(5)), 5)
                draw.draw()
                sex = Game(picture=pictures(4), text={'canvas2c': '       "1" - мужской  "2" - женский'})
                draw = Draw(canvas(sex.print_text(), pictures(5)), 5)
                draw.draw()
                sex_choice = Menu(1, 2, draw).check_choice()
                sex = Game(choice=sex_choice).sex_choice()
                Game(name=char_name, params=sex).save_new_game()
            with open('save.txt', 'r') as save:
                characters = json.loads(save.read())
            print(characters)

            # picture_approved_name = Game(picture=pictures(7), text={}).print_text()
            # draw_not_approved = Draw(canvas(picture_approved_name), 7)
            # hero = Game(draw_repeat=draw_not_approved, name=char_name)
            # hero.save_new_game()
            #
            #     picture_name = Game(picture=pictures(7), text={'canvas4c': char_name}).print_text()
            #     draw_name_approved = Draw(canvas(picture_name, pictures(6)), 7)
            #     draw_name_approved.draw()
            #     if Game(name=char_name).save_new_game():
            #         name = False
            #     name_choice = Menu(1, 2, draw).check_choice()
            #     if name_choice == 1:
            #         name = False
            #     elif name_choice == 2:
            #         pass
            #
            # Draw(canvas(sex, pictures(5)), 5).draw()
            # sex = Game(picture=pictures(4), text={'canvas2c': '       "1" - мужской  "2" - женский'})
            # draw = Draw(canvas(sex.print_text(), pictures(5)), 5)
            # draw.draw()
            # sex_choice = Menu(1, 2, draw).check_choice()
            # sex = Game(choice=sex_choice).sex_choice()
        elif menu_choice == 2:
            pass
        elif menu_choice == 3:
            run = game_exit()


if __name__ == '__main__':
    init()
    run_game()












