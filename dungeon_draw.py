from dungeon_rooms import draw_game, draw_skull, draw_start_menu
from colorama import init, Fore, Back, Style
import random
import os

cls = lambda: os.system('cls')

colors = (Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE)
colors_no_black = (Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE)
colors_back = (Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE)
colors_style = (Style.DIM, Style.NORMAL, Style.BRIGHT)


class Draw:

    def __init__(self, frame, color_frame, picture, text, color_picture, color_text):
        """инициализация того что хотим нарисовать"""
        self.frame = frame
        self.color_frame = color_frame
        self.picture = picture
        self.text = text
        self.color_picture = color_picture
        self.color_text = color_text

    def window_size(self):
        """задает размер окна"""
        os.system(f"mode con cols={len(draw_game[0])+1} lines={len(draw_game) - len(self.picture) * 3 + 10}")

    def draw(self):
        """метод отрисовки картинок и текста"""
        picture_srt = tuple(i for i in range(2, len(self.frame)-3, 4))
        text_str = tuple(i for i in range(3, len(self.frame)-2, 4))

        for n in range(len(self.frame) - 2 - len(self.picture) * 3):
            self.frame[picture_srt[n]] = self.picture[n]
            self.frame[text_str[n]] = self.text[n]

        for i in self.frame:
            if self.frame.index(i) in picture_srt:
                print(self.color_picture + Back.BLACK + i, end='')
            elif self.frame.index(i) in text_str:
                print(self.color_text + Back.BLACK + i, end='')
            else:
                print(self.color_frame + Back.BLACK + i, end='')


if __name__ == '__main__':
    # init()
    random_color1 = random.choice(colors_no_black)
    random_color2 = random.choice(colors_no_black)
    draw = Draw(draw_game, Fore.LIGHTCYAN_EX, draw_skull, draw_start_menu, random_color1, random_color2)
    draw.window_size()
    draw.draw()
