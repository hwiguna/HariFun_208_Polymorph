"""RP2040 Development Board with 1.14 inch LCD LORA Supports Arduino/MicroPyth - No SX1278"""
# https://www.banggood.com/RP2040-Development-Board-with-1_14-inch-LCD-LORA-Supports-Arduino-or-MicroPyth-p-1947659.html?rmmds=myorder&cur_warehouse=CN&ID=6319451
# https://github.com/01Space/RP2040-1.14LCD

from machine import Pin, SPI
from time import sleep
import st7789

TFA = 40	# top free area when scrolling
BFA = 40	# bottom free area when scrolling

def config(rotation=0, buffer_size=0, options=0):

    Pin(22, Pin.OUT, value=1)

    spi = SPI(1,#Was 0,
        baudrate=62500000,
        polarity=1,
        phase=0,
        sck=Pin(10, Pin.OUT), #Was Pin(2, Pin.OUT),
        mosi=Pin(11, Pin.OUT), #Was Pin(3, Pin.OUT),
        miso=None)

    return st7789.ST7789(
        spi,
        135,
        240,
        cs=Pin(9, Pin.OUT),#Was Pin(5, Pin.OUT),
        dc=Pin(8, Pin.OUT),#Was Pin(1, Pin.OUT),
        reset=Pin(12, Pin.OUT), #Was missing
        backlight=Pin(2, Pin.OUT),#Was Pin(4, Pin.OUT),
        rotation=rotation,
        options=options,
        buffer_size=buffer_size)