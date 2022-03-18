from src.modules.module import Module as TemplateModule
from PIL import Image, ImageDraw, ImageFont
import os
import json

font_path = os.path.join('assets', 'Font.ttf')

class Module(TemplateModule):
    def __init__(self, display):
        super().__init__(display)
        
        self.display = display
        
        self.txt_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"sensor_data.txt")
        
        self.temperature = "0C"
        self.font = ImageFont.truetype(font_path, 20)
        
        self.start_image = Image.new('1', (display.width, display.height), "WHITE")
        self.draw_object = ImageDraw.Draw(self.start_image)

    
    def get_data(self):
        f = open("sensor_data.txt","r")
        data = json.loads(f.read())
        print(data)
        #with open(self.txt_path,"r") as f:
            #return f.read()
     
    def draw(self):
        self.start_image = Image.new('1', (self.display.width, self.display.height), "WHITE")
        self.draw_object = ImageDraw.Draw(self.start_image)
        self.display.clear()

        self.draw_object.text((5, 5), self.temperature, font=self.font, fill=0)

        return self.start_image
    
    def update(self):
        super().update()
        self.get_data()
    
