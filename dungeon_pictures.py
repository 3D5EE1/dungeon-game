from colorama import init, Fore, Back, Style
from dungeon_draw import colors_no_black, colors_ligth_no_back
import random

random_color0 = random.choice(colors_no_black)
random_color1 = random.choice(colors_ligth_no_back)
random_color2 = random.choice(colors_ligth_no_back)
random_color3 = random.choice(colors_ligth_no_back)
random_color4 = random.choice(colors_ligth_no_back)


def pictures(number):
    """('picture_name', 'frame_color', 'frame_back', 'canvas1_color', 'canvas1_back', 'canvas2_color', 'canvas2_back',
    elements_style)"""

    color = [
        ('skull', Fore.LIGHTCYAN_EX, Back.BLACK, random_color1, Back.BLACK, random_color2, Back.BLACK, '', ),
        ('cross', random_color0, Back.BLACK, random_color1, Back.BLACK, random_color2, Back.BLACK, '', ),
        ('text1', Fore.LIGHTCYAN_EX, Back.BLACK, random_color1, Back.BLACK, random_color2, Back.BLACK, '', '', ),
        ('add_4_canvas', Fore.LIGHTCYAN_EX, Back.BLACK, random_color1, Back.BLACK, random_color2, Back.BLACK, '', ),
        ('name_hero', Fore.LIGHTCYAN_EX, Back.BLACK, random_color3, Back.BLACK, random_color4, Back.BLACK, '', ),
        ('del_5', '', '', '', '', '', '', '', ),
        ('del_center_frame', '', '', '', '', '', '', '',),
        ('check_name', Fore.LIGHTCYAN_EX, Back.BLACK, random_color1, Back.BLACK, random_color2, Back.BLACK, '', ),
        ('name_approved', random_color0, Back.BLACK, random_color1, Back.BLACK, random_color2, Back.BLACK, '',),
        ('canvas_three', Fore.LIGHTCYAN_EX, Back.BLACK, random_color1, Back.BLACK, random_color2, Back.BLACK, '',),
        ('menu_continue', Fore.LIGHTCYAN_EX, Back.BLACK, random_color1, Back.BLACK, random_color2, Back.BLACK, '',),
        ('param_character1', random_color0, Back.BLACK, random_color1, Back.BLACK, random_color2, Back.BLACK, '',),
        ('param_character2', random_color0, Back.BLACK, random_color1, Back.BLACK, random_color2, Back.BLACK, '',),
    ]

    skull = {
        'canvas2a': ['════════════════════════════════════════════', color[number][1], color[number][2], '', ],
        'canvas2c': ['              uu$$$$$$$$$$uu                ', color[number][3], color[number][4], '', ],
        'canvas2d': ['          uu$$$$$$$$$$$$$$$$$uu             ', color[number][3], color[number][4], '', ],
        'canvas2e': ['         u$$$$$$$$$$$$$$$$$$$$$u            ', color[number][3], color[number][4], '', ],
        'canvas2f': ['        u$$$$$$$$$$$$$$$$$$$$$$$u           ', color[number][3], color[number][4], '', ],
        'canvas2g': ['       u$$$$$$$$$$$$$$$$$$$$$$$$$u          ', color[number][3], color[number][4], '', ],
        'canvas2h': ['       u$$$$$$$$$$$$$$$$$$$$$$$$$u          ', color[number][3], color[number][4], '', ],
        'canvas2i': ['       u$$$$$$     $$$     $$$$$$u          ', color[number][3], color[number][4], '', ],
        'canvas2k': ['        $$$$        u$u      $$$$u          ', color[number][3], color[number][4], '', ],
        'canvas2l': ['        $$$u        u$u       u$$$          ', color[number][3], color[number][4], '', ],
        'canvas2m': ['         $$$u       u$$$u     u$$$          ', color[number][3], color[number][4], '', ],
        'canvas2n': ['         $$$$uu$$$uu_   _$$$uu$$$$          ', color[number][3], color[number][4], '', ],
        'canvas2o': ['          $$$$$$$         $$$$$$$           ', color[number][3], color[number][4], '', ],
        'canvas2p': ['             u$$$$$$$u$$$$$$$u              ', color[number][3], color[number][4], '', ],
        'canvas2q': ['              u$##$$ $ $ $u$$u              ', color[number][3], color[number][4], '', ],
        'canvas2r': ['    uuu       $$u$_$  $ $ $u$$        uuu   ', color[number][3], color[number][4], '', ],
        'canvas2s': ['   u$$$$        $$$$$ u$u$u$$$       u$$$$  ', color[number][3], color[number][4], '', ],
        'canvas2t': ['  $$$$$uu        $$$ $$$$$$       uu$$$$$$  ', color[number][3], color[number][4], '', ],
    }

    cross = {
        'canvas2a': ['════════════════════════════════════════════', color[number][1], color[number][2], '', ],
        'canvas2c': ['                       ######               ', color[number][3], color[number][4], '', ],
        'canvas2d': ['                      ######                ', color[number][3], color[number][4], '', ],
        'canvas2e': ['                      ######                ', color[number][3], color[number][4], '', ],
        'canvas2f': ['                     ######                 ', color[number][3], color[number][4], '', ],
        'canvas2g': ['           #########################        ', color[number][3], color[number][4], '', ],
        'canvas2h': ['          ##########################        ', color[number][3], color[number][4], '', ],
        'canvas2i': ['         ##########################         ', color[number][3], color[number][4], '', ],
        'canvas2k': ['                   ######                   ', color[number][3], color[number][4], '', ],
        'canvas2l': ['                   ######                   ', color[number][3], color[number][4], '', ],
        'canvas2m': ['                  ######                    ', color[number][3], color[number][4], '', ],
        'canvas2n': ['                  ######                    ', color[number][3], color[number][4], '', ],
        'canvas2o': ['                 ######                     ', color[number][3], color[number][4], '', ],
        'canvas2p': ['                 ######                     ', color[number][3], color[number][4], '', ],
        'canvas2q': ['                ######                      ', color[number][3], color[number][4], '', ],
        'canvas2r': ['            ,,&&&&&&&&&&,,                  ', color[number][3], color[number][4], '', ],
        'canvas2s': ['        ,,@@@@@@@@@@@@@@@@@,,               ', color[number][3], color[number][4], '', ],
        'canvas2t': ['  ,,,,@@@@@@@@@@@@@@@@@@@@@@@@@@@@,,        ', color[number][3], color[number][4], '', ],
    }

    text1 = {
        'canvas4f': ['           Добро пожаловать в подземелье              ', color[number][5], color[number][6], ''],
        'canvas4k': ['                 "1" - новая игра                     ', color[number][5], color[number][6], ''],
        'canvas4l': ['                 "2" - продолжить                     ', color[number][5], color[number][6], ''],
        'canvas4m': ['                 "3" - выйти                          ', color[number][5], color[number][6], ''],
        'canvas4t': ['                                              (c)rypy ', Fore.BLUE, color[number][6], '', ],
    }

    add_4_canvas = {
        'frame1v': ['║', color[number][3], color[number][4], '', ],
        'canvas1v': ['', color[number][3], color[number][4], '', ],
        'canvas2v': ['                                            ', color[number][3], color[number][4], '', ],
        'canvas3v': ['', color[number][3], color[number][4], '', ],
        'frame2v': [' ', color[number][3], color[number][4], '', ],
        'canvas4v': ['                                                      ', color[number][3], color[number][4], ''],
        'frame3v': ['║\n', color[number][3], color[number][4], '', ],
        'frame1w': ['║', color[number][3], color[number][4], '', ],
        'canvas1w': ['', color[number][3], color[number][4], '', ],
        'canvas2w': ['                                            ', color[number][3], color[number][4], '', ],
        'canvas3w': ['', color[number][3], color[number][4], '', ],
        'frame2w': [' ', color[number][3], color[number][4], '', ],
        'canvas4w': ['                                                      ', color[number][3], color[number][4], ''],
        'frame3w': ['║\n', color[number][1], color[number][2], '', ],
        'frame1x': ['║', color[number][1], color[number][2], '', ],
        'canvas1x': ['', color[number][3], color[number][4], '', ],
        'canvas2x': ['                                            ', color[number][3], color[number][4], '', ],
        'canvas3x': ['', color[number][3], color[number][4], '', ],
        'frame2x': [' ', color[number][3], color[number][4], '', ],
        'canvas4x': ['                                                      ', color[number][3], color[number][4], ''],
        'frame3x': ['║\n', color[number][1], color[number][2], '', ],
        'frame1y': ['║', color[number][1], color[number][2], '', ],
        'canvas1y': ['', color[number][3], color[number][4], '', ],
        'canvas2y': ['                                            ', color[number][3], color[number][4], '', ],
        'canvas3y': ['', color[number][3], color[number][4], '', ],
        'frame2y': [' ', color[number][3], color[number][4], '', ],
        'canvas4y': ['                                                      ', color[number][3], color[number][4], ''],
        'frame3y': ['║\n', color[number][1], color[number][2], '', ],
        'frame1z': ['╚', color[number][1], color[number][2], '', ],
        'canvas1z': ['', color[number][3], color[number][4], '', ],
        'canvas2z': ['════════════════════════════════════════════', color[number][1], color[number][2], '', ],
        'canvas3z': ['', color[number][3], color[number][4], '', ],
        'frame2z': ['═', color[number][1], color[number][2], '', ],
        'canvas4z': ['══════════════════════════════════════════════════════', color[number][1], color[number][2], ''],
        'frame3z': ['╝\n', color[number][1], color[number][2], '', ],
    }

    name_hero = {
        'canvas2a': ['══════════════════════════════════════════════════', color[number][3], color[number][4], '', ],
        'canvas2b': ['                                                  ', color[number][3], color[number][4], '', ],
        'canvas2c': ['          Ведите имя своего персонажа!!!          ', color[number][5], color[number][6], '', ],
        'canvas2d': ['                                                  ', color[number][3], color[number][4], '', ],
        'canvas2e': ['══════════════════════════════════════════════════', '', '', '', ],
        'frame1e': ['╚', '', '', '', ],
        'frame2e': ['═', '', '', '', ],
        'frame3e': ['╝\n', '', '', '', ],
    }

    del_5 = {
        'canvas4a': [], 'canvas4b': [], 'canvas4c': [], 'canvas4d': [], 'canvas4e': [],
    }

    del_center_frame = {
        'frame2a': ['', '', '', '', ], 'frame2b': ['', '', '', '', ], 'frame2c': ['', '', '', '', ],
        'frame2d': ['', '', '', '', ], 'frame2e': ['', '', '', '', ], 'frame2f': ['', '', '', '', ],
        'frame2g': ['', '', '', '', ], 'frame2h': ['', '', '', '', ], 'frame2i': ['', '', '', '', ],
        'frame2k': ['', '', '', '', ], 'frame2l': ['', '', '', '', ], 'frame2m': ['', '', '', '', ],
        'frame2n': ['', '', '', '', ], 'frame2o': ['', '', '', '', ], 'frame2p': ['', '', '', '', ],
        'frame2q': ['', '', '', '', ], 'frame2r': ['', '', '', '', ], 'frame2s': ['', '', '', '', ],
        'frame2t': ['', '', '', '', ], 'frame2v': ['', '', '', '', ],
    }

    check_name = {
        'canvas2a': ['═══════════════════════', color[number][1], color[number][2], '', ],
        'canvas2b': ['                       ', color[number][3], color[number][4], '', ],
        'canvas2c': [' Имя вашего персонажа: ', color[number][3], color[number][4], '', ],
        'canvas2d': ['                       ', color[number][3], color[number][4], '', ],
        'canvas2e': [' все верно? выберите "1', color[number][3], color[number][4], '', ],
        'canvas2f': ['                       ', color[number][3], color[number][4], '', ],
        'canvas2g': ['     "3" - для возарата', color[number][3], color[number][4], '', ],
        'canvas2h': ['                       ', color[number][3], color[number][4], '', ],
        'canvas2i': ['═══════════════════════', '', '', '', ],
        'canvas4a': ['═════════════════════', '', '', '', ],
        'canvas4b': ['                     ', color[number][3], color[number][4], '', ],
        'canvas4c': ['                     ', color[number][5], color[number][6], '', ],
        'canvas4d': ['                     ', color[number][3], color[number][4], '', ],
        'canvas4e': ['" - да или "2" - нет ', color[number][3], color[number][4], '', ],
        'canvas4f': ['                     ', color[number][3], color[number][4], '', ],
        'canvas4g': [' в главное меню      ', color[number][3], color[number][4], '', ],
        'canvas4h': ['                     ', color[number][3], color[number][4], '', ],
        'canvas4i': ['═════════════════════', '', '', '', ],
        'frame1i': ['╚', '', '', '', ],
        'frame2i': ['═', '', '', '', ],
        'frame3i': ['╝\n', '', '', '', ],
    }

    name_approved = {
        'canvas2a': ['═════════════════════════════', color[number][1], color[number][2], '', ],
        'canvas2b': ['                             ', color[number][1], color[number][2], '', ],
        'canvas2c': ['  уже есть персонаж с именем:', color[number][3], color[number][4], '', ],
        'canvas2d': ['                             ', color[number][1], color[number][2], '', ],
        'canvas2e': ['═════════════════════════════', '', '', '', ],
        'canvas4a': ['═════════════════════', color[number][1], color[number][2], '', ],
        'canvas4b': ['                     ', color[number][1], color[number][2], '', ],
        'canvas4c': ['                     ', color[number][5], color[number][6], '', ],
        'canvas4d': ['                     ', color[number][1], color[number][2], '', ],
        'canvas4e': ['═════════════════════', '', '', '', ],
        'frame1e': ['╚', '', '', '', ],
        'frame2e': ['═', '', '', '', ],
        'frame3e': ['╝\n', '', '', '', ],
    }

    canvas_three = {
        'canvas1a': ['════════════════════', color[number][3], color[number][4], '', ],
        'canvas1b': ['                    ', color[number][3], color[number][4], '', ],
        'canvas1c': ['                    ', color[number][3], color[number][4], '', ],
        'canvas1d': ['                    ', color[number][3], color[number][4], '', ],
        'canvas1e': ['                    ', color[number][3], color[number][4], '', ],
        'canvas1f': ['                    ', color[number][3], color[number][4], '', ],
        'canvas1g': ['                    ', color[number][3], color[number][4], '', ],
        'canvas1h': ['                    ', color[number][3], color[number][4], '', ],
        'canvas1i': ['                    ', color[number][3], color[number][4], '', ],
        'canvas1k': ['════════════════════', color[number][3], color[number][4], '', ],
        'canvas2a': ['╦', color[number][3], color[number][4], '', ],
        'canvas2b': ['║', color[number][3], color[number][4], '', ],
        'canvas2c': ['║', color[number][3], color[number][4], '', ],
        'canvas2d': ['║', color[number][3], color[number][4], '', ],
        'canvas2e': ['║', color[number][3], color[number][4], '', ],
        'canvas2f': ['║', color[number][3], color[number][4], '', ],
        'canvas2g': ['║', color[number][3], color[number][4], '', ],
        'canvas2h': ['║', color[number][3], color[number][4], '', ],
        'canvas2i': ['║', color[number][3], color[number][4], '', ],
        'canvas2k': ['╩', color[number][3], color[number][4], '', ],
        'canvas3a': ['════════════════════', color[number][3], color[number][4], '', ],
        'canvas3b': ['                    ', color[number][3], color[number][4], '', ],
        'canvas3c': ['                    ', color[number][3], color[number][4], '', ],
        'canvas3d': ['                    ', color[number][3], color[number][4], '', ],
        'canvas3e': ['                    ', color[number][3], color[number][4], '', ],
        'canvas3f': ['                    ', color[number][3], color[number][4], '', ],
        'canvas3g': ['                    ', color[number][3], color[number][4], '', ],
        'canvas3h': ['                    ', color[number][3], color[number][4], '', ],
        'canvas3i': ['                    ', color[number][3], color[number][4], '', ],
        'canvas3k': ['════════════════════', color[number][3], color[number][4], '', ],
        'canvas4a': ['════════════════════', color[number][3], color[number][4], '', ],
        'canvas4b': ['                    ', color[number][3], color[number][4], '', ],
        'canvas4c': ['                    ', color[number][3], color[number][4], '', ],
        'canvas4d': ['                    ', color[number][3], color[number][4], '', ],
        'canvas4e': ['                    ', color[number][3], color[number][4], '', ],
        'canvas4f': ['                    ', color[number][3], color[number][4], '', ],
        'canvas4g': ['                    ', color[number][3], color[number][4], '', ],
        'canvas4h': ['                    ', color[number][3], color[number][4], '', ],
        'canvas4i': ['                    ', color[number][3], color[number][4], '', ],
        'canvas4k': ['════════════════════', color[number][3], color[number][4], '', ],
        'frame2a': ['╦', color[number][1], color[number][2], '', ],
        'frame2b': ['║', color[number][1], color[number][2], '', ],
        'frame2c': ['║', color[number][1], color[number][2], '', ],
        'frame2d': ['║', color[number][1], color[number][2], '', ],
        'frame2e': ['║', color[number][1], color[number][2], '', ],
        'frame2f': ['║', color[number][1], color[number][2], '', ],
        'frame2g': ['║', color[number][1], color[number][2], '', ],
        'frame2h': ['║', color[number][1], color[number][2], '', ],
        'frame2i': ['║', color[number][1], color[number][2], '', ],
        'frame2k': ['╩', color[number][1], color[number][2], '', ],
        'frame3a': ['╗\n', color[number][1], color[number][2], '', ],
        'frame3k': ['╝\n', color[number][1], color[number][2], '', ],
        'frame1a': ['╔', color[number][1], color[number][2], '', ],
        'frame1k': ['╚', color[number][1], color[number][2], '', ],
    }

    menu_continue = {
        'canvas2c': [' "1" - новое имя   "2" - вернуться в главное меню ', color[number][5], color[number][6], '', ],
    }

    param_character1 = {
        'canvas2a': ['══════════════', color[number][1], color[number][2], '', ],
        'canvas2b': ['              ', color[number][3], color[number][4], '', ],
        'canvas2c': ['     персонаж:', color[number][3], color[number][4], '', ],
        'canvas2d': ['              ', color[number][3], color[number][4], '', ],
        'canvas2e': ['          пол:', color[number][3], color[number][4], '', ],
        'canvas2f': ['        расса:', color[number][3], color[number][4], '', ],
        'canvas2g': ['        класс:', color[number][3], color[number][4], '', ],
        'canvas2h': ['      возраст:', color[number][3], color[number][4], '', ],
        'canvas2i': ['       оружие:', color[number][3], color[number][4], '', ],
        'canvas2k': ['      здровье:', color[number][3], color[number][4], '', ],
        'canvas2l': ['        броня:', color[number][3], color[number][4], '', ],
        'canvas2m': ['         сила:', color[number][3], color[number][4], '', ],
        'canvas2n': [' выносливасть:', color[number][3], color[number][4], '', ],
        'canvas2o': ['        манна:', color[number][3], color[number][4], '', ],
        'canvas2p': ['        ульта:', color[number][3], color[number][4], '', ],
        'canvas2q': ['              ', color[number][3], color[number][4], '', ],
        'canvas2r': ['══════════════', color[number][1], color[number][2], '', ],
        'canvas4a': ['════════════════════════════════════════', color[number][1], color[number][2], '', ],
        'canvas4b': ['                                        ', color[number][3], color[number][4], '', ],
        'canvas4c': ['                                        ', color[number][3], color[number][4], '', ],
        'canvas4d': ['                                        ', color[number][3], color[number][4], '', ],
        'canvas4p': ['                                        ', color[number][3], color[number][4], '', ],
        'canvas4q': ['                                        ', color[number][3], color[number][4], '', ],
        'canvas4r': ['════════════════════════════════════════', color[number][1], color[number][2], '', ],
        'frame1r': ['╚', '', '', '', ],
        'frame2r': ['═', '', '', '', ],
        'frame3r': ['╝\n', '', '', '', ],

    }

    param_character2 = {
        'canvas4e': ['                                        ', color[number][5], color[number][6], '', ],
        'canvas4f': ['                                        ', color[number][5], color[number][6], '', ],
        'canvas4g': ['                                        ', color[number][5], color[number][6], '', ],
        'canvas4h': ['                                        ', color[number][5], color[number][6], '', ],
        'canvas4i': ['                                        ', color[number][5], color[number][6], '', ],
        'canvas4k': ['                                        ', color[number][5], color[number][6], '', ],
        'canvas4l': ['                                        ', color[number][5], color[number][6], '', ],
        'canvas4m': ['                                        ', color[number][5], color[number][6], '', ],
        'canvas4n': ['                                        ', color[number][5], color[number][6], '', ],
        'canvas4o': ['                                        ', color[number][5], color[number][6], '', ],
        'canvas4p': ['                                        ', color[number][5], color[number][6], '', ],
    }

    picture = {
        0: skull,
        1: cross,
        2: text1,
        3: add_4_canvas,
        4: name_hero,
        5: del_5,
        6: del_center_frame,
        7: check_name,
        8: name_approved,
        9: canvas_three,
        10: menu_continue,
        11: param_character1,
        12: param_character2,
    }

    return picture[number]



