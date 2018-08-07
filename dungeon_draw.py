from colorama import init, Fore, Back, Style

def picture(change):

    original_picture = \
        {'frame1a': '╔', 'canvas1a': '════════════════════════════════════════════', 'frame2a': '═', 'canvas2a': '══════════════════════════════════════════════════════', 'frame3a': '╗\n',
         'frame1b': '║', 'canvas1b': '                                            ', 'frame2b': ' ', 'canvas2b': '                                                      ', 'frame3b': '║\n',
         'frame1c': '║', 'canvas1c': '                                            ', 'frame2c': ' ', 'canvas2c': '                                                      ', 'frame3c': '║\n',
         'frame1d': '║', 'canvas1d': '                                            ', 'frame2d': ' ', 'canvas2d': '                                                      ', 'frame3d': '║\n',
         'frame1e': '║', 'canvas1e': '                                            ', 'frame2e': ' ', 'canvas2e': '                                                      ', 'frame3e': '║\n',
         'frame1f': '║', 'canvas1f': '                                            ', 'frame2f': ' ', 'canvas2f': '                                                      ', 'frame3f': '║\n',
         'frame1g': '║', 'canvas1g': '                                            ', 'frame2g': ' ', 'canvas2g': '                                                      ', 'frame3g': '║\n',
         'frame1h': '║', 'canvas1h': '                                            ', 'frame2h': ' ', 'canvas2h': '                                                      ', 'frame3h': '║\n',
         'frame1i': '║', 'canvas1i': '                                            ', 'frame2i': ' ', 'canvas2i': '                                                      ', 'frame3i': '║\n',
         'frame1k': '║', 'canvas1k': '                                            ', 'frame2k': ' ', 'canvas2k': '                                                      ', 'frame3k': '║\n',
         'frame1l': '║', 'canvas1l': '                                            ', 'frame2l': ' ', 'canvas2l': '                                                      ', 'frame3l': '║\n',
         'frame1m': '║', 'canvas1m': '                                            ', 'frame2m': ' ', 'canvas2m': '                                                      ', 'frame3m': '║\n',
         'frame1n': '║', 'canvas1n': '                                            ', 'frame2n': ' ', 'canvas2n': '                                                      ', 'frame3n': '║\n',
         'frame1o': '║', 'canvas1o': '                                            ', 'frame2o': ' ', 'canvas2o': '                                                      ', 'frame3o': '║\n',
         'frame1p': '║', 'canvas1p': '                                            ', 'frame2p': ' ', 'canvas2p': '                                                      ', 'frame3p': '║\n',
         'frame1q': '║', 'canvas1q': '                                            ', 'frame2q': ' ', 'canvas2q': '                                                      ', 'frame3q': '║\n',
         'frame1r': '║', 'canvas1r': '                                            ', 'frame2r': ' ', 'canvas2r': '                                                      ', 'frame3r': '║\n',
         'frame1s': '║', 'canvas1s': '                                            ', 'frame2s': ' ', 'canvas2s': '                                                      ', 'frame3s': '║\n',
         'frame1t': '║', 'canvas1t': '                                            ', 'frame2t': ' ', 'canvas2t': '                                                      ', 'frame3t': '║\n',
         'frame1v': '╚', 'canvas1v': '════════════════════════════════════════════', 'frame2v': '═', 'canvas2v': '══════════════════════════════════════════════════════', 'frame3v': '╝\n', }

    original_numbers = ['frame1a', 'canvas1a', 'frame2a', 'canvas2a', 'frame3a',
                        'frame1b', 'canvas1b', 'frame2b', 'canvas2b', 'frame3b',
                        'frame1c', 'canvas1c', 'frame2c', 'canvas2c', 'frame3c',
                        'frame1d', 'canvas1d', 'frame2d', 'canvas2d', 'frame3d',
                        'frame1e', 'canvas1e', 'frame2e', 'canvas2e', 'frame3e',
                        'frame1f', 'canvas1f', 'frame2f', 'canvas2f', 'frame3f',
                        'frame1g', 'canvas1g', 'frame2g', 'canvas2g', 'frame3g',
                        'frame1h', 'canvas1h', 'frame2h', 'canvas2h', 'frame3h',
                        'frame1i', 'canvas1i', 'frame2i', 'canvas2i', 'frame3i',
                        'frame1k', 'canvas1k', 'frame2k', 'canvas2k', 'frame3k',
                        'frame1l', 'canvas1l', 'frame2l', 'canvas2l', 'frame3l',
                        'frame1m', 'canvas1m', 'frame2m', 'canvas2m', 'frame3m',
                        'frame1n', 'canvas1n', 'frame2n', 'canvas2n', 'frame3n',
                        'frame1o', 'canvas1o', 'frame2o', 'canvas2o', 'frame3o',
                        'frame1p', 'canvas1p', 'frame2p', 'canvas2p', 'frame3p',
                        'frame1q', 'canvas1q', 'frame2q', 'canvas2q', 'frame3q',
                        'frame1r', 'canvas1r', 'frame2r', 'canvas2r', 'frame3r',
                        'frame1s', 'canvas1s', 'frame2s', 'canvas2s', 'frame3s',
                        'frame1t', 'canvas1t', 'frame2t', 'canvas2t', 'frame3t',
                        'frame1v', 'canvas1v', 'frame2v', 'canvas2v', 'frame3v']

    original_frames = ['frame1a', 'frame2a',  'frame3a', 'frame1b', 'frame2b',  'frame3b',
                       'frame1c', 'frame2c',  'frame3c', 'frame1d', 'frame2d',  'frame3d',
                       'frame1e', 'frame2e',  'frame3e', 'frame1f', 'frame2f',  'frame3f',
                       'frame1g', 'frame2g',  'frame3g', 'frame1h', 'frame2h',  'frame3h',
                       'frame1i', 'frame2i',  'frame3i', 'frame1k', 'frame2k',  'frame3k',
                       'frame1l', 'frame2l',  'frame3l', 'frame1m', 'frame2m',  'frame3m',
                       'frame1n', 'frame2n',  'frame3n', 'frame1o', 'frame2o',  'frame3o',
                       'frame1p', 'frame2p',  'frame3p', 'frame1q', 'frame2q',  'frame3q',
                       'frame1r', 'frame2r',  'frame3r', 'frame1s', 'frame2s',  'frame3s',
                       'frame1t', 'frame2t',  'frame3t', 'frame1v', 'frame2v',  'frame3v']

    if change is None:
        return original_picture, original_numbers, original_frames
    else:
        for key, vol in change.items():
            original_picture[key] = vol[0]
        return original_picture, original_numbers, original_frames

