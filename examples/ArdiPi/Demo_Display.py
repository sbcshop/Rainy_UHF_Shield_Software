# Demo Code for Onboard Display Testing

# Import required modules
from machine import Pin, UART, SPI
import st7789py as st7789
import vga1_bold_16x32 as font  # Large bold font
import vga1_8x16 as font1       # Smaller font
from time import sleep

# Initialize SPI interface for the onboard display
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

def draw_box():
    """Draws a red border around the screen."""
    tft.fill(0)  # Clear screen with black background
    tft.fill_rect(0, 0, 5, 132, st7789.RED)  # Left border
    tft.fill_rect(235, 0, 5, 132, st7789.RED)  # Right border
    tft.fill_rect(0, 0, 235, 5, st7789.RED)  # Top border
    tft.fill_rect(0, 130, 240, 5, st7789.RED)  # Bottom border

# Clear the display
tft.fill(0)

# Display a message on the screen
tft.text(font1, "Hello !", 30, 30)
sleep(2)  
tft.text(font1, "Hello !", 30, 30, st7789.BLACK)

draw_box()
tft.text(font, "Rainy UHF", 50, 20, st7789.YELLOW)  
tft.text(font, "Shield", 90, 60)   
