from src.wrapper.sh1106 import SH1106, SPI
from src.menu.start_menu import StartMenu
from src.menu.menu import Menu
from src.wrapper.joystick import Joystick, Keymap as JSKM
from src.wrapper.buttons import Buttons, Keymap as BKM
import RPi.GPIO as GPIO
import time

def main():
    GPIO.setmode(GPIO.BCM)
    disp = SH1106()

    disp.Init()
    disp.clear()
    
    start_screen = StartMenu(disp)
    disp.show_image(disp.get_buffer(start_screen.start_image))

    time.sleep(2)

    menu = Menu(disp)
    disp.clear()

    # Setup Buttons & Joystick
    menu_controller_joystick = Joystick(JSKM.UP, JSKM.DOWN, JSKM.LEFT, JSKM.RIGHT, JSKM.PRESS)
    menu_controller_buttons = Buttons(BKM.KEY1, BKM.KEY2, BKM.KEY3)


    # Setup button events for menu
    menu_controller_joystick.event_up = menu.menu_up
    menu_controller_joystick.event_down = menu.menu_down
    menu_controller_joystick._setup_events()

    menu_controller_buttons.event_key1 = menu.menu_option1
    menu_controller_buttons.event_key2 = menu.menu_option2
    menu_controller_buttons.event_key3 = menu.menu_option3
    menu_controller_buttons._setup_events()

    try:
        while True:
            print(menu.module)

            if menu.module == None:
                disp.show_image(disp.get_buffer(menu.start_image))
            else:
                menu.module.update()
                disp.show_image(disp.get_buffer(menu.module.draw()))
    except KeyboardInterrupt:
        disp.reset()
        SPI.module_exit()
        GPIO.cleanup()


if __name__ == '__main__':
    main()
