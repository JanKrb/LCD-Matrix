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
        MenuItem('Temp.', TemperatureModule),
        MenuItem('Uxhrzeit', ClockModule),
        MenuItem('Texmp.', TemperatureModule),
    ]

    items_on_display = 2
    items_margin = 25

class Menu:
    def __init__(self, display):
        self.display = display
        self.font = ImageFont.truetype(font_path, 20)
        self.current_scroll_index = 0

        self.start_image = Image.new('1', (display.width, display.height), "WHITE")
        self.draw = ImageDraw.Draw(self.start_image)

        self.shown_menu = Settings.menu_items[self.current_scroll_index : (Settings.items_on_display + self.current_scroll_index)]
        self.draw_menu()

    def draw_menu(self):
        for index, item in enumerate(self.shown_menu):
            self.draw.text((5, Settings.items_margin * index + 5), f"{index + 1} {item.title}", font=self.font, fill=0)

    def rerender_display(self):
        self.draw = ImageDraw.Draw(self.start_image)
        self.draw_menu()

    def menu_up(self, channel):
        print(self.current_scroll_index)
        self.current_scroll_index = min(self.current_scroll_index + 1, len(Settings.menu_items) - 1)
        print(self.current_scroll_index)
        self.rerender_display()

    def menu_down(self, channel):
        print(self.current_scroll_index)
        self.current_scroll_index = max(0, self.current_scroll_index - 1)
        print(self.current_scroll_index)
        self.rerender_display()

    def menu_option1(self, channel):
        pass
    
    def menu_option2(self, channel):
        pass

    def menu_option3(self, channel):
        pass