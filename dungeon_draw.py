from colorama import init, Fore, Back, Style
import random
import os

colors = (Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE)
colors_no_black = (
    Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE, Fore.LIGHTRED_EX,
    Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTCYAN_EX,
    Fore.LIGHTWHITE_EX
)
colors_ligth_no_back = (
                   Fore.LIGHTRED_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTMAGENTA_EX,
                   Fore.LIGHTCYAN_EX, Fore.LIGHTWHITE_EX
)
colors_back = (Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE)
colors_style = (Style.DIM, Style.NORMAL, Style.BRIGHT)


def cls():
    os.system('cls')


def canvas(fragment=None, add=None, change=None):
    """СШК (Стандартная шаблонная консрукция)  (с) ваха ^_^,  функция  задает  изначальные паратметры полей
    отрисовки рамки и картинок, ее можно изменять добавляя нужные поля.  Для уменьшеня размера достаточно в
    классе Draw() в аргументе "size_picture" указать нужное значение, для добавления новых фрагментов нужно
    передать словарь с дополнительными полями в агрумент picture(append_original_picture), ниже указано как
    должены выглядить новые фрагменты.

    пример каким должен быть change или append_original_picture:
                                                      {'frame1a': ['╔', Fore.CYAN, Back.BLACK, ], }
    -ключ это поле "СШК", которое хотим заменить (для change) или добавить (для append_original_picture)
    -значение ключа это список:
                             -первым его аргументом будет то каким вы хотите видеть содержание  строки поля
                              отрисовки, обращайте внимание на длину остальных полей, иначе результат может
                              получиться не таким как вы планировали.
                             -вторым аргументом передается цвет символов в поле отрисовки.
                             -третьим, фон поля."""

    original_picture = \
        {'frame1a': '╠', 'canvas1a': '', 'canvas2a': '════════════════════════════════════════════', 'canvas3a': '',
         'frame2a': '═', 'canvas4a': '══════════════════════════════════════════════════════', 'frame3a': '╣\n',
         'frame1b': '║', 'canvas1b': '', 'canvas2b': '                                            ', 'canvas3b': '',
         'frame2b': ' ', 'canvas4b': '                                                      ', 'frame3b': '║\n',
         'frame1c': '║', 'canvas1c': '', 'canvas2c': '                                            ', 'canvas3c': '',
         'frame2c': ' ', 'canvas4c': '                                                      ', 'frame3c': '║\n',
         'frame1d': '║', 'canvas1d': '', 'canvas2d': '                                            ', 'canvas3d': '',
         'frame2d': ' ', 'canvas4d': '                                                      ', 'frame3d': '║\n',
         'frame1e': '║', 'canvas1e': '', 'canvas2e': '                                            ', 'canvas3e': '',
         'frame2e': ' ', 'canvas4e': '                                                      ', 'frame3e': '║\n',
         'frame1f': '║', 'canvas1f': '', 'canvas2f': '                                            ', 'canvas3f': '',
         'frame2f': ' ', 'canvas4f': '                                                      ', 'frame3f': '║\n',
         'frame1g': '║', 'canvas1g': '', 'canvas2g': '                                            ', 'canvas3g': '',
         'frame2g': ' ', 'canvas4g': '                                                      ', 'frame3g': '║\n',
         'frame1h': '║', 'canvas1h': '', 'canvas2h': '                                            ', 'canvas3h': '',
         'frame2h': ' ', 'canvas4h': '                                                      ', 'frame3h': '║\n',
         'frame1i': '║', 'canvas1i': '', 'canvas2i': '                                            ', 'canvas3i': '',
         'frame2i': ' ', 'canvas4i': '                                                      ', 'frame3i': '║\n',
         'frame1k': '║', 'canvas1k': '', 'canvas2k': '                                            ', 'canvas3k': '',
         'frame2k': ' ', 'canvas4k': '                                                      ', 'frame3k': '║\n',
         'frame1l': '║', 'canvas1l': '', 'canvas2l': '                                            ', 'canvas3l': '',
         'frame2l': ' ', 'canvas4l': '                                                      ', 'frame3l': '║\n',
         'frame1m': '║', 'canvas1m': '', 'canvas2m': '                                            ', 'canvas3m': '',
         'frame2m': ' ', 'canvas4m': '                                                      ', 'frame3m': '║\n',
         'frame1n': '║', 'canvas1n': '', 'canvas2n': '                                            ', 'canvas3n': '',
         'frame2n': ' ', 'canvas4n': '                                                      ', 'frame3n': '║\n',
         'frame1o': '║', 'canvas1o': '', 'canvas2o': '                                            ', 'canvas3o': '',
         'frame2o': ' ', 'canvas4o': '                                                      ', 'frame3o': '║\n',
         'frame1p': '║', 'canvas1p': '', 'canvas2p': '                                            ', 'canvas3p': '',
         'frame2p': ' ', 'canvas4p': '                                                      ', 'frame3p': '║\n',
         'frame1q': '║', 'canvas1q': '', 'canvas2q': '                                            ', 'canvas3q': '',
         'frame2q': ' ', 'canvas4q': '                                                      ', 'frame3q': '║\n',
         'frame1r': '║', 'canvas1r': '', 'canvas2r': '                                            ', 'canvas3r': '',
         'frame2r': ' ', 'canvas4r': '                                                      ', 'frame3r': '║\n',
         'frame1s': '║', 'canvas1s': '', 'canvas2s': '                                            ', 'canvas3s': '',
         'frame2s': ' ', 'canvas4s': '                                                      ', 'frame3s': '║\n',
         'frame1t': '║', 'canvas1t': '', 'canvas2t': '                                            ', 'canvas3t': '',
         'frame2t': ' ', 'canvas4t': '                                                      ', 'frame3t': '║\n',
         'frame1v': '╚', 'canvas1v': '', 'canvas2v': '════════════════════════════════════════════', 'canvas3v': '',
         'frame2v': '═', 'canvas4v': '══════════════════════════════════════════════════════', 'frame3v': '╝\n', }

    if add is None:  # добавляет поля к fragment или заменяет уже существующие поля
        pass
    else:
        for key, vol in add.items():
            if fragment is None or key not in fragment and key not in original_picture:
                original_picture[key] = vol[0]
            elif len(vol) == 0:
                original_picture.pop(key)
            else:
                fragment[key] = vol

    if change is None:  # дополнительная возможность изменить новый fragment
        pass
    else:
        for key, vol in change.items():
            if len(vol) == 0:
                fragment.pop(key)
            else:
                fragment[key] = vol

    original_keys = []
    original_frames = []

    for key in original_picture:  # копирует все ключи original_picture в original_keys, frame's в original_frames
        original_keys.append(key)
        if 'frame' in key:
            original_frames.append(key)

    original_colors = {'None': [random.choice(colors_no_black), Back.BLACK, '', ]}

    if fragment is None:  # возвращает параметры для дальнейшей отрисовки картинки
        return original_picture, original_keys, original_frames, original_colors
    else:
        for key, vol in fragment.items():
            original_picture[key] = vol[0]
            original_colors[key] = [vol[1], vol[2], vol[3]]
        return original_picture, original_keys, original_frames, original_colors


