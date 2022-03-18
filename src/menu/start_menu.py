from src.wrapper.sh1106 import Screen
from PIL import Image, ImageDraw, ImageFont
import os

font_path = os.path.join('assets', 'Font.ttf')

class StartMenu:
    def __init__(self, display):
        self.font = ImageFont.truetype(font_path, 20)

        self.start_image = Image.new('1', (display.width, display.height), "WHITE")
        self.draw = ImageDraw.Draw(self.start_image)

        self._draw_display_outline()
        self._draw_name_tags()
    
    def _draw_display_outline(self):
        self.draw.line([(0, 0), (Screen.width - 1, 0)], fill=0)  # Top
        self.draw.line([(0, 0), (0, Screen.height - 1)], fill=0)  # Left
        self.draw.line([(0, Screen.height - 1), (Screen.width - 1, Screen.height - 1)], fill=0)  # Bottom
        self.draw.line([(Screen.width - 1, 0), (Screen.width - 1, Screen.height - 1)], fill=0)  # Right

    def _draw_name_tags(self):
        self.draw.text((5, 5), 'Niclas Heide', font=self.font, fill=0)
        self.draw.text((5, 25), 'Jan Ruhfus ', font=self.font, fill=0)