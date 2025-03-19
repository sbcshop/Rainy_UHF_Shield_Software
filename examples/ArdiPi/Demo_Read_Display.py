''' Demo to perform Multiple Read operation '''
from machine import Pin, UART, SPI
import st7789py as st7789 
import vga1_bold_16x32 as font
import vga1_8x16 as font1
from rainy_uhf import UHFMODULE
from time import sleep

baudrate = 115200  # Default baudrate of Rainy UHF module
uhf = UHFMODULE(baudrate)

LED = Pin(4, Pin.OUT)

#Define and configure Display SPI pins
spi = SPI(0, baudrate=40000000, sck=Pin(18), mosi=Pin(19))

# Initialize the ST7789 TFT display
tft = st7789.ST7789(
    spi,
    135,  # Display height
    240,  # Display width
    reset=Pin(15, Pin.OUT),  # Reset pin
    cs=Pin(17, Pin.OUT),      # Chip select pin
    dc=Pin(14, Pin.OUT),      # Data/command pin
    backlight=Pin(10, Pin.OUT),  # Backlight pin
    rotation=1  # Set display rotation
)
enable = Pin(11,Pin.OUT)
enable.on()

# Stop any previous multiple polling command if executed before
uhf.stop_reading()

tft.fill(0)
tft.text(font1, "EPCs Detected:", 30, 20, st7789.WHITE)

sleep(0.5)

detected_epcs = []  # List to store detected EPCs
max_entries = 4  # Maximum EPCs to display before refreshing

def refresh_display():
    """ Clears the display and resets detected EPCs list. """
    tft.fill(0)
    tft.text(font1, "EPCs Detected:", 30, 20, st7789.WHITE)
    detected_epcs.clear()

while True:
    recv = uhf.read_multiple_tags()
    if recv is not None:
        LED.on()
        sleep(0.05)
        LED.off()
        epc = "".join(recv[8:20])  # Extract EPC value
        
        if epc not in detected_epcs:
            if len(detected_epcs) >= max_entries:
                refresh_display()  # Refresh display when full
            
            detected_epcs.append(epc)
            print(f"New EPC: {epc}")
            tft.text(font1, epc, 30, 30 + (len(detected_epcs) * 20), st7789.YELLOW)
            
    sleep(0.1)

