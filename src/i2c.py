import RPi.GPIO as GPIO
from smbus import SMBus
from wrapper.sh1106 import Keymap as Pins

address = 0x3C
bus = SMBus(1)

def digital_write(pin, value):
    GPIO.output(pin, value)

def digital_read(pin):
    return GPIO.input(pin)

def i2c_writebyte(reg, value):
    bus.write_byte_data(address, reg, value)

def module_init():
    # print("module_init")

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(Pins.RST, GPIO.OUT)
    GPIO.setup(Pins.DC, GPIO.OUT)
    GPIO.setup(Pins.CS, GPIO.OUT)
    GPIO.setup(Pins.BL, GPIO.OUT)

    GPIO.output(Pins.CS, 0)
    GPIO.output(Pins.BL, 1)
    GPIO.output(Pins.DC, 0)
    return 0

def module_exit():
    bus.close()
    GPIO.output(Pins.RST, 0)
    GPIO.output(Pins.DC, 0)
    