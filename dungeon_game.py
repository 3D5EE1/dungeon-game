from colorama import init, Fore, Back, Style
from dungeon_draw import cls
import json

"""save_hero = {'name':
['пол', 'расса', 'класс', 'возраст', 'оружие', 'здровье', 'броня', 'сила', 'выносливасть', 'манна', 'ульта']}"""

save_file = {
    'Гарош': ['мужская особь', 'орк', 'воин', 'среднего возраста', 'массивный топор', 100, 30, 25, 60, 0,
              'кратковременно впадает в ярость, незначительно увеличиваются все показатели'],
}


def char_params(char):
    params = [None, None, None, None, None, None, None, None, None, None, None]
    if char[0] == 1:
        params[0] = 'мужчина'
    elif char[0] == 2:
        params[0] = 'женщина'

    if char[1] == 1:
        params[1] = 'человек'
        if char[2] == 1:
            params[2] = 'воин'
            params[3] = str(char[3])
            params[4] = 'меч'
            params[5] = '100'''
            params[6] = '50'''
            params[7] = '20'''
            params[8] = '50'''
            params[9] = '10'''
            params[10] = 'кратковременно впадает в ярость'
        elif char[2] == 2:
            params[2] = 'лучник'
            params[3] = str(char[3])
            params[4] = 'лук'
            params[5] = '100'
            params[6] = '15'
            params[7] = '60'
            params[8] = '50'
            params[9] = '10'
            params[10] = 'серия метких выстрелов'
        elif char[2] == 3:
            params[2] = 'маг'
            params[3] = str(char[3])
            params[4] = 'посох'
            params[5] = '60'
            params[6] = '15'
            params[7] = '10'
            params[8] = '20'
            params[9] = '100'
            params[10] = 'увеличение мощности заклинаний'
        elif char[2] == 4:
            params[2] = 'вор'
            params[3] = str(char[3])
            params[4] = 'меч'
            params[5] = '85'
            params[6] = '35'
            params[7] = '60'
            params[8] = '60'
            params[9] = '15'
            params[10] = 'коварный удар игнорирующий доспех'
    elif char[1] == 2:
        params[1] = 'эльф'
        if char[2] == 1:
            params[2] = 'воин'
            params[3] = str(char[3])
            params[4] = 'эльфийская сабля'
            params[5] = '90'
            params[6] = '55'
            params[7] = '15'
            params[8] = '70'
            params[9] = '30'
            params[10] = 'кратковременно впадает в ярость'
        elif char[2] == 2:
            params[2] = 'лучник'
            params[3] = str(char[3])
            params[4] = 'эльфийский лук'
            params[5] = '90'
            params[6] = '15'
            params[7] = '75'
            params[8] = '65'
            params[9] = '20'
            params[10] = 'серия метких выстрелов'
        elif char[2] == 3:
            params[2] = 'маг'
            params[3] = str(char[3])
            params[4] = 'посох'
            params[5] = '70'
            params[6] = '10'
            params[7] = '10'
            params[8] = '25'
            params[9] = '130'
            params[10] = 'увеличение мощности заклинаний'
    elif char[1] == 3:
        params[1] = 'орк'
        if char[2] == 1:
            params[2] = 'воин'
            params[3] = str(char[3])
            params[4] = 'меч'
            params[5] = '130'
            params[6] = '25'
            params[7] = '35'
            params[8] = '70'
            params[9] = '0'
            params[10] = 'кратковременно впадает в ярость'
        elif char[2] == 2:
            params[2] = 'разведчик'
            params[3] = str(char[3])
            params[4] = 'метательный топор'
            params[5] = '120'
            params[6] = '10'
            params[7] = '80'
            params[8] = '65'
            params[9] = '0'
            params[10] = 'серия метких бросков'
        elif char[2] == 3:
            params[2] = 'шаман'
            params[3] = str(char[3])
            params[4] = 'тотем'
            params[5] = '70'
            params[6] = '5'
            params[7] = '20'
            params[8] = '25'
            params[9] = '85'
            params[10] = 'увеличение мощности заклинаний'
    elif char[1] == 4:
        params[1] = 'гном'
        if char[2] == 1:
            params[2] = 'воин'
            params[3] = str(char[3])
            params[4] = 'меч'
            params[5] = '120'
            params[6] = '70'
            params[7] = '40'
            params[8] = '60'
            params[9] = '0'
            params[10] = 'кратковременно впадает в ярость'
        elif char[2] == 2:
            params[2] = 'копейщик'
            params[3] = str(char[3])
            params[4] = 'мететельное копье'
            params[5] = '130'
            params[6] = '24'
            params[7] = '65'
            params[8] = '65'
            params[9] = '0'
            params[10] = 'серия метких бросков'
    return params


def params_char(picture=None, params=None):
    m = 0
    for key in picture.keys():
        for i in range(len(params)):
            picture[key] = params[m]
        m += 1
    return picture


class Game:

    def __init__(self, draw_repeat=None, picture=None, text=None, choice=None, name=None, params=None):
        self.draw_repeat = draw_repeat
        self.picture = picture
        self.text = text
        self.choice = choice
        self.name = name
        self.params = params

    def check_name(self):
        while True:
            try:
                print(Fore.GREEN + Back.BLACK + '\n ваше имя: ', end='')
                character_name = str(input())
                if 1 < len(character_name) < 21 and character_name.isalpha():
                    cls()
                    return character_name.capitalize()
                else:
                    raise ValueError
            except ValueError:
                cls()
                self.draw_repeat.draw()
                print(
                    Style.BRIGHT + Fore.LIGHTCYAN_EX + '\n     имя персонажа может состоять только из букв \n'
                                                       '           длина имени от 2 до 20 символов \n'
                                                       '             цифр в имене быть не должно',
                    Style.RESET_ALL
                )

    def print_text(self):
        for key, vol in self.text.items():
            if key in self.picture:
                self.picture[key][0] = vol + ' ' * (len(self.picture[key][0]) - len(vol))
        return self.picture

    def save(self):
        with open('save.txt', 'r') as save:
            characters = json.loads(save.read())  # загружает фаил
            if self.name and self.params:
                characters[self.name] += [self.params]
                with open('save.txt', 'w') as save_game:
                    save_game.write(json.dumps(characters))
            elif self.name in characters:
                self.draw_repeat.draw()
                return False
            elif self.name not in characters:
                characters[self.name] = []
                with open('save.txt', 'w') as save_game:
                    save_game.write(json.dumps(characters))
                return True

    def save_new_game(self):
        try:
            with open('save.txt', 'x') as save:
                save.write(json.dumps(save_file))
            return self.save()
        except FileExistsError:  # если файл уже есть
            return self.save()

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

    char_choice = {'canvas4c': 'женщина', 'canvas4e': 'эльф', 'canvas4f': 'лучник', 'canvas4g': 23, 'canvas4h': 'эльфийский лук', 'canvas4i': 90, 'canvas4k': 15, 'canvas4l': 75, 'canvas4m': 65, 'canvas4n': 20, 'canvas4o': 'серия метких выстрелов'}


    params = params_char(pictures(12), char_params([1, 2, 2, 44]))
    print(params)
    picture_params = Game(picture=pictures(12), text=params).print_text()
    print(picture_params)
    draw = Draw(canvas(pictures(11), picture_params), 17)
    draw.draw()
