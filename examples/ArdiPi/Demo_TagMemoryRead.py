'''
Code to perform read operation from Memory of UHF Tags,
Reserved, EPC, TID and User are different memory options available
'''
from machine import Pin,UART
from time import sleep
from rainy_uhf import UHFMODULE

baudrate = 115200  #default baudrate of Rainy UHF module
uhf = UHFMODULE(baudrate)
enable = Pin(11,Pin.OUT)
enable.on()
buzzer = Pin(3,Pin.OUT)

def beep_buzzer():
    buzzer.on()
    sleep(0.2)
    buzzer.off()
    
'''
Memory Bank 
1 - EPC  --> Read/Write
2 - TID  --> Only readable
3 - USER --> Read/Write
'''
memory_bank = '3' # Change for corresponding Memory Read operation

response = None

# Select corresponding Tag, Change with EPC of card whose memory needs to be read
uhf.select_tag("c7059afb1a00bd25ef7853d7")  

while 1:
    response = uhf.read_tag_memory(memory_bank)  #Tag Memory Data read
    print("ResponseFrame:",response)
    if response is not None:
        beep_buzzer()
        if memory_bank == '1':   # Response adjusted as per Tag data received
            print("EPC= ",response[8:])
        if memory_bank == '2':
            print("TID= ",response[:-8])
        if memory_bank == '3':
            print("Data= ",response)
        break
    sleep(0.1)

    

            
    


