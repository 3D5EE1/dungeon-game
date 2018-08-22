from colorama import init, Fore, Back, Style
from dungeon_draw import cls
import json

"""save_hero = {'name':
['пол', 'расса', 'класс', 'возраст', 'оружие', 'здровье', 'броня', 'сила', 'выносливасть', 'манна', 'ульта']}"""

save_file = {}

enemy_file = {
    'Гарош': ['мужская особь', 'орк', 'воин', 'среднего возраста', 'массивный топор', 100, 30, 25, 60, 0,
              'кратковременно впадает в ярость, незначительно увеличиваются все показатели'],
}


def enemy_save():
    try:
        with open('save.txt', 'x') as save:
            save.write(json.dumps(enemy_file))
    except FileExistsError:
        pass


def new_enemy():
    try:
        print(Fore.LIGHTYELLOW_EX + 'Вам необходимо ввести информация по вашему противнику,\n'
              'мы ни как не будем  вас ограничивать, можете  проявить\n'
              'фантазию,  но помните от того  какие данные вы введете\n'
              'будет зависить то с кем вам предстаит сражаться.\n'
              'Помните, что показатель здровья, силы, брони, возраста\n'
              'выносливости и манны являются числовыми значениями.\n'
              'В имени не должно быть цифр.\n', Fore.GREEN)
        name = str(input('имя персонажа: ')).capitalize()
        if name.isalpha() is False:
            raise ValueError
        with open('save.txt', 'r') as save:
            characters = json.loads(save.read())
        with open('enemy.txt', 'r') as save:
            enemy_characters = json.loads(save.read())
        if name in characters or name in enemy_characters:
            raise TypeError
        else:
            enemy = []
            enemy += [str(input('пол: '))]
            enemy += [str(input('расса: '))]
            enemy += [str(input('класс: '))]
            val = int(input('возраст: '))
            enemy += [str(val)]
            enemy += [str(input('оружие: '))]
            val = int(input('здровье: '))
            enemy += [str(val)]
            val = int(input('броня: '))
            enemy += [str(val)]
            val = int(input('сила: '))
            enemy += [str(val)]
            val = int(input('выносливасть: '))
            enemy += [str(val)]
            val = int(input('манна: '))
            enemy += [str(val)]
            enemy += [str(input('ульта: '))]
            print()
            enemy_characters[name] = enemy
            with open('enemy.txt', 'w') as save_game:
                save_game.write(json.dumps(enemy_characters))
            return True
    except ValueError:
        cls()
        print(Fore.LIGHTRED_EX + 'Вы   допустили  ошибку  при  вводе  данных,  прочтите \n'
                                 'внимательно условие!\n')
        return False
    except TypeError:
        cls()
        print(Fore.LIGHTRED_EX + 'Увы,  но персонаж с таким именем уже есть,  попробуйте \n'
                                 'снова!!!\n')
        return False


def char_params(char):
    params = []
    if char[0] == 1:
        params += ['мужчина']
    elif char[0] == 2:
        params += ['женщина']

    if char[1] == 1:
        params += ['человек']

        if char[2] == 1:
            params += ['воин', str(char[3]), 'меч', '100', '50', '20', '50', '10', 'кратковременно впадает в ярость']
        elif char[2] == 2:
            params += ['лучник', str(char[3]), 'лук', '100', '15', '60', '50', '10', 'серия метких выстрелов']
        elif char[2] == 3:
            params += ['маг', str(char[3]), 'посох', '60', '15', '10', '20', '100', 'увеличение мощности заклинаний']
        elif char[2] == 4:
            params += ['вор', str(char[3]), 'меч', '85', '35', '60', '60', '15', 'удары игнорируют доспехи']

    elif char[1] == 2:
        params += ['эльф']

        if char[2] == 1:
            params += ['воин', str(char[3]),
                       'эльфийская сабля', '90', '55', '15', '70', '30', 'кратковременно впадает в ярость']
        elif char[2] == 2:
            params += ['лучник', str(char[3]), 'эльфийский лук', '90', '15', '75', '65', '20', 'серия метких выстрелов']
        elif char[2] == 3:
            params += ['маг', str(char[3]), 'посох', '70', '10', '10', '25', '130',  'увеличение мощности заклинаний']

    elif char[1] == 3:
        params += ['орк']

        if char[2] == 1:
            params += ['воин', str(char[3]), 'меч', '130', '25', '35', '70', '0',  'кратковременно впадает в ярость']
        elif char[2] == 2:
            params += [
                'разведчик', str(char[3]), 'метательный топор', '120', '10', '80', '65', '0',  'серия метких бросков']
        elif char[2] == 3:
            params += ['шаман', str(char[3]), 'тотем', '70', '5', '20', '25', '85',  'увеличение мощности заклинаний']

    elif char[1] == 4:
        params += ['гном']

        if char[2] == 1:
            params += ['воин', str(char[3]), 'меч', '120', '70', '40', '60', '0',  'кратковременно впадает в ярость']
        elif char[2] == 2:
            params += [
                'копейщик', str(char[3]), 'мететельное копье', '130', '24', '65', '65', '0',  'серия метких бросков']

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
                characters[self.name] += self.params
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

    def enemy_save(self):
        try:
            with open('enemy.txt', 'x') as save:
                save.write(json.dumps(enemy_file))
        except FileExistsError:
            pass

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
    # from dungeon_draw import Draw, canvas
    # from dungeon_pictures import pictures
    #
    # char_choice = {'canvas4c': 'женщина', 'canvas4e': 'эльф', 'canvas4f': 'лучник', 'canvas4g': 23, 'canvas4h': 'эльфийский лук', 'canvas4i': 90, 'canvas4k': 15, 'canvas4l': 75, 'canvas4m': 65, 'canvas4n': 20, 'canvas4o': 'серия метких выстрелов'}
    #
    #
    # params = params_char(pictures(12), char_params([1, 2, 2, 44]))
    # print(params)
    # picture_params = Game(picture=pictures(12), text=params).print_text()
    # print(picture_params)
    # draw = Draw(canvas(pictures(11), picture_params), 17)
    # draw.draw()
        print(new_enemy())
