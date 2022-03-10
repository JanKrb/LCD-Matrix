from src.modules.module import Module as TemplateModule

class Module(TemplateModule):
    def __init__(self):
        super().__init__()
    
    def draw(self):
        super().draw()

    def update(self):
        super().update()
        print("test")