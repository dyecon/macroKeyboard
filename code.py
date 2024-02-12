import board
import digitalio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
keyboard = Keyboard(usb_hid.devices)

import pwmio

# use 'import board' then 'dir(board)' to list available pin names
pin1 = board.A3
pin2 = board.GP17
pin3 = board.GP16
pin4 = board.GP14
led_pin = board.GP0

# Initialize LED
indicatorLED = pwmio.PWMOut(led_pin, frequency = 5000, duty_cycle = 0)

# Initialize Buttons
button1 = digitalio.DigitalInOut(pin1)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.DOWN

button2 = digitalio.DigitalInOut(pin2)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.DOWN

button3 = digitalio.DigitalInOut(pin3)
button3.direction = digitalio.Direction.INPUT
button3.pull = digitalio.Pull.DOWN

button4 = digitalio.DigitalInOut(pin4)
button4.direction = digitalio.Direction.INPUT
button4.pull = digitalio.Pull.DOWN

# Bools to store states (for controlling LEDs etc.)
button1_bool = False

# Set LED brightness
indicatorLED.duty_cycle = 2000 # 0 to 65535

# Main loop
while True:
    if button1.value:  
        print("Button 1 Pressed")
        keyboard.press(Keycode.W)
    else:
        keyboard.release(Keycode.W)
    if button2.value:  
        print("Button 2 Pressed")
        keyboard.press(Keycode.A)
    else:
        keyboard.release(Keycode.A)
    if button3.value:  
        print("Button 3 Pressed")
        keyboard.press(Keycode.S)
    else:
        keyboard.release(Keycode.S)
    if button4.value:  
        print("Button 4 Pressed")
        keyboard.press(Keycode.D)
    else:
        keyboard.release(Keycode.D)