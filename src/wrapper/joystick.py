import RPi.GPIO as GPIO

class Keymap:
    """BCM keymap for joystick buttons"""
    UP = 6
    DOWN = 19
    LEFT = 5
    RIGHT = 26
    PRESS = 13

class Joystick:
    def __init__(self, up, down, left, right, click):
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.click = click

        GPIO.setup(GPIO.BCM)

        GPIO.setup(self.up,    GPIO.IN,    pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.down,  GPIO.IN,    pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.left,  GPIO.IN,    pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.right, GPIO.IN,    pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.click, GPIO.IN,    pull_up_down=GPIO.PUD_UP)

    def is_pressed_up(self):
        return GPIO.input(self.up)

    def is_pressed_down(self):
        return GPIO.input(self.down)

    def is_pressed_left(self):
        return GPIO.input(self.left)

    def is_pressed_right(self):
        return GPIO.input(self.right)

    def is_pressed_click(self):
        return GPIO.input(self.click)