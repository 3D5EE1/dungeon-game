from colorama import init, Fore, Back, Style
import random
import os

colors = (Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE)
colors_no_black = (Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE,
                   Fore.LIGHTRED_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTMAGENTA_EX,
                   Fore.LIGHTCYAN_EX, Fore.LIGHTWHITE_EX)
colors_back = (Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE)
colors_style = (Style.DIM, Style.NORMAL, Style.BRIGHT)


def picture(change, append_original_picture=None):
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
        {'frame1a': '╔', 'canvas1a': '', 'canvas2a': '════════════════════════════════════════════', 'canvas3a': '',
         'frame2a': '═', 'canvas4a': '══════════════════════════════════════════════════════', 'frame3a': '╗\n',
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

    if append_original_picture is None:
        pass
    else:
        for key, vol in append_original_picture.items():
            original_picture[key] = vol

    original_numbers = []
    original_frames = []

    for i in original_picture:
        original_numbers.append(i)
        if 'frame' in i:
            original_frames.append(i)

    original_colors = {'None': [random.choice(colors_no_black), Back.BLACK]}

    if change is None:
        return original_picture, original_numbers, original_frames, original_colors
    else:
        for key, vol in change.items():
            original_picture[key] = vol[0]
            original_colors[key] = [vol[1], vol[2]]
        return original_picture, original_numbers, original_frames, original_colors


class Draw:
    """клас отрисовки 'псевдографики'
    draw_picture - принимает  функцию  picture(change)  с  измененными  полями, если change ровняется None, передается
    изначальная модель, picture(append_original_picture) добавляет новые фрагменты.
    size_picture - "обрезает" СШК переданную в функции picture(change), принимает число строк, которые вы хотите отоб-
    разить, строки от 0 до переданного заначение.
    color_frame  - принимает список цвета и фона для рамки нашей графики, None принимает рандомный цвет на черном фоне
    """
    new_keys = []

    def __init__(self, draw_picture, size_picture, color_frame):
        self.draw_picture = draw_picture
        self.size_picture = size_picture
        self.color_frame = color_frame

    def picture_size(self):
        length_first_line = [0, 0, 0]

        for key, vol in self.draw_picture[0].items():
            length_first_line[0] += len(vol)
            length_first_line[1] += 1
            if 'frame' in key:
                length_first_line[2] += 1
            if '\n' in vol:
                break

        return length_first_line

    def draw(self):
        """основной метод отрисовки нашей графики, принимает положительные числа или "None" тем самым можно "обрезать"
           нашу СШК. None передаст размеры СШК в изначальном виде, при этом все внесенные измения сохраняются. """

        if self.size_picture is None:
            self.new_keys = self.draw_picture[1]
        elif self.size_picture > len(self.draw_picture[1]) / self.picture_size()[1] or self.size_picture < 0:
            return print(
                Fore.LIGHTWHITE_EX + Back.MAGENTA
                + f'второй аргумент Draw() "size_picture" не может быть меньше 0 или больше '
                  f'{int(len(self.draw_picture[1]) / self.picture_size()[1])} !!! ваше значение: {self.size_picture}'
            )
        else:
            self.new_keys = self.draw_picture[1][0: self.size_picture * self.picture_size()[1]]

        for key in self.new_keys:
            if key in self.draw_picture[3]:
                print(self.draw_picture[3][key][0] + self.draw_picture[3][key][1] + self.draw_picture[0][key], end='')

            elif self.color_frame is None:
                if 'canvas2a'in self.draw_picture[3]:
                    print(self.draw_picture[3]['canvas2a'][0]
                          + self.draw_picture[3]['canvas2a'][1] + self.draw_picture[0][key], end='')
                else:
                    print(self.draw_picture[3]['None'][0]
                          + self.draw_picture[3]['None'][1] + self.draw_picture[0][key], end='')
            else:
                print(self.color_frame[0] + self.color_frame[1] + self.draw_picture[0][key], end='')

    def window_size(self):
        """задает размер окна в windows терминале(нужен при компиляции)"""
        os.system(f"mode con cols={self.picture_size()[0]} "
                  f"lines={int(len(self.draw_picture[2]) / self.picture_size()[2] + 5)}")


if __name__ == '__main__':
    from dungeon_pictures import draw_skull

    a = {'frame1w': '╚', 'canvas1w': '', 'canvas2w': '═══════════════W════════════════════════════', 'canvas3w': '',
         'frame2w': '═', 'canvas4w': '═════════════════════════════w════════════════════════', 'frame3w': '╝\n',
         'frame1x': '╚', 'canvas1x': '', 'canvas2x': '═══════════X════════════════════════════════', 'canvas3x': '',
         'frame2x': '═', 'canvas4x': '═══════════════════════════════x══════════════════════', 'frame3x': '╝\n',
         'frame1y': '╚', 'canvas1y': '', 'canvas2y': '══════════════Y═════════════════════════════', 'canvas3y': '',
         'frame2y': '═', 'canvas4y': '════════════════════════════════y═════════════════════', 'frame3y': '╝\n',
         'frame1z': '╚', 'canvas1z': '', 'canvas2z': '═════════════Z══════════════════════════════', 'canvas3z': '',
         'frame2z': '═', 'canvas4z': '═════════════════════════════════z════════════════════', 'frame3z': '╝\n', }

    a1 = Draw(picture(draw_skull, a), None, None)
    a1.window_size()
    print('\na1')
    a1.draw()

    a2 = Draw(picture(draw_skull), -1, None)
    print('\na2')
    a2.draw()

    a3 = Draw(picture(draw_skull), 21, draw_skull['canvas2a'][1:])
    print('\na3')
    a3.draw()

    a4 = Draw(picture(draw_skull), 10, draw_skull['canvas2a'][1:])
    print('\na4')
    a4.draw()

    a5 = Draw(picture(draw_skull), None, draw_skull['canvas2a'][1:])
    print('\na5')
    a5.draw()

    a6 = Draw(picture(draw_skull), None, None)
    print('\na6')
    a6.draw()
