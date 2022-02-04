from src.wrapper.sh1106 import Screen
from PIL import Image, ImageDraw, ImageFont
import os

font_path = os.path.join('assets', 'Font.ttf')

class Menu:
    def __init__(self, display):
        self.font = ImageFont.truetype(font_path, 20)

        self.start_image = Image.new('1', (display.width, display.height), "WHITE")
        self.draw = ImageDraw.Draw(self.start_image)

        # TODO: Menu
        # TODO: Scrollable Menu

    def menu_up(self):
        pass

    def menu_down(self):
        pass

    def menu_option1(self):
        pass
    
    def menu_option2(self):
        pass

    def menu_option3(self):
        pass