class Draw:
    """клас отрисовки 'псевдографики'
    draw_picture - принимает  функцию  picture(change)  с  измененными  полями, если change ровняется None, передается
    изначальная модель, picture(append_original_picture) добавляет новые фрагменты.
    size_picture - "обрезает" СШК переданную в функции picture(change), принимает число строк, которые вы хотите отоб-
    разить, строки от 0 до переданного заначение.
    color_frame  - принимает список цвета и фона для рамки нашей графики, None принимает рандомный цвет на черном фоне
    """
    new_keys = []

    def __init__(self, picture=canvas(), size=None, frame=None):
        self.picture = picture
        self.size = size
        self.frame = frame
        self.color = self.picture[3]

    def canvas_size(self):
        """определяет размеры холста"""
        elements_first_line = [0, 0, 0]

        for key, vol in self.picture[0].items():
            elements_first_line[0] += len(vol)
            elements_first_line[1] += 1
            if 'frame' in key:
                elements_first_line[2] += 1
            if '\n' in vol:
                break

        return elements_first_line

    def draw(self):
        """основной метод отрисовки нашей графики, принимает положительные числа или "None" тем самым можно "обрезать"
           нашу СШК. None передаст размеры СШК в изначальном виде, при этом все внесенные измения сохраняются. """

        if self.size is None:
            self.new_keys = self.picture[1]
        elif self.size > len(self.picture[1]) / self.canvas_size()[1] or self.size < 0:
            return print(
                Fore.LIGHTWHITE_EX + Back.MAGENTA
                + f'второй аргумент Draw() "size" не может быть меньше 0 или больше '
                  f'{int(len(self.picture[1]) / self.canvas_size()[1])} !!! ваше значение: {self.size}'
            )
        else:
            self.new_keys = self.picture[1][0: self.size * self.canvas_size()[1]]

        for key in self.new_keys:
            if key in self.color:
                print(self.color[key][0] +
                      self.color[key][1] + self.color[key][2] + self.picture[0][key], end='')

            elif self.frame is None:  # параметры поля Frame
                if 'canvas2a'in self.color:
                    print(self.color['canvas2a'][0] +
                          self.color['canvas2a'][1] + self.color['canvas2a'][2] + self.picture[0][key], end='')
                else:
                    print(self.color['None'][0] +
                          self.color['None'][1] + self.color['None'][2] + self.picture[0][key], end='')
            else:
                print(self.frame[0] + self.frame[1] + self.frame[2] + self.picture[0][key], end='')

    def window_size(self):
        """задает размер окна в windows терминале(нужен при компиляции)"""
        os.system(f"mode con cols={self.canvas_size()[0]} "
                  f"lines={int(len(self.picture[2]) / self.canvas_size()[2] + 10)}")


