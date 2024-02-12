# macroKeyboard
Learn how to build your own 4-key macro keyboard with an indicator LED.

---

## Step 1: Hardware
Minimum requirements: Raspberry Pi Pico, breadboard or perfboard, keyswitches, LED

1. Take a switch, connect one terminal to the **3V3** pin and the other to an available GPIO pin. Repeat for all other switches.
2. Connect the anode of your LED to **3V3**, and the cathode to a resistor (300 - 1kΩ), and the other end of the resistor to an available GPIO pin.

---

## Step 2. Install CircuitPython and adafruit_hid
1. Go to the [CircuitPython Website](https://circuitpython.org/downloads) and download the appropriate .UF2 for your Raspberry Pi model.
2. Hold the BOOT_SEL button on your Raspberry Pi, then connect it to your PC.
3. Copy the .UFW to the Pi's root directory; it should reboot automatically.
4. Download the [Adafruit HID code](https://github.com/adafruit/Adafruit_CircuitPython_HID) and copy the `adafruit_hid` folder into the Pi's `lib` folder.

---

## Step 3. Install Thonny
Thonny is the editor we will use for writing code and debugging. 
You can download Thonny from https://thonny.org.

---

## Step 4. Preparing to code
1. Connect your Raspberry Pi Pico to your PC, then open Thonny.
2. In Thonny, set your interpreter to `CircuitPython (generic)` in the bottom-right corner. You will now be able to run code on your Pi.
3. Run the following commands in Thonny's terminal (it could be hidden by default)
    ```
    import board
    dir(board)
    ```
    You should see a list of valid GPIO pin names. You will need the pin names later to control the LED and get input from the switches.

---

## Step 5. Coding
1. Copy the **code\.py** file in this repository to the root directory of your Raspberry Pi. 

Now we will edit the code to make it work.

2. On lines 11 to 15, change the pin names to the ones you are using.
3. On line 41, change the PWM duty cycle to control the LED brightness.
4. On lines 44 to 64, change `Keycode.W` etc. to the keys you want. A list of available keycodes can be found in  **keycodes.txt** in this repository.
5. Save the script and test your keyboard!

---

## Step 6. Take it a step further
The code provided here are simple examples, but you can modify it to add or improve features. For example, you could light the LED only when a key is pressed. Be creative and have fun!