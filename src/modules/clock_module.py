from src.modules.module import Module as TemplateModule
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import os

font_path = os.path.join('assets', 'Font.ttf')

class Module(TemplateModule):
    def __init__(self, display):
        super().__init__(display)

        self.time = "00:00:00"
        self.font = ImageFont.truetype(font_path, 20)

        self.start_image = Image.new(self.time, (display.width, display.height), "WHITE")
        self.draw = ImageDraw.Draw(self.start_image)

    def draw(self):
        self.draw.text((5, 5), self.time, font=self.font, fill=0)

        return self.draw

    def update(self):
        super().update()

        now = datetime.now()
        self.time = now.strftime("%H:%M:%S")