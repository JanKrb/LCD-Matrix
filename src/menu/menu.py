from src.wrapper.sh1106 import Screen
from src.modules.clock_module import Module as ClockModule
from src.modules.temperature_module import Module as TemperatureModule
from PIL import Image, ImageDraw, ImageFont
import os

font_path = os.path.join('assets', 'Font.ttf')

class MenuItem:
    def __init__(self, title, module):
        self.title = title
        self.module = module

class Settings: 
    menu_items = [
        MenuItem('Uhrzeit', ClockModule),
        MenuItem('Temperatur', TemperatureModule)
    ]

    items_on_display = 2

class Menu:
    def __init__(self, display):
        self.display = display
        self.font = ImageFont.truetype(font_path, 20)
        self.current_scroll_index = 0

        self.start_image = Image.new('1', (display.width, display.height), "WHITE")
        self.draw = ImageDraw.Draw(self.start_image)

        self.shown_menu = Settings.menu_items[self.current_scroll_index : (Settings.items_on_display + self.current_scroll_index)]
        # TODO: Scrollable Menu

    def draw_menu(self):
        for index, item in self.shown_menu:
            self.draw.text((5, 5 * (index + 1)), item.title, font=self.font, fill=0)

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