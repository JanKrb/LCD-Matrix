from PIL import Image, ImageDraw

class Module:
    def __init__(self, display) -> None:
        self.image = Image.new('1', (display.width, display.height), "WHITE")
        self.draw_image = ImageDraw.Draw(self.image)
    
    def draw(self):
        pass
    
    def update(self):
        pass