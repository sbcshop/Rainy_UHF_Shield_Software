'''
Demo code to perform UHF Tags Memory write operation
'''
from machine import Pin,UART
from time import sleep
from rainy_uhf import UHFMODULE

baudrate = 115200  #default baudrate of Rainy UHF module
uhf = UHFMODULE(baudrate)

buzzer = Pin(3,Pin.OUT)
def beep_buzzer():
    buzzer.on()
    sleep(0.2)
    buzzer.off()
    
'''
Memory Bank : only writable memory can be used for memory write operation
1 - EPC  --> Read/Write
3 - USER --> Read/Write

2Byte = 1 Word for Rainy UHF Module
For Ease Write operation we have set 8 Word size (16 Byte) data size in library, So follow below configuration:

User Memory => 
- For Data write in user memory you can create random data of length 8 Word
  example,
  data_value = 00000000000000000000000000000012  <= pass for write

EPC Memory =>
- Use Tag Memory Read [Memory Bank - 1] operation first to get ResponseFrame
- For example,
  if EPC is 300833b2ddd2022022500869, you will get below using read operation
  ResponseFrame = '1f0e3400300833b2ddd2022022500869'
  1f0e, 3400,  [300833b2ddd2022022500869] (old EPC)
  
  Data Frame with New EPC,
  1f0e, 3400, [400833b2ddd2022022500890] (new EPC)
  data_value = 1f0e3400400833b2ddd2022022500890  <= pass this for write

'''

memory_bank = '3' # Change for corresponding Memory Write operation

''' Uncomment and provide data interested to write into memory '''
#data_value = 'b64c3400c7059afb1a00bd25ef7853d7'  #Data with EPC value for memory  1
data_value =   '00000000011100000000000000000020' #Random data for storing into memory 3
#print(data_value)

# Select corresponding Tag, Change with EPC of card on which write needs to perform
uhf.select_tag("c7059afb1a00bd25ef7853d7")  

response = None

while 1:
    response = uhf.write_tag_memory(memory_bank, data_value)  #Tag Memory Data Write
    if response is not None:
        beep_buzzer()
        print("Data= ",response)
        break
    sleep(0.1)