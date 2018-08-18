from colorama import init, Fore, Back, Style
from dungeon_draw import cls
import json

# save_hero = {'name': ['race', 'sex', 'age', 'strange', 'weapon', 'health=100', 'armor', 'stamina=100', 'manna=100', 'ulta']}

save_file = {
    'Гарош': ['орк', 'мужская особь', 'среднего возраста', 'средний показатель', 'массивный топор', 100, 10, 100, 0,
              'кратковременно впадает в ярость, незначительно увеличиваются все показатели'],
}

class Game:

    def __init__(self, draw_repeat=None, picture=None, text=None, choice= None, name=None, params=None):
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

    def sex_choice(self):
        if self.choice == 1:
            return 'мужчина'
        elif self.choice == 2:
            return 'женщина'

    def save(self):
        with open('save.txt', 'r') as save:
            characters = json.loads(save.read())
            if self.params:
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


            # with open('save.txt', 'r') as save:
            #     char = json.loads(save.read())
            #     print(char)
            #     char[self.name][0] = self.params
            # with open('save.txt', 'w') as save:
            #     save.write(char)
        # except FileExistsError:
        #     pass

    # def save(self):
    #     """метод создает или загружает save фаил"""
    #     try:
    #         with open('save.txt', 'x') as save:
    #             save.write(json.dumps(save_file))
    #         print('создан сайв')
    #     except FileExistsError:
    #         print('таокй файл уже есть')


            # with open('save.txt', 'w') as save:
            #     save.write(json.dumps(char))

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
    game = Game()
    game.save()



