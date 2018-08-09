from colorama import init, Fore, Back, Style
import random
import os

colors = (Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE)
colors_no_black = (Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE,
                   Fore.LIGHTRED_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTMAGENTA_EX,
                   Fore.LIGHTCYAN_EX, Fore.LIGHTWHITE_EX)
colors_back = (Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE)
colors_style = (Style.DIM, Style.NORMAL, Style.BRIGHT)


def picture(change):
    """СШК (Стандартная шаблонная консрукция)  (с) ваха ^_^,  функция  задает  изначальные паратметры полей
    отрисовки рамки и картинок, ее можно изменять добавляя нужные поля.  Для уменьшеня размера достаточно в
    классе Draw() в аргументе size_picture указать нужное значение, для увеличения добавить новые фрагменты

    пример каким должен быть change: {'frame1a': ['╔', Fore.LIGHTCYAN_EX, Back.BLACK, ], }
    -ключ это поле "СШК", которое хотим заменить.
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
    изначальная модель.
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
        """основной метод отрисовки нашей графики, принимает положительные числа или "None" тем самым можно "оберезать"
           нашу СШК. None передаст размеры СШК в изначальном виде, при этом все внесенные измения сохраняются. """

        if self.size_picture is None:
            self.new_keys = self.draw_picture[1]
        elif self.size_picture > len(self.draw_picture[1])/self.picture_size()[1] or self.size_picture < 0:
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
                print(self.draw_picture[3]['None'][0]+self.draw_picture[3]['None'][1]+self.draw_picture[0][key], end='')
            else:
                print(self.color_frame[0] + self.color_frame[1] + self.draw_picture[0][key], end='')

    def window_size(self):
        """задает размер окна в windows терминале(нужен при компиляции)"""
        os.system(f"mode con cols={self.picture_size()[0]} "
                  f"lines={int(len(self.draw_picture[2]) / self.picture_size()[2] + 5)}")


if __name__ == '__main__':

    b = {'frame1b': ['#', Fore.LIGHTCYAN_EX, Back.BLACK],
         'canvas2b': ['                                       место', Fore.GREEN, Back.BLACK],
         'frame2b': [' ', Fore.LIGHTCYAN_EX, Back.BLACK],
         'canvas4b': ['для проверки                                          ', Fore.GREEN, Back.BLACK],
         'frame3b': ['#\n', Fore.LIGHTCYAN_EX, Back.BLACK],
         'frame1l': ['╚', Fore.LIGHTCYAN_EX, Back.BLACK],
         'canvas2l': ['════════════════════════════════════════════', Fore.LIGHTCYAN_EX, Back.BLACK],
         'frame2l': ['═', Fore.LIGHTCYAN_EX, Back.BLACK],
         'canvas4l': ['══════════════════════════════════════════════════════', Fore.LIGHTCYAN_EX, Back.BLACK],
         'frame3l': ['╝\n', Fore.LIGHTCYAN_EX, Back.BLACK]}

    a = Draw(picture(b), -11, b['frame1b'][1:])
    a.window_size()
    a.draw()

    m = {'frame1c': ['#', Fore.LIGHTMAGENTA_EX, Back.BLACK],
         'canvas2c': ['                                       место', Fore.GREEN, Back.BLACK],
         'frame2c': [' ', Fore.LIGHTCYAN_EX, Back.BLACK],
         'canvas4c': ['для проверки                                          ', Fore.GREEN, Back.BLACK],
         'frame3c': ['#\n', Fore.LIGHTCYAN_EX, Back.BLACK],
         'frame1m': ['╚', Fore.LIGHTCYAN_EX, Back.BLACK],
         'canvas2m': ['════════════════════════════════════════════', Fore.LIGHTCYAN_EX, Back.BLACK],
         'frame2m': ['═', Fore.LIGHTCYAN_EX, Back.BLACK],
         'canvas4m': ['══════════════════════════════════════════════════════', Fore.LIGHTCYAN_EX, Back.BLACK],
         'frame3m': ['╝\n', Fore.LIGHTCYAN_EX, Back.BLACK]}

    n = Draw(picture(m), 12, m['frame1c'][1:])
    n.draw()

    c = {'frame1m': ['#', Fore.LIGHTYELLOW_EX, Back.BLACK],
         'canvas2m': ['                                       место', Fore.GREEN, Back.BLACK],
         'frame2m': [' ', Fore.LIGHTCYAN_EX, Back.BLACK],
         'canvas4m': ['для проверки                                          ', Fore.GREEN, Back.BLACK],
         'frame3m': ['#\n', Fore.LIGHTCYAN_EX, Back.BLACK],}

    k = Draw(picture(c), None, c['frame1m'][1:])
    k.draw()

    t = Draw(picture(None), None, None)
    t.draw()

    from dungeon_pictures import draw_skull

    g = Draw(picture(draw_skull), None, draw_skull['canvas2a'][1:])
    g.draw()

