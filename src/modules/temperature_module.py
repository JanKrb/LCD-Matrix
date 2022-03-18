from src.modules.module import Module as TemplateModule
import os
import json

class Module(TemplateModule):
    def __init__(self, display):
        super().__init__(display)
        self.txt_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"sensor_data.txt")
    
    def get_data(self):
        f = open(self.txt_path,"r")
        data = json.loads(f.read())
        print(data)
        #with open(self.txt_path,"r") as f:
            #return f.read()
     
    def draw(self):
        pass
    
    def update(self):
        self.get_data()
    
