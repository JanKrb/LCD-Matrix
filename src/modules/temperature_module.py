from src.modules.module import Module as TemplateModule
from PIL import Image, ImageDraw, ImageFont
import os
import json

font_path = os.path.join('assets', 'Font.ttf')

class Module(TemplateModule):
    def __init__(self, display):
        super().__init__(display)
        
        self.display = display
        
        self.font = ImageFont.truetype(font_path, 20)
        
        self.start_image = Image.new('1', (display.width, display.height), "WHITE")
        self.draw_object = ImageDraw.Draw(self.start_image)

    
    def get_data(self):
        f = open("sensor_data.txt","r")
        data = json.loads(f.read())
        return data["temperature"], data["humidity"]
     
    def draw(self):
        temperature, humidity = self.get_data()
        self.start_image = Image.new('1', (self.display.width, self.display.height), "WHITE")
        self.draw_object = ImageDraw.Draw(self.start_image)
        self.display.clear()

        self.draw_object.text((5, 5), str(temperature), font=self.font, fill=0)
        self.draw_object.text((5, 30), str(humidity), font=self.font, fill=0)

        return self.start_image
    
    def update(self):
        super().update()
        self.get_data()
    
