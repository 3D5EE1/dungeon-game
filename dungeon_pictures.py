from colorama import init, Fore, Back, Style
from dungeon_draw import colors_no_black
import random

random_color1 = random.choice(colors_no_black)
random_color2 = random.choice(colors_no_black)


def figure(number):
    """('frame_color', 'frame_back', 'canvas1_color', 'canvas1_back', 'canvas2_color', 'canvas2_back')"""

    color = [
        (Fore.LIGHTCYAN_EX, Back.BLACK, random_color1, Back.BLACK, random_color2, Back.BLACK)
    ]

    draw_skull = \
        {'canvas2a': ['════════════════════════════════════════════', color[number][0], color[number][1], ],
         'canvas2c': ['              uu$$$$$$$$$$uu                ', color[number][2], color[number][3], ],
         'canvas2d': ['          uu$$$$$$$$$$$$$$$$$uu             ', color[number][2], color[number][3], ],
         'canvas2e': ['         u$$$$$$$$$$$$$$$$$$$$$u            ', color[number][2], color[number][3], ],
         'canvas2f': ['        u$$$$$$$$$$$$$$$$$$$$$$$u           ', color[number][2], color[number][3], ],
         'canvas2g': ['       u$$$$$$$$$$$$$$$$$$$$$$$$$u          ', color[number][2], color[number][3], ],
         'canvas2h': ['       u$$$$$$$$$$$$$$$$$$$$$$$$$u          ', color[number][2], color[number][3], ],
         'canvas2i': ['       u$$$$$$     $$$     $$$$$$u          ', color[number][2], color[number][3], ],
         'canvas2k': ['        $$$$        u$u      $$$$u          ', color[number][2], color[number][3], ],
         'canvas2l': ['        $$$u        u$u       u$$$          ', color[number][2], color[number][3], ],
         'canvas2m': ['         $$$u       u$$$u     u$$$          ', color[number][2], color[number][3], ],
         'canvas2n': ['         $$$$uu$$$uu_   _$$$uu$$$$          ', color[number][2], color[number][3], ],
         'canvas2o': ['          $$$$$$$         $$$$$$$           ', color[number][2], color[number][3], ],
         'canvas2p': ['             u$$$$$$$u$$$$$$$u              ', color[number][2], color[number][3], ],
         'canvas2q': ['              u$##$$ $ $ $u$$u              ', color[number][2], color[number][3], ],
         'canvas2r': ['    uuu       $$u$_$  $ $ $u$$        uuu   ', color[number][2], color[number][3], ],
         'canvas2s': ['   u$$$$        $$$$$ u$u$u$$$       u$$$$  ', color[number][2], color[number][3], ],
         'canvas2t': ['  $$$$$uu        $$$ $$$$$$       uu$$$$$$  ', color[number][2], color[number][3], ],
         'canvas4f': ['           Добро пожаловать в подземелье              ', color[number][4], color[number][5], ],
         'canvas4k': ['                 "1" - новая игра                     ', color[number][4], color[number][5], ],
         'canvas4l': ['                 "2" - продолжить                     ', color[number][4], color[number][5], ],
         'canvas4m': ['                 "3" - выйти                          ', color[number][4], color[number][5], ],
         'canvas4t': ['                                              (c)rypy ', Fore.BLUE, color[number][5], ], }

    pictures = [draw_skull]

    return pictures[number]



