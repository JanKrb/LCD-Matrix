from src.wrapper.sh1106 import SH1106, Screen
from PIL import Image,ImageDraw,ImageFont
import time
import os

font_path = os.path.join('assets', 'Font.ttf')

def main():
    disp = SH1106()

    disp.Init()
    disp.clear()

    start_image = Image.new('1', (disp.width, disp.height), "WHITE")
    draw = ImageDraw.Draw(start_image)
    font = ImageFont.truetype(font_path, 20)

    draw.line([(0,0),(Screen.width - 1, 0)], fill = 0)
    draw.line([(0,0),(0,Screen.height - 1)], fill = 0)
    draw.line([(0,Screen.height - 1),(Screen.width - 1,Screen.height - 1)], fill = 0)
    draw.line([(Screen.width - 1,0),(Screen.width - 1,Screen.height - 1)], fill = 0)

    draw.text((5,5), 'Niclas Heide', font = font, fill = 0)
    draw.text((5,25), 'Jan Ruhfus ', font = font, fill = 0)

    disp.ShowImage(disp.getbuffer(start_image))

if __name__ == '__main__':
    main()