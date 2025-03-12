/*
 * Demo code to test onboard TFT Display
 * Arduino UNO <-> Display
 * D8  - TFT_RST 
 * D9  - TFT_DC  
 * D10 - TFT_CS  
 * D11 - TFT_MOSI  
 * D13 - TFT_CLK 
 * D7  - TFT_BL 
 */
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

void displayText(String text, int x, int y, uint16_t color, int size) {
  tft.setTextSize(size); 
  tft.setTextWrap(false);
  tft.setCursor(x, y);
  tft.setTextColor(color);
  tft.println(text);
}

void setup() {
    pinMode(BackLight, OUTPUT); // Set backLight LED pin OUTPUT
    digitalWrite(BackLight, HIGH); // Turn display backlight ON
    
    Serial.begin(115200); // Initialize SerialTerminal-ESP32 communication 
    
    tft.init(135, 240);           // Init ST7789 240x135
    Serial.println(F("Initialized"));

    tft.setRotation(3); // Change display rotation as per requirement
    tft.fillScreen(ST77XX_BLACK);
    
    // Draw outer box
    tft.drawRect(5, 5, 230, 125, ST77XX_WHITE); // Surrounding border
    
    displayText("Hello..!", 20, 20, ST77XX_YELLOW, 2);
    
    delay(2000);
    tft.fillScreen(ST77XX_BLACK);
}

void loop() {
    tft.fillScreen(ST77XX_BLACK);
    tft.drawRect(5, 5, 230, 125, ST77XX_WHITE); // Border
    
    displayText("Rainy UHF", 30, 30, ST77XX_YELLOW, 3);
    displayText("for", 80, 60, ST77XX_YELLOW, 2);
    displayText("Arduino", 50, 90, ST77XX_YELLOW, 3);
    
    delay(2000);
    tft.fillScreen(ST77XX_BLACK);
    tft.drawRect(5, 5, 230, 125, ST77XX_WHITE); // Redraw border
    
    displayText("SBComponents", 10, 40, ST77XX_BLUE, 3);
    displayText("https://shop.sb-components.co.uk/", 10, 80, ST77XX_WHITE, 1);
    
    delay(2000);
    tft.fillScreen(ST77XX_BLACK);
}
