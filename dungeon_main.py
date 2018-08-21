from colorama import init, Fore, Back, Style
from dungeon_draw import canvas, Draw
from dungeon_pictures import pictures
from dungeon_logic import Menu, game_exit
from dungeon_game import Game, char_params, params_char
import random, time


def run_game():
    run = True
    while run:
        draw = Draw(canvas(random.choice([pictures(0), pictures(1)]), pictures(2)))
        draw.window_size()
        draw.draw()
        menu_choice = Menu(1, 3, draw).check_choice()  # первый выбор, основное меню
        if menu_choice == 1:
            name_choice, hero, char_name = None, True, None
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
                    draw = Draw(canvas(picture_name_approved), 5)  # картинка, что такое имя уже есть
                    name = Game(draw_repeat=draw, name=char_name).save_new_game()  # проверяет наличие имени в save

                    if name is False:  # такое имя уже есть в save
                        draw = Draw(canvas(pictures(4), pictures(5), pictures(10)), 5)  # рисует выбор нового имени
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
                char_choice = []

                Draw(canvas(pictures(4), pictures(5), pictures(13)), 5).draw()
                draw = Draw(canvas(pictures(4), pictures(5), pictures(14)), 5)  # картинка выбора пола
                draw.draw()
                sex_choice = Menu(1, 2, draw).check_choice()  # выбор пола вашего персонажа
                char_choice += [sex_choice]

                Draw(canvas(pictures(4), pictures(5), pictures(15)), 5).draw()
                draw = Draw(canvas(pictures(9)), 10)  # картинка выбора рассы
                draw.draw()
                race_choice = Menu(1, 4, draw).check_choice()  # выбор рассы вашего персонажа
                char_choice += [race_choice]

                if race_choice == 2:
                    Draw(canvas(pictures(4), pictures(5), pictures(16)), 5).draw()
                    draw = Draw(canvas(pictures(4), pictures(5), pictures(17)), 5)  # картинка выбора класса эльфа
                    draw.draw()
                    class_choice = Menu(1, 3, draw).check_choice()  # выбор класса вашего персонажа
                    char_choice += [class_choice]

                elif race_choice == 3:
                    Draw(canvas(pictures(4), pictures(5), pictures(16)), 5).draw()
                    draw = Draw(canvas(pictures(4), pictures(5), pictures(18)), 5)  # картинка выбора класса орка
                    draw.draw()  # рисуем картинку выбора класса
                    class_choice = Menu(1, 3, draw).check_choice()  # выбор класса вашего персонажа
                    char_choice += [class_choice]

                elif race_choice == 4:
                    Draw(canvas(pictures(4), pictures(5), pictures(16)), 5).draw()
                    draw = Draw(canvas(pictures(4), pictures(5), pictures(19)), 5)  # картинка выбора класса гнома
                    draw.draw()
                    class_choice = Menu(1, 2, draw).check_choice()  # выбор класса вашего персонажа
                    char_choice += [class_choice]

                else:
                    Draw(canvas(pictures(4), pictures(5), pictures(16)), 5).draw()
                    draw = Draw(canvas(pictures(4), pictures(5), pictures(20)), 5)  # картинка выбора класса человека
                    draw.draw()
                    class_choice = Menu(1, 4, draw).check_choice()  # выбор класса вашего персонажа
                    char_choice += [class_choice]

                draw = Draw(canvas(pictures(4), pictures(5), pictures(21)), 5)  # картинка возраста персонажа
                draw.draw()
                age_choice = Menu(20, 100, draw).check_choice()  # выбор возраста вашего персонажа
                char_choice += [age_choice]

                draw = Draw(canvas(pictures(4), pictures(5), pictures(22)), 7)
                draw.draw()
                params_choice = Menu(1, 3, draw).check_choice()  # выбор параметров персонажа
                if params_choice == 1:
                    print('тут будет продолжение')
                    time.sleep(2.5)
                elif params_choice == 2:
                    params = params_char(pictures(12), char_params(char_choice))  # заменяем словарь параметров
                    picture_params1 = Game(picture=pictures(11), text={'canvas4c': char_name}).print_text()
                    picture_params2 = Game(picture=pictures(12), text=params).print_text()
                    draw = Draw(canvas(picture_params1, picture_params2), 17)
                    draw.draw()
                    print('\nна этом пока все, ждите продолжения\nдля выхода нажмине "1", для продолжения "2"')
                    params_choice = Menu(1, 2, draw).check_choice()
                    if params_choice == 1:
                        run = game_exit()
                    elif params_choice == 2:
                        pass
                elif params_choice == 3:
                    pass
        elif menu_choice == 2:
            print('продолжение пока не готово')
            time.sleep(2.5)
        elif menu_choice == 3:
            run = game_exit()


if __name__ == '__main__':
    init()
    run_game()












