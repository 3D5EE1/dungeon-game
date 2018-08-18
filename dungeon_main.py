from colorama import init, Fore, Back, Style
from dungeon_draw import canvas, Draw
from dungeon_pictures import pictures
from dungeon_logic import Menu, game_exit
from dungeon_game import Game
import random


def run_game():
    run = True
    while run:
        draw = Draw(canvas(random.choice([pictures(0), pictures(1)]), pictures(2)))
        draw.window_size()
        draw.draw()
        menu_choice = Menu(1, 3, draw).check_choice()  # первый выбор, основное меню
        if menu_choice == 1:
            name_choice, hero, char_name, enemy_name = None, True, None, None
            while hero:
                draw = Draw(canvas(pictures(4), pictures(5)), 5)  # картинка ввода имени персонажа
                draw.draw()
                char_name = Game(draw).check_name()  # ввод имени
                picture_name = Game(picture=pictures(7), text={'canvas4c': char_name}).print_text()
                draw = Draw(canvas(picture_name, pictures(6)), 9)  # картинка отображающая ваше имя
                draw.draw()
                name_choice = Menu(1, 3, draw).check_choice()  # выбор подтверждения вашего имени
                if name_choice == 1:  # выбор подтверждения вашего имени, вы согласны с именем
                    picture_name_approved = Game(picture=pictures(8), text={'canvas4c': char_name}).print_text()
                    draw = Draw(canvas(picture_name_approved), 5)  # картинка если такое имя уже есть
                    name = Game(draw_repeat=draw, name=char_name).save_new_game()  # проверяет наличие имени в save
                    if name is False:  # такое имя уже есть в save
                        draw = Draw(canvas(pictures(4), pictures(5), pictures(10)), 5)  # рисует что имя есть
                        draw.draw()
                        approved_name_choice = Menu(1, 2, draw).check_choice()  # либо новое имя либо вернуться в меню
                        if approved_name_choice == 1:  # если новое имя то цикл занова
                            pass
                        elif approved_name_choice == 2:  # возврат в главное меню
                            hero = False
                            name_choice = 3
                    elif name is True:  # если имени в save нет, будет создан персонаж
                        hero = False
                elif name_choice == 2:  # выбор подтверждения вашего имени, вы не согласны с именем, цикл hero занова
                    pass
                elif name_choice == 3:  # выбор подтверждения вашего имени, возврат в главное меню
                    hero = False
            if name_choice != 3:  # продолжаем создавать персонажа, выбираем пол
                sex = Game(picture=pictures(4), text={'canvas2c': '         Выберите пол вашего персонажа!!!'}
                           ).print_text()  # создаем картинку выбора пола, внеся изменения в готовую картинку
                draw = Draw(canvas(sex, pictures(5)), 5)
                draw.draw()
                sex = Game(picture=pictures(4), text={'canvas2c': '           "1" - мужской   "2" - женский'})
                draw = Draw(canvas(sex.print_text(), pictures(5)), 5)  # рисуем картинку выбора пола
                draw.draw()
                sex_choice = Menu(1, 2, draw).check_choice()  # выбор пола вашего персонажа
                sex = Game(choice=sex_choice).sex_choice()  # переделывает выбол пола в слово
                Game(name=char_name, params=sex).save_new_game()  # сохраняет пол в save
        elif menu_choice == 2:
            pass
        elif menu_choice == 3:
            run = game_exit()


if __name__ == '__main__':
    init()
    run_game()