if __name__ == '__main__':
    from dungeon_pictures import pictures

    test1 = Draw(size=-1)
    print(Fore.WHITE + Back.BLACK + '\ntest1, неверные параметры "обрезания" шаблона')
    test1.window_size()
    test1.draw()

    test2 = Draw(size=21)
    print(Fore.WHITE + Back.BLACK + '\ntest2, неверные параметры "обрезания" шаблона')
    test2.draw()

    test3 = Draw()
    test1.window_size()
    print(Fore.WHITE + Back.BLACK + '\ntest3, только рамка, цвет случайный')
    test3.draw()

    test4 = Draw(canvas(add=pictures(3)))
    print(Fore.WHITE + Back.BLACK + '\ntest4, добавление 4-х полей, цвет рамки случайный')
    test4.draw()

    test5 = Draw(canvas(add=pictures(3)), size=25)
    print(Fore.WHITE + Back.BLACK + '\ntest5, добавление 4-х полей, неверные параметры "обрезания" шаблона')
    test5.draw()

    test6 = Draw(canvas(pictures(0)))
    print(Fore.WHITE + Back.BLACK + '\ntest6, рисует скелета, цвет рамки повторяет рамку скелета')
    test6.draw()

    test7 = Draw(canvas(pictures(0)), size=5)
    print(Fore.WHITE + Back.BLACK + '\ntest7, рисует скелета, обрезает до 5, цвет рамки повторяет рамку скелета')
    test7.draw()

    test8 = Draw(canvas(pictures(0), change={'canvas2a': []}))
    print(Fore.WHITE + Back.BLACK + '\ntest8, рисует скелета, удаляет рамку скелета, цвет рамки случайный')
    test8.draw()

    test9 = Draw(canvas(pictures(0), pictures(3), pictures(2)), None, pictures(0)['canvas2o'][1:])
    print(Fore.WHITE + Back.BLACK + '\ntest9, рисует скелета, добавляет 4 поля, добавляет текст, цвет рамки '
                                    ' как цвет скелета, но рамка скелета из шаблона скелета')
    test9.draw()

    test10 = Draw(canvas(pictures(0), pictures(2), {'canvas2a': []}), None, pictures(2)['canvas4f'][1:])
    print(Fore.WHITE + Back.BLACK + '\ntest10, рисует скелета, добавляет текст, делает цвет рамки как цвет текста')
    test10.draw()