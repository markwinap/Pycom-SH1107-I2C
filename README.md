# Pycom-SH1107
Pycom SH1107 128x128 OLED Screen driver


### Basic Usage

```py
# main.py -- put your code here!
from SH1107 import SH1107

screen = SH1107()
screen.init()
screen.clearDisplay()
screen.verticalMode()
# screen.horizontalMode()
screen.contrastLevel(128)  # 0 - 255

for x in range(20):
    screen.textXY(x, 0)
    screen.string("Hello World " + str(x))

````