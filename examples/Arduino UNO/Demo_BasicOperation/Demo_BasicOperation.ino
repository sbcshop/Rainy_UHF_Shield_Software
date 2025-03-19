/* Demo code to perform basic operation and display content*/
#include <SPI.h>
#include <Adafruit_GFX.h>    // Core graphics library
#include <Adafruit_ST7789.h> // Hardware-specific library for ST7789

// Define Display SPI pins 
#define TFT_CS        10  
#define TFT_RST       8 
#define TFT_DC        9
#define TFT_MOSI      11
#define TFT_CLK       13
#define BackLight     7

// Configure SPI and create instance for display 
Adafruit_ST7789 tft = Adafruit_ST7789(TFT_CS, TFT_DC, TFT_MOSI, TFT_CLK, TFT_RST);

byte HARDWARE_VERSION[] = {0XAA,0X00,0X03,0X00,0X01,0X00,0X04,0XDD};//Command for Hardware Version.
byte container[512]; //A buff container to contain received bytes

const int uhf_enable = 6;  // Enable pin of UHF module connected at GPIO6

void displayText(const String text, int x, int y, uint16_t color, int size) {
  tft.setTextSize(size); 
  tft.setTextWrap(false);
  tft.setCursor(x, y);
  tft.setTextColor(color);
  tft.println(text);
}


void frameExtract(byte frm[], int le) {
  String asciiVal;

  // Uncomment to view complete Frame
  Serial.print("\nComplete Frame: ");
  for (int i = 0; i < le; i++) {
      Serial.print(frm[i], HEX);    //To print in HEX format
      Serial.write(32); // To add space between each byte print
  }

  if (frm[2] != 0xFF) {
    //Serial.print("\nExtracted Info Byte from Frame: ");

    // Verify response with 2nd Byte -> Type and 3rd Byte -> COMMAND
    if (frm[1] == 0x01 && frm[2] == 0x03) { // Extracts info Frame -> Hardware_version Data
      //Serial.write(42);   // This add * on terminal 
      for (int i = 5; i < le - 2; i++) {
        Serial.print(frm[i], HEX);
        asciiVal += (char)frm[i];   // create ASCII string format of Response Byte Data 
        Serial.write(32);   // To add space between each byte print
      }
      Serial.write(10);
      Serial.print("HW Version: ");    //To print in ASCII format
      Serial.println(asciiVal);
      
      tft.fillScreen(ST77XX_BLACK);
      tft.drawRect(5, 5, 230, 125, ST77XX_WHITE); // Border
      tft.setTextSize(2); 
      tft.setTextWrap(false);
      tft.setCursor(20, 20);
      tft.setTextColor(ST77XX_WHITE);
      tft.print("HW Version:");
      tft.setCursor(20, 50);
      tft.setTextColor(ST77XX_YELLOW);
      tft.println(asciiVal);
      delay(2000);
      
      asciiVal = "";
    }
  Serial.println();
 }
 
}

void setup() {
  pinMode(uhf_enable,OUTPUT); // set UHF Enable/Disable pin as OUTPUT
  digitalWrite(uhf_enable,HIGH); // HIGH to enable and LOW - to disable the module
  
  pinMode(BackLight,OUTPUT); // Set backLight LED pin OUTPUT
  digitalWrite(BackLight,HIGH); // turn display backlight ON

  
  Serial.begin(115200);
  tft.init(135, 240);           // Init display
  
  Serial.println(F("Initialized"));

  tft.setRotation(3); // Change display rotation as per requirement
  tft.fillScreen(ST77XX_BLACK);
  
  // Draw outer box
  tft.drawRect(5, 5, 230, 125, ST77XX_WHITE); // Surrounding border
  displayText("Ready..!", 20, 20, ST77XX_YELLOW, 2);
  
  memset(container, 0, sizeof(container)); // Clear buffer before reading new data
}

void loop() {
  
  Serial.write(HARDWARE_VERSION, sizeof(HARDWARE_VERSION)); // Send command to UHF module
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
      frameExtract(container, len);
      
    } else {
      Serial.println("Invalid data received!"); // Debugging output
    }
  }

  delay(50);
}

  
