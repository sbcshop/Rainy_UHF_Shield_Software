''' Demo to perform Single Read operation '''
from machine import Pin, UART,SPI
import vga1_bold_16x32 as font
import vga1_8x16 as font1
from time import sleep
from rainy_uhf import UHFMODULE
enable = Pin(11,Pin.OUT)
enable.on()

baudrate = 115200  #default baudrate of Rainy UHF module
uhf = UHFMODULE(baudrate)

LED = Pin(4,Pin.OUT)

buzzer = Pin(3,Pin.OUT)
def beep_buzzer():
    LED.on()
    buzzer.on()
    sleep(0.05)
    LED.off()
    buzzer.off()
    
def hex_to_signed_decimal(hex_number, bit_width):
    # Convert the hexadecimal number to a decimal integer
    decimal_number = int(hex_number, 16)
    
    # Calculate the maximum value for a signed integer of the given bit width
    max_value = 2 ** (bit_width - 1)
    
    # If the decimal number is greater than or equal to max_value, it is negative in two's complement
    if decimal_number >= max_value:
        decimal_number -= 2 ** bit_width

    return decimal_number

'''
Uncomment to set operating region, execute only once.
Options:
# "US" -> For the United States (902-928 MHz)  
# "EU" -> For the European region (865-868 MHz)
'''
#uhf.set_region("EU")

while True:
    recv = uhf.read_single_tag()
    #print(recv)
    if recv is not None:
        beep_buzzer()
        epc = "".join(recv[8:20])
        rssi = hex_to_signed_decimal(recv[5],8)
        print(f"EPC: {epc}")
        print(f"RSSI: {rssi}dBm")
    sleep(0.1)
    
   


            
    

