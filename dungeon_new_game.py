from colorama import init, Fore, Back, Style
from dungeon_draw import cls
import re
import json


class Game:

    def __init__(self, draw_repeat=None, picture=None, text=None):
        self.draw_repeat = draw_repeat
        self.picture = picture
        self.text = text

    def check_name(self):
        while True:
            try:
                print(Fore.GREEN + Back.BLACK + '\n >>>', end='')
                character_name = str(input())
                if 1 < len(character_name) < 21 and character_name.isalpha():
                    return character_name.capitalize()
                else:
                    raise ValueError
            except ValueError:
                cls()
                self.draw_repeat.draw()
                print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '\n имя персонажа может состоять только из букв \n'
                                                         '      длина имени от 2 до 20 символов \n'
                                                         '        цифр в имене быть не должно\n'
                                                         '        (в вашем же имени нет цифр)', Style.RESET_ALL)

    def print_text(self):
        cls()
        for key, vol in self.text.items():
            if key in self.picture:
                self.picture[key][0] = vol + ' ' * (len(self.picture[key][0]) - len(vol))
        return self.picture

    # def change_draw(self):
    #
    #     for i in range(len(self.new_picture)):
    #         self.new_picture[i] = self.picture_dict[str(i + 1)]
    #         self.new_text[i] = self.text_dict[str(i + 1)]
    #     if self.name_str is not None:
    #         space_1 = int(round((20 - len(Game.change_start(self))) / 2, 0))
    #         space_2 = 20 - len(Game.change_start(self)) - space_1
    #         self.new_text[self.name_str] = ' ' * space_1 + Game.change_start(self).capitalize() + ' ' * space_2




if __name__ == '__main__':
    from dungeon_draw import Draw, canvas
    from dungeon_pictures import pictures
    game = Game(picture=pictures(7), text={'canvas4c': 'asds'})
    Draw(canvas(game.print_text()), 7).draw()



