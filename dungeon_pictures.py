from colorama import init, Fore, Back, Style
from dungeon_draw import colors_no_black
import random

random_color1 = random.choice(colors_no_black)
random_color2 = random.choice(colors_no_black)

"""picture_colors = ['frame_color', 'frame_back', 'canvas1_color', 'canvas1_back', 'canvas2_color', 'canvas2_back']"""

picture_colors = [Fore.LIGHTCYAN_EX, Back.BLACK, random_color1, Back.BLACK, random_color2, Back.BLACK]

draw_skull = \
  {'canvas2a': ['════════════════════════════════════════════', picture_colors[0], picture_colors[1], ],
   'canvas2c': ['              uu$$$$$$$$$$uu                ', picture_colors[2], picture_colors[3], ],
   'canvas2d': ['          uu$$$$$$$$$$$$$$$$$uu             ', picture_colors[2], picture_colors[3], ],
   'canvas2e': ['         u$$$$$$$$$$$$$$$$$$$$$u            ', picture_colors[2], picture_colors[3], ],
   'canvas2f': ['        u$$$$$$$$$$$$$$$$$$$$$$$u           ', picture_colors[2], picture_colors[3], ],
   'canvas2g': ['       u$$$$$$$$$$$$$$$$$$$$$$$$$u          ', picture_colors[2], picture_colors[3], ],
   'canvas2h': ['       u$$$$$$$$$$$$$$$$$$$$$$$$$u          ', picture_colors[2], picture_colors[3], ],
   'canvas2i': ['       u$$$$$$     $$$     $$$$$$u          ', picture_colors[2], picture_colors[3], ],
   'canvas2k': ['        $$$$        u$u      $$$$u          ', picture_colors[2], picture_colors[3], ],
   'canvas2l': ['        $$$u        u$u       u$$$          ', picture_colors[2], picture_colors[3], ],
   'canvas2m': ['         $$$u       u$$$u     u$$$          ', picture_colors[2], picture_colors[3], ],
   'canvas2n': ['         $$$$uu$$$uu_   _$$$uu$$$$          ', picture_colors[2], picture_colors[3], ],
   'canvas2o': ['          $$$$$$$         $$$$$$$           ', picture_colors[2], picture_colors[3], ],
   'canvas2p': ['             u$$$$$$$u$$$$$$$u              ', picture_colors[2], picture_colors[3], ],
   'canvas2q': ['              u$##$$ $ $ $u$$u              ', picture_colors[2], picture_colors[3], ],
   'canvas2r': ['    uuu       $$u$_$  $ $ $u$$        uuu   ', picture_colors[2], picture_colors[3], ],
   'canvas2s': ['   u$$$$        $$$$$ u$u$u$$$       u$$$$  ', picture_colors[2], picture_colors[3], ],
   'canvas2t': ['  $$$$$uu        $$$ $$$$$$       uu$$$$$$  ', picture_colors[2], picture_colors[3], ],
   'canvas2v': ['════════════════════════════════════════════', picture_colors[0], picture_colors[1], ],
   'canvas4f': ['           Добро пожаловать в подземелье              ', picture_colors[4], picture_colors[5], ],
   'canvas4k': ['                 "1" - новая игра                     ', picture_colors[4], picture_colors[5], ],
   'canvas4l': ['                 "2" - продолжить                     ', picture_colors[4], picture_colors[5], ],
   'canvas4m': ['                 "3" - выйти                          ', picture_colors[4], picture_colors[5], ],
   'canvas4t': ['                                              (c)rypy ', Fore.BLUE, picture_colors[5], ],
   'canvas4v': ['══════════════════════════════════════════════════════', picture_colors[0], picture_colors[1], ], }


