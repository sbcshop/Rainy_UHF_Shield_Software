/* Simple command Testing */

// RAINY UHF COMMANDS CONSTANT 
const byte SINGLE_READ[]={0XAA,0X00,0X22,0X00,0X00,0X22,0XDD};   // Single polling command 
const byte HARDWARE_VERSION[]={0XAA,0X00, 0X03, 0X00, 0X01, 0X00, 0X04,0XDD};    // Hardware version read command
const byte MULTIPLE_READ[]={0XAA,0X00,0X27,0X00,0X03,0X22,0X27,0X10,0X83,0XDD};  // multiple polling command
const byte STOP_READ[]={0XAA,0X00,0X28,0X00,0X00,0X28,0XDD};  // Make sure to run Stop command if previously Multiple Read used
const byte START_BYTE[]={0XAA,0X00};  // default command start byte for each command
const byte END_BYTE[]={0XDD};         // command end byte for each command 
const byte GET_TRANSMIT_POWER[]={0xAA,0X00,0XB7,0X00,0X00,0XB7,0XDD};  // to get transmit power 
const byte REGION_US[]={0XAA,0X00,0X07,0X00,0X01,0X02,0X0A,0XDD};      // to set operating region as per module
const byte REGION_EU[]={0XAA,0X00,0X07,0X00,0X01,0X03,0X0B,0XDD};  
// Refer manual for more commands: https://github.com/sbcshop/Rainy_UHF_Breakout_Software/blob/main/Document/Rainy%20UHF%20Module%20Command%20Manual.pdf

String epcData;       // variable to store the data for displaying on tft screen.


byte container[512]; //A buff container to contain received bytes
const int uhf_enable = 6;  // Enable pin of UHF module connected at GPIO6

void setup() {
  pinMode(uhf_enable,OUTPUT); // set UHF Enable/Disable pin as OUTPUT
  digitalWrite(uhf_enable,HIGH); // HIGH to enable and LOW - to disable the module
  
  Serial.begin(115200);
  delay(3000);
  Serial.println("Ready!");
  Serial.flush();
  
  memset(container, 0, sizeof(container)); // Clear buffer before reading new data
}

void loop() {
  Serial.write(SINGLE_READ, sizeof(SINGLE_READ)); // Replace with suitable command to send for Testing
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
      delay(200);
      
    } else {
      Serial.println("Invalid data received!"); // Debugging output
    }
  }
    
  delay(50);
}
  
