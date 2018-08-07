from old_dungeon_draw import cls
from colorama import init, Fore, Back, Style
from dungeon_save import save_file
import re
import json


class Game:

    def __init__(self, new_picture, new_text, picture_dict, text_dict, name_str):
        """инициализация нового фреймаб списка текста и строк текста
        str_list - это строки, которые хотим заменить
        name_str - это строка, которая содержит имя """
        self.new_picture = new_picture
        self.new_text = new_text
        self.picture_dict = picture_dict
        self.text_dict = text_dict
        self.name_str = name_str


    def change_start(self):
        """метод создает или загружает save фаил"""
        while True:
            try:
                print(Fore.GREEN + Back.BLACK + ' >>>', end='')
                character_name = str(input())
                if 3 < len(character_name) < 20 and re.findall(r'\d', character_name) == []:
                    print(character_name)
                    return character_name
                else:
                    raise ValueError
            except ValueError:
                print(Style.BRIGHT + Fore.LIGHTCYAN_EX + 'Данные введены неверно, попробуйте еще раз')


    def change_draw(self):
        """изменяет поля отрисовки"""
        for i in range(len(self.new_picture)):
            self.new_picture[i] = self.picture_dict[str(i + 1)]
            self.new_text[i] = self.text_dict[str(i + 1)]
        if self.name_str is not None:
            space_1 = int(round((20 - len(Game.change_start(self))) / 2, 0))
            space_2 = 20 - len(Game.change_start(self)) - space_1
            self.new_text[self.name_str] = ' ' * space_1 + Game.change_start(self).capitalize() + ' ' * space_2




if __name__ == '__main__':
    import random
    from dungeon_pictures import *
    from old_dungeon_draw import colors_no_black, Draw

    game = Game(enter_you_name_5_1, enter_you_name_5_2, text_0, text_0_1, None)
    game.change_draw()

    draw1 = Draw(draw_game_5_1, Fore.LIGHTCYAN_EX, enter_you_name_5_1,
                 enter_you_name_5_2, Fore.GREEN, Fore.GREEN)
    draw1.draw()
    game.change_start()

    game1 = Game(enter_you_name_5_3, enter_you_name_5_3, text_1, text_1_1, 1)
    game1.change_draw()

    draw2 = Draw(draw_game_5_1, Fore.LIGHTCYAN_EX, enter_you_name_5_3,
                 enter_you_name_5_4, Fore.GREEN, Fore.GREEN)
    draw2.draw()

    def load(self):
        with open('save.txt', 'r') as save:
            t = json.loads(save.read())

    def save(self):
        with open('save.txt', 'w') as save:
            save.write(json.dumps(save_file))