class Draw:
    """клас отрисовки 'как бы' графики"""
    new_numbers = []

    def __init__(self, draw_picture, size_picture, color_frame, color_change):
        self.draw_picture = draw_picture
        self.size_picture = size_picture
        self.color_frame = color_frame
        self.color_change = color_change

    def draw(self):
        if self.size_picture is None:
            self.new_numbers = self.draw_picture[1]
        elif self.size_picture > len(self.draw_picture[1]):
            return print(Fore.LIGHTGREEN_EX + Back.MAGENTA + 'аргумент picture() не может быть больше 100 !!!')
        else:
            self.new_numbers = self.draw_picture[1][0: self.size_picture]

        for number in self.new_numbers:
            if number in self.color_change:
                print(self.color_change[number][1] + self.color_change[number][2] + self.draw_picture[0][number],
                      end='')
            else:
                print(self.color_frame[0] + self.color_frame[1] + self.draw_picture[0][number], end='')


colors = (Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE)
colors_no_black = (Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE)
colors_back = (Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE)
colors_style = (Style.DIM, Style.NORMAL, Style.BRIGHT)



if __name__ == '__main__':

    b = {'frame1b': ['#', Fore.LIGHTCYAN_EX, Back.BLACK],
         'canvas1b': ['                                       место', Fore.GREEN, Back.BLACK],
         'frame2b': [' ', Fore.LIGHTCYAN_EX, Back.BLACK],
         'canvas2b': ['для проверки                                          ', Fore.GREEN, Back.BLACK],
         'frame3b': ['#\n', Fore.LIGHTCYAN_EX, Back.BLACK],
         'frame1l': ['╚', Fore.LIGHTCYAN_EX, Back.BLACK],
         'canvas1l': ['════════════════════════════════════════════', Fore.LIGHTCYAN_EX, Back.BLACK],
         'frame2l': ['═', Fore.LIGHTCYAN_EX, Back.BLACK],
         'canvas2l': ['══════════════════════════════════════════════════════', Fore.LIGHTCYAN_EX, Back.BLACK],
         'frame3l': ['╝\n', Fore.LIGHTCYAN_EX, Back.BLACK]}

    a = Draw(picture(b), 55, b['frame1b'][1:], b)
    a.draw()

    m = {'frame1c': ['#', Fore.LIGHTCYAN_EX, Back.BLACK],
         'canvas1c': ['                                       место', Fore.GREEN, Back.BLACK],
         'frame2c': [' ', Fore.LIGHTCYAN_EX, Back.BLACK],
         'canvas2c': ['для проверки                                          ', Fore.GREEN, Back.BLACK],
         'frame3c': ['#\n', Fore.LIGHTCYAN_EX, Back.BLACK],
         'frame1m': ['╚', Fore.LIGHTCYAN_EX, Back.BLACK],
         'canvas1m': ['════════════════════════════════════════════', Fore.LIGHTCYAN_EX, Back.BLACK],
         'frame2m': ['═', Fore.LIGHTCYAN_EX, Back.BLACK],
         'canvas2m': ['══════════════════════════════════════════════════════', Fore.LIGHTCYAN_EX, Back.BLACK],
         'frame3m': ['╝\n', Fore.LIGHTCYAN_EX, Back.BLACK]}

    n = Draw(picture(m), 60, m['frame1m'][1:], m)
    n.draw()

    c = {'frame1m': ['#', Fore.LIGHTCYAN_EX, Back.BLACK],
         'canvas1m': ['                                       место', Fore.GREEN, Back.BLACK],
         'frame2m': [' ', Fore.LIGHTCYAN_EX, Back.BLACK],
         'canvas2m': ['для проверки                                          ', Fore.GREEN, Back.BLACK],
         'frame3m': ['#\n', Fore.LIGHTCYAN_EX, Back.BLACK],}

    k = Draw(picture(c), None, c['frame1m'][1:], c)
    k.draw()