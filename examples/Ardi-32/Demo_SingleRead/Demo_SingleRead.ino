/*
 * Demo code to read UHF Tags - Single Polling operation
 * 
 * Interfacing Details:
 * IO18/U1RXD - UHF_TXD 
 * IO17/U1TXD - UHF_RXD 
 * IO9        - UHF_EN 
 * IO2        - Buzzer
 * IO41       - User LED
 */
#include "RAINY_UHF.h"  // include Rainy UHF library

#define UHF_ENABLE 9 // Rainy UHF Enable pin

RAINY_UHF uhf;   // create Rainy UHF module instance 

const int buzzerPin = 2;    // buzzer at GPIO2
const int userLED = 41; // programmable led for status

void beep(int note, int duration){  // need note frequency and time duration (in millis)
  digitalWrite(userLED, HIGH);
  tone(buzzerPin, note, duration);
  delay(duration);
  digitalWrite(userLED, LOW);
}

void setup() {
    pinMode(buzzerPin,OUTPUT);
    //digitalWrite(buzzerPin, LOW);
    pinMode(userLED, OUTPUT);  // set User led pin as OUTPUT
    pinMode(UHF_ENABLE, OUTPUT);     // Initialize pin as OUTPUT
    digitalWrite(UHF_ENABLE, HIGH);  // HIGH - Enable UHF module, LOW -Disable Module
    
    Serial.begin(115200); // Initialize SerialTerimal-ESP32 communication 
    uhf.begin(115200, 18, 17);          // Initialize UHF-ESP32 UART communication (baudrate, rx, tx) 

    Serial.println("Ready!");
    
    /*
     * Uncomment to Set the UHF module's operating region, command should be executed only once 
     * Available options:  
     * "US" -> For the United States (902-928 MHz)  
     * "EU" -> For the Europe region (865-868 MHz)
     * You get reduce working range if incorrect region set
     * Required to set only once
     */
    //uhf.setRegion("US");
    //uhf.stopRead();    // Need to run only if previously multi read command execute
}


void loop(){
  std::vector<byte> single;     // Variable to hold single polling response from Rainy UHF
  single = uhf.singleReadTag();   // Perform single polling operation

  Serial.print("Response: ");
  for (byte& hexData : single){
    Serial.print(hexData,HEX);       // print reponse data
    Serial.write(32);            // add space between each hex byte value
  }

  Serial.println();
  
  String rssi = "EPC: ", epcText = "", crc = "";
  if (single.size() > 10) { // Ensure we have a valid response
     beep(1245, 500);
      for (int i = 8; i < single.size() - 4; i++) { // Extract EPC bytes
          char hexStr[3];  // Buffer for hex value (2 chars + null terminator)
            sprintf(hexStr, "%02X", single[i]);  // Convert to hex format
            epcText += String(hexStr) + " "; 
          
      }
      int rssi = single[5]; // RSSI is typically a byte, converting to integer
      char crcStr[6]; 
      sprintf(crcStr, "%02X %02X", single[20], single[21]); // Proper CRC formatting
      Serial.print("EPC: ");
      Serial.println(epcText);  // Print extracted EPC
      Serial.print("RSSI: ");
      Serial.println(rssi);     // Print extracted EPC
      Serial.print("CRC: ");
      Serial.println(crcStr);      // Print extracted EPC
      delay(500);
  }
  delay(20);
}
