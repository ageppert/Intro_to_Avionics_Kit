import machine
from machine import Pin, SoftI2C
import ssd1306
import time
from time import sleep

led_built_in = machine.Pin('LED', machine.Pin.OUT) #configure LED Pin as an output pin and create and led object for Pin class
led_external = machine.Pin(15, machine.Pin.OUT) #configure GPIO-15 Pin as an output pin and create and led object for Pin class
led_built_in.value(True)  #turn on the LED
led_external.value(True)
  
i2c = machine.SoftI2C(scl=machine.Pin(5), sda=machine.Pin(4))
print('Scanning I2C bus.')
devices = i2c.scan() # this returns a list of devices
device_count = len(devices)
if device_count == 0:
    print('No i2c device found.')
else:
    print(device_count, 'devices found.')
    oled_width = 128
    oled_height = 64
    oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
    oled.fill(0)
    oled.text('Aviation', 0, 10)
    oled.text('Explorers!', 0, 20)
    oled.show()
for device in devices:
    print('Decimal address:', device, ", Hex address: ", hex(device))

while True:
  led_built_in.value(True)  #turn on the LED
  led_external.value(False)
  time.sleep_ms(500)   #wait for one half second
  led_built_in.value(False)  #turn off the LED
  led_external.value(True)
  time.sleep_ms(500)   #wait for one half second
  