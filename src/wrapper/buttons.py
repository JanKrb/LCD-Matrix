import RPi.GPIO as GPIO


class Keymap:
    """BCM keymap for left-sided buttons"""
    KEY1 = 21
    KEY2 = 20
    KEY3 = 16


class Buttons:
    def __init__(self, key1, key2, key3):
        self.key1 = key1
        self.key2 = key2
        self.key3 = key3

        self.event_key1 = None
        self.event_key2 = None
        self.event_key3 = None

        self._setup_keys()
        self._setup_events()

    def _setup_keys(self):
        GPIO.setup(GPIO.BCM)

        GPIO.setup(self.key1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.key2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.key3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def _setup_events(self):
        if self.event_key1 is not None:
            GPIO.add_event_detect(self.key1, GPIO.RISING, callback=self.event_key1)
        if self.event_key2 is not None:
            GPIO.add_event_detect(self.key2, GPIO.RISING, callback=self.event_key2)
        if self.event_key3 is not None:
            GPIO.add_event_detect(self.key3, GPIO.RISING, callback=self.event_key3)

    def is_pressed_key1(self):
        return GPIO.input(self.key1)

    def is_pressed_key2(self):
        return GPIO.input(self.key2)

    def is_pressed_key3(self):
        return GPIO.input(self.key3)
