from src.wrapper.sh1106 import SH1106, SPI
from src.menu.start_menu import StartMenu
import RPi.GPIO as GPIO

def main():
    disp = SH1106()

    disp.Init()
    disp.clear()
    
    start_screen = StartMenu()
    disp.show_image(disp.get_buffer(start_screen.start_image))

    try:
        while True: pass
    except KeyboardInterrupt:
        disp.reset()
        SPI.module_exit()
        GPIO.cleanup()


if __name__ == '__main__':
    main()
