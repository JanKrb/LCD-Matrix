import RPi.GPIO as GPIO
import time
import spidev


class Keymap:
    """BCM keymap display"""
    RST = 25
    DC = 24
    CS = 8
    BL = 18


class Screen:
    """Size of the oled display"""
    width = 128
    height = 64


class SPI:
    spi = spidev.SpiDev(0, 0)

    @staticmethod
    def digital_write(pin, value):
        GPIO.output(pin, value)

    @staticmethod
    def delay_ms(delaytime):
        time.sleep(delaytime / 1000.0)

    @staticmethod
    def spi_writebyte(data):
        SPI.spi.writebytes([data[0]])

    @staticmethod
    def module_init():
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(Keymap.RST, GPIO.OUT)
        GPIO.setup(Keymap.DC, GPIO.OUT)
        GPIO.setup(Keymap.CS, GPIO.OUT)
        GPIO.setup(Keymap.BL, GPIO.OUT)

        SPI.spi.max_speed_hz = 10000000
        SPI.spi.mode = 0b00

        GPIO.output(Keymap.CS, 0)
        GPIO.output(Keymap.BL, 1)
        GPIO.output(Keymap.DC, 0)
        return 0

    @staticmethod
    def module_exit():
        GPIO.output(Keymap.RST, 0)
        GPIO.output(Keymap.DC, 0)


class SH1106(object):
    def __init__(self):
        self.width = Screen.width
        self.height = Screen.height

    def command(self, cmd):
        """Write register address and data"""
        GPIO.output(Keymap.DC, GPIO.LOW)
        SPI.spi_writebyte([cmd])

    def Init(self):
        """Initialize display"""
        if SPI.module_init() != 0:
            return -1

        self.reset()
        self.command(0xAE)  # -- turn off oled panel
        self.command(0x02)  # -- set low column address
        self.command(0x10)  # -- set high column address
        self.command(0x40)  # -- set start line address  Set Mapping RAM Display Start Line (0x00~0x3F)
        self.command(0x81)  # -- set contrast control register
        self.command(0xA0)  # -- Set SEG/Column Mapping
        self.command(0xC0)  # -- Set COM/Row Scan Direction
        self.command(0xA6)  # -- set normal display
        self.command(0xA8)  # -- set multiplex ratio(1 to 64)
        self.command(0x3F)  # -- 1/64 duty
        self.command(0xD3)  # -- set display offset    Shift Mapping RAM Counter (0x00~0x3F)
        self.command(0x00)  # -- not offset
        self.command(0xd5)  # -- set display clock divide ratio/oscillator frequency
        self.command(0x80)  # -- set divide ratio, Set Clock as 100 Frames/Sec
        self.command(0xD9)  # -- set pre-charge period
        self.command(0xF1)  # -- Set Pre-Charge as 15 Clocks & Discharge as 1 Clock
        self.command(0xDA)  # -- set com pins hardware configuration
        self.command(0x12)
        self.command(0xDB)  # -- set vcomh
        self.command(0x40)  # -- Set VCOM Deselect Level
        self.command(0x20)  # -- Set Page Addressing Mode (0x00/0x01/0x02)
        self.command(0x02)  #
        self.command(0xA4)  # -- Disable Entire Display On (0xa4/0xa5)
        self.command(0xA6)  # -- Disable Inverse Display On (0xa6/a7)

        time.sleep(0.1)
        self.command(0xAF)  # -- turn on oled panel

    def reset(self):
        """Reset the display"""
        GPIO.output(Keymap.RST, GPIO.HIGH)
        time.sleep(0.1)

        GPIO.output(Keymap.RST, GPIO.LOW)
        time.sleep(0.1)

        GPIO.output(Keymap.RST, GPIO.HIGH)
        time.sleep(0.1)

    def get_buffer(self, image):
        buf = [0xFF] * ((self.width // 8) * self.height)
        image_monocolor = image.convert('1')
        imwidth, imheight = image_monocolor.size
        pixels = image_monocolor.load()

        if imwidth == self.width and imheight == self.height:
            for y in range(imheight):
                for x in range(imwidth):
                    if pixels[x, y] == 0:
                        buf[x + (y // 8) * self.width] &= ~(1 << (y % 8))

        elif imwidth == self.height and imheight == self.width:
            for y in range(imheight):
                for x in range(imwidth):
                    newx = y
                    newy = self.height - x - 1
                    if pixels[x, y] == 0:
                        buf[(newx + (newy // 8) * self.width)] &= ~(1 << (y % 8))
        return buf

    def show_image(self, pixel_buffer):
        for page in range(0, 8):
            # set page address
            self.command(0xB0 + page)

            # set low column address
            self.command(0x02)

            # set high column address
            self.command(0x10)

            # write data
            GPIO.output(Keymap.DC, GPIO.HIGH)

            for i in range(0, self.width):
                SPI.spi_writebyte([~pixel_buffer[i + self.width * page]])

    def clear(self):
        """Clear contents of image buffer"""
        _buffer = [0xff] * (self.width * self.height // 8)
        self.show_image(_buffer)
