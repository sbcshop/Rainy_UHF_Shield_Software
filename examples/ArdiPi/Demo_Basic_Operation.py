''' Code to perform Basic Rainy UHF operations '''

#import required modules
from machine import Pin, UART,SPI
import st7789py as st7789 
import vga1_bold_16x32 as font
import vga1_8x16 as font1
from rainy_uhf import UHFMODULE
from time import sleep

baudrate = 115200 #default baudrate of Rainy UHF   
uhf = UHFMODULE(baudrate) #

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

buzzer = Pin(3,Pin.OUT)

enable = Pin(11,Pin.OUT)
enable.on()
sleep(0.5)

# Set the UHF module's operating region, command should be executed only once  
# Available options:  
# "US" -> For the United States (902-928 MHz)  
# "EU" -> For the European region (865-868 MHz)
# You get reduce working range if incorrect region set 
uhf.set_region("EU")
sleep(0.5)

tft.fill(0)
tft.text(font1,"Version:", 30, 30,st7789.WHITE)
sleep(0.5)

response = uhf.get_hardware_version() #get hardware version of UHF module
print(response)
tft.text(font1,response, 30, 50,st7789.YELLOW)

# Set the transmit power level (acceptable range: 15-26 dBm)
uhf.set_transmit_power(26) 

tft.text(font1,"Power:", 30, 80,st7789.WHITE)
sleep(0.5)

response = uhf.get_transmit_power() #get power value
print(response)
tft.text(font1,response, 30, 100,st7789.YELLOW)