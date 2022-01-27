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

        GPIO.setup(GPIO.BCM)
        
        GPIO.setup(key1,    GPIO.IN,    pull_up_down=GPIO.PUD_UP)
        GPIO.setup(key2,    GPIO.IN,    pull_up_down=GPIO.PUD_UP)
        GPIO.setup(key3,    GPIO.IN,    pull_up_down=GPIO.PUD_UP)
    
    def is_pressed_key1(self):
        return GPIO.input(self.key1)
    
    def is_pressed_key2(self):
        return GPIO.input(self.key2)
    
    def is_pressed_key3(self):
        return GPIO.input(self.key3)