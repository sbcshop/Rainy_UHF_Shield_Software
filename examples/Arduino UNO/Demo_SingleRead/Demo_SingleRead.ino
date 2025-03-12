#include <SPI.h>
#include <Adafruit_GFX.h>    // Core graphics library
#include <Adafruit_ST7789.h> // Hardware-specific library for ST7789

byte MULTIPLE_READ[]   = {0XAA,0X00,0X27,0X00,0X03,0X22,0XFF,0XFF,0X4A,0XDD}; //Command for multiple reading of UHF card.
byte HARDWARE_VERSION[] = {0XAA,0X00,0X03,0X00,0X01,0X00,0X04,0XDD};//Command for Hardware Version.
byte STOP_READ[] = {0XAA, 0X00, 0X28, 0X00, 0X00, 0X28, 0XDD};
byte SINGLE_READ[] = {0XAA, 0X00, 0X22, 0X00, 0X00, 0X22, 0XDD};

byte container[512]; //A buff container to contain received bytes

const int uhf_enable = 6;  // Enable pin of UHF module connected at GPIO40
const int buzzerPin = 5;    // buzzer at GPIO
const int userLED = 4; // programmable led for status at GPIO3

void beep(int note, int duration){  // need note frequency and time duration (in millis)
  digitalWrite(userLED, HIGH);
  tone(buzzerPin, note, duration);
  delay(duration);
  digitalWrite(userLED, LOW);
}

void extractEPC(byte frm[], int le) {
  String asciiVal;

  // Uncomment to view complete Frame
  /*
  Serial.print("\nComplete Frame: ");
  for (int i = 0; i < le; i++) {
      Serial.print(frm[i], HEX);    //To print in HEX format
      Serial.write(32); // To add space between each byte print
    }
  */

  if (frm[2] != 0xFF) {
    //Serial.print("\nExtracted Info Byte from Frame: ");
  
    // Verify response with 2nd Byte -> Type and 3rd Byte -> COMMAND
    if (frm[1] == 0x02 && frm[2] == 0x22) {  // Extracts info Frame -> multiple read, single read command
      
      // exclude starting 3bytes - HEADER , TYPE, COMMAND and Last 4 bytes - CRC(MSB),CRC(LSB), CHECKSUM,  END
      // information contained inbetween bytes, Uncomment to view Extracted complete Frame
      /*
      for (int i = 3; i < le - 3; i++) { 
        Serial.print(frm[i], HEX);    //To print in HEX format on terminal
        Serial.write(32);   // To add space between each byte print on terminal
      }
      Serial.write(10);
      */
      beep(1245,500);
      Serial.print("EPC = 0x");
      for (int i = 8; i < le - 4; i++) { // UHF EPC value starts from 8th byte
        Serial.print(frm[i], HEX);    //To print in HEX format on terminal
      }
      Serial.write(10);
    }
  
  Serial.println();
 }
}

void setup() {
  pinMode(buzzerPin, OUTPUT); // set Buzzer pin as OUTPUT
  pinMode(uhf_enable,OUTPUT); // set UHF Enable/Disable pin as OUTPUT
  pinMode(userLED, OUTPUT);  // set User led pin as OUTPUT

  digitalWrite(uhf_enable,HIGH); // HIGH to enable and LOW - to disable the module

  Serial.begin(115200);

  Serial.println("Ready!");
  memset(container, 0, sizeof(container)); // Clear buffer before reading new data
  
}

void loop() {
  
  Serial.write(SINGLE_READ, sizeof(SINGLE_READ)); // Send command to UHF module
  //Serial.write(STOP_READ, sizeof(STOP_READ)); // Send command to UHF module required if previously multiread command executed
  Serial.flush();
  
  //delay(200);
  Serial.setTimeout(0);
  while (Serial.available()) { // Ensure data is received
    int len = Serial.readBytes(container, sizeof(container));

    Serial.print("Response: ");
    //Serial.println(container[0], HEX);
    // Check if the response starts with 0xAA to ensure correct data
    if (container[0] == 0xAA) {
      for (int i = 0; i < len; i++) {
        Serial.print(container[i], HEX);
        Serial.write(32); // Space between bytes
      }
      Serial.write(10); // New line
      Serial.flush();
      extractEPC(container, len);
      
    } else {
      Serial.println("Invalid data received!"); // Debugging output
    }
  }

  delay(200);
}

  
