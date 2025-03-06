# Rainy_UHF_Shield_Software

<img src="https://github.com/sbcshop/Rainy_UHF_Shield_Software/blob/main/images/Feature_Banner_Rainy_UHFShield.jpg">

Rainy UHF Shield which is Long-Range UHF RFID module designed to seamlessly integrate with your ArdiPi, Ardi-32 and Arduino Uno plus compatible boards, making it accessible to both beginners and experienced users alike.

This github provides getting started guide and other working details for Rainy UHF Shield 

### Features:
- Mounts directly onto your [ArdiPi](https://shop.sb-components.co.uk/products/ardipi-uno-r3-alternative-board-based-on-pico-w), [Ardi-32](https://shop.sb-components.co.uk/products/ardi32-uno-r3-alternative-board-based-on-esp32-s3-wroom), Arduino UNO and compatible boards
- Onboard High-performance Long-Range fast speed Rainy UHF RFID module
- SMA Antenna port to connect antenna of choice for increased range
- 1.14" TFT display for visual interactions
- Multi-tone Buzzer onboard for Audio alerts
- Shield compatible with both 3.3V and 5V MCU

### Specifications:
- **Microcontroller**  : Arduino and Compatible Boards
- **Supply Voltage:** 5V
- **Operating Pin:** 3.3V ~ 5V
- **Display Size**: 1.14"
- **Display Resolution**: 135x240 pixel
- **Communication Interface:** TTL (UART)
- **Frequency:** EU 865-868MHz or US 902-928MHz
- **Protocol:** ISO 18000-6C (EPC Gen 2)
- **Read speed:** Multi-tag,1-60tags/second (depend on antenna/tag and application)
- **Read range:**- 1-20m (depend on tag, antenna and application)
- **Read/Write Capability:** Yes
- **RF Power Output:** 15-26 dBm(adjustable)
- **Cooling Method:** Air cooling (no external heat sink required)
- **Antenna port:** 1 port ,SMA
- **Estimated Antenna Range:** 
     - **3dBi Antenna:** 0-2m Range
     - **5.5dBi Antenna:** 0-5m Range
       
## Hardware Overview
### Pinout
<img src="https://github.com/sbcshop/Rainy_UHF_Shield_Software/blob/main/images/Rainy_UHFShield_Pinout.jpg">

### Interfacing Details

- When Rainy UHF shield mounted on Ardi-32,

  <img src="https://github.com/sbcshop/Rainy_UHF_Shield_Software/blob/main/images/Rainy_UHF_Shield_withArdi-32.jpg">

  |Ardi-32 | Rainy UHF shield | Function |
  |---|---|---|
  | IO18/U1RXD | UHF_TXD | Serial UART communication Pin |
  | IO17/U1TXD | UHF_RXD | Serial UART communication Pin |
  | IO9 | UHF EN | UHF Enable pin, LOW to disable and HIGH to enable |  
  | IO2 | BUZ | Buzzer +ve Pin |
  | IO41 | LED | User LED |
  | IO47 | TFT_RST | Display Reset Pin for SPI |
  | IO21 | TFT_DC | Data/Command Pin of SPI |
  | IO10 | TFT_CS | Display Chip Select for SPI |
  | IO11 | TFT_MOSI | MOSI(Master OUT Slave IN) Pin of SPI  |
  | IO12 | TFT_CLK | Serial Clock pin of SPI |
  | IO14 | TFT_BL | Backlight of display |


- When Rainy UHF shield mounted on Arduino Uno, for uploading Code in UNO you will have to remove this UHF shield as it is using Hardware serial pin.
  
  <img src="https://github.com/sbcshop/Rainy_UHF_Shield_Software/blob/main/images/RainyUHFShield_withUNO.jpg">

  |Arduino UNO | Rainy UHF shield | Function |
  |---|---|---|
  | D0/Rx | UHF TXD | Serial UART Communication Pin |
  | D1/Tx | UHF RXD | Serial UART Communication Pin |
  | D6 | UHF EN | UHF Enable pin, HIGH - enable and LOW - disable |  
  | D5 | BUZ | Buzzer +ve Pin |
  | D4 | LED | User LED |
  | D8 | TFT_RST | Display Reset Pin for SPI |
  | D9 | TFT_DC | Data/Command Pin of SPI |
  | D10 | TFT_CS | Display Chip Select for SPI |
  | D11 | TFT_MOSI | MOSI(Master OUT Slave IN) Pin of SPI  |
  | D13 | TFT_CLK | Serial Clock pin of SPI |
  | D7 | TFT_BL | Backlight of display |


### 2. Installing Libraries
   - When compiling sample codes there are some dependency on external libraries sometime which you can add as shown here.
   - For example installing library, for display select Sketch > Include Library > Manage Libraries. We need ST7789 (1.10.3 version) and GFX library (1.11.7 version) for 1.14" TFT Display,

     <img src= "https://github.com/sbcshop/EnkFi_7.5_Software/blob/main/images/Lib_install.png" />

     <img src= "https://github.com/sbcshop/Rainy_UHF_ESP32_Software/blob/main/images/st7789_lib.png" width="589" height="228" />
     <img src= "https://github.com/sbcshop/Rainy_UHF_ESP32_Software/blob/main/images/GFX_lib.png" width="588" height="217" />

   - Similarly you can add more libraries if needed, make sure to install correct version. 

## Resources
  * [Schematic](https://github.com/sbcshop/Rainy_UHF_ESP32_Hardware/blob/main/Design%20Data/Rainy%20UHF%20FOR%20ESP32%20Sch.PDF)
  * [Hardware Files](https://github.com/sbcshop/Rainy_UHF_ESP32_Hardware)
  * [Rainy UHF Module Command Manual](https://github.com/sbcshop/Rainy_UHF_Breakout_Software/blob/main/Document/Rainy%20UHF%20Module%20Command%20Manual.pdf)
  * [Arduino IDE 1 overview](https://docs.arduino.cc/software/ide-v1/tutorials/Environment)
  * [Official Arduino Getting Started](https://docs.arduino.cc/learn/starting-guide/getting-started-arduino)
  * [Official Pico W Getting Started](https://projects.raspberrypi.org/en/projects/get-started-pico-w)
  * [Official Getting Started with ESP32 in Arduino](https://docs.espressif.com/projects/arduino-esp32/en/latest/)

    
## Related Products
   * [Rainy UHF for ESP32](https://shop.sb-components.co.uk/products/rainyfi-uhf-for-esp32-complete-board-kit) - UHF module with embedded ESP32 S3 for IoT prototyping.
   * [Rainy UHF HAT](https://shop.sb-components.co.uk/products/rainy-uhf-pi-hat-complete-kit) - UHF module HAT with Standard 40pin to support Raspberry Pi.
   * [Rainy UHF Pico Expansion](https://shop.sb-components.co.uk/products/rainypi-uhf-based-on-pico-complete-kit) -  UHF Expansion board easily incorporate Pico/Pico W/Pico 2.
   * [Rainy UHF Breakout](https://shop.sb-components.co.uk/products/rainy-uhf-breakout-complete-kit) - Compact UHF module breakout with Type C for standalone use and TTL for interfacing with various MCU.

## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=300">
</p>  
