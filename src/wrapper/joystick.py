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

        self.event_up = None
        self.event_down = None
        self.event_left = None
        self.event_right = None
        self.event_click = None

        self._setup_keys()
        self._setup_events()

    def _setup_keys(self):
        GPIO.setup(GPIO.BCM)

        GPIO.setup(self.up, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.down, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.left, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.right, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.click, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def _setup_events(self):
        if self.event_up is not None:
            GPIO.add_event_detect(self.up, GPIO.RISING, callback=self.event_up)
        if self.event_down is not None:
            GPIO.add_event_detect(self.down, GPIO.RISING, callback=self.event_down)
        if self.event_left is not None:
            GPIO.add_event_detect(self.left, GPIO.RISING, callback=self.event_left)
        if self.event_right is not None:
            GPIO.add_event_detect(self.right, GPIO.RISING, callback=self.event_right)
        if self.event_click is not None:
            GPIO.add_event_detect(self.click, GPIO.RISING, callback=self.event_click)

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
