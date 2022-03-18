from src.modules.module import Module as TemplateModule
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import os
import time

font_path = os.path.join('assets', 'Font.ttf')

class Module(TemplateModule):
    def __init__(self, display):
        super().__init__(display)

        self.time = "00:00:00"
        self.font = ImageFont.truetype(font_path, 20)

        self.start_image = Image.new('1', (display.width, display.height), "WHITE")
        self.draw_object = ImageDraw.Draw(self.start_image)

    def draw(self):
        self.draw_object.text((5, 5), self.time, font=self.font, fill=0)

        return self.draw_object

    def update(self):
        super().update()

        now = datetime.now()
        self.time = now.strftime("%H:%M:%S")
        
        time.sleep(1)