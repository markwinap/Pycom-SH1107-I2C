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

# screen.inverseDisplay()
# screen.normalDisplay()
# screen.deactivateScroll()
# screen.activateScroll()
# screen.on()
# screen.off()
SeeedLogo128x128 = [
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x40, 0x20, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x80, 0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x80, 0x18, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x03, 0x80, 0x1C, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x07, 0x00, 0x0E, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x05, 0x00, 0x0E, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0F, 0x00, 0x0F, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x1B, 0x00, 0x05, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x1A, 0x00, 0x05, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x32, 0x00, 0x04, 0xC0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x26, 0x00, 0x06, 0x40, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x66, 0x00, 0x06, 0x40, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x64, 0x00, 0x02, 0x60, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x44, 0x00, 0x02, 0x20, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x20, 0x00, 0xC4, 0x00, 0x02, 0x30, 0x00, 0x40, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x20, 0x00, 0x84, 0x00, 0x03, 0x10, 0x00, 0x40, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x20, 0x00, 0x8C, 0x00, 0x03, 0x10, 0x00, 0x40, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x60, 0x00, 0x8C, 0x00, 0x03, 0x10, 0x00, 0x60, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x60, 0x01, 0x88, 0x00, 0x01, 0x18, 0x00, 0x60, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x60, 0x01, 0x88, 0x00, 0x01, 0x18, 0x00, 0x60, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x60, 0x01, 0x08, 0x00, 0x01, 0x08, 0x00, 0x60, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x70, 0x01, 0x08, 0x00, 0x01, 0x08, 0x00, 0xE0, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x70, 0x01, 0x08, 0x00, 0x01, 0x08, 0x00, 0xE0, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x50, 0x01, 0x08, 0x00, 0x01, 0x08, 0x00, 0xE0, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x50, 0x01, 0x08, 0x00, 0x01, 0x08, 0x00, 0xB0, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x50, 0x01, 0x08, 0x00, 0x01, 0x08, 0x00, 0xB0, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x58, 0x01, 0x08, 0x00, 0x01, 0x08, 0x01, 0xB0, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x48, 0x01, 0x08, 0x00, 0x01, 0x08, 0x01, 0x30, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x48, 0x01, 0x08, 0x00, 0x01, 0x08, 0x01, 0x20, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x4C, 0x01, 0x08, 0x00, 0x01, 0x08, 0x03, 0x20, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x4C, 0x01, 0x08, 0x00, 0x01, 0x08, 0x03, 0x20, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x44, 0x01, 0x08, 0x00, 0x01, 0x08, 0x02, 0x20, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x46, 0x01, 0x88, 0x00, 0x01, 0x18, 0x06, 0x20, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x62, 0x01, 0x88, 0x00, 0x01, 0x18, 0x04, 0x20, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x63, 0x00, 0x88, 0x00, 0x01, 0x10, 0x0C, 0x60, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x21, 0x00, 0x8C, 0x00, 0x03, 0x10, 0x08, 0x40, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x21, 0x00, 0x84, 0x00, 0x03, 0x10, 0x08, 0x40, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x31, 0x80, 0xC4, 0x00, 0x02, 0x30, 0x18, 0xC0, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x10, 0x80, 0x44, 0x00, 0x02, 0x20, 0x10, 0x80, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x18, 0xC0, 0x64, 0x00, 0x02, 0x60, 0x31, 0x80, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x18, 0x40, 0x64, 0x00, 0x02, 0x60, 0x21, 0x80, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x08, 0x20, 0x26, 0x00, 0x06, 0x40, 0x61, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x0C, 0x30, 0x36, 0x00, 0x06, 0xC0, 0xC3, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x04, 0x30, 0x1A, 0x00, 0x05, 0x80, 0x82, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x06, 0x18, 0x1A, 0x00, 0x05, 0x81, 0x86, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x03, 0x0C, 0x0F, 0x00, 0x0F, 0x03, 0x0C, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x01, 0x84, 0x07, 0x00, 0x0E, 0x02, 0x18, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x01, 0x86, 0x07, 0x00, 0x0E, 0x06, 0x18, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0xC3, 0x03, 0x80, 0x1C, 0x0E, 0x30, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x63, 0x81, 0x80, 0x18, 0x0C, 0x60, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x39, 0x80, 0x80, 0x10, 0x18, 0xC0, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x1C, 0xC0, 0x40, 0x20, 0x33, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x0C, 0x60, 0x00, 0x00, 0x67, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x07, 0x30, 0x00, 0x00, 0xCE, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0xD8, 0x00, 0x01, 0xB8, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x7C, 0x00, 0x03, 0xE0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x1E, 0x00, 0x07, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x03, 0x80, 0x1C, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0E, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x1E, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x1E, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x1E, 0x00, 0x00,
    0x00, 0x00, 0x7E, 0x00, 0x0F, 0xC0, 0x00, 0x7E, 0x00, 0x03, 0xE0, 0x00, 0x00, 0x1E, 0x00, 0x00,
    0x00, 0x01, 0xFF, 0x80, 0x3F, 0xF0, 0x01, 0xFF, 0x80, 0x0F, 0xF8, 0x00, 0x3E, 0x1E, 0x00, 0x00,
    0x00, 0x03, 0xFF, 0xE0, 0x7F, 0xF8, 0x03, 0xFF, 0xC0, 0x1F, 0xFE, 0x00, 0xFF, 0x9E, 0x00, 0x00,
    0x00, 0x07, 0xFF, 0xC0, 0xFF, 0xFC, 0x07, 0xFF, 0xE0, 0x3F, 0xFF, 0x01, 0xFF, 0xDE, 0x00, 0x00,
    0x00, 0x07, 0x83, 0xC1, 0xFC, 0x7E, 0x0F, 0xC3, 0xE0, 0x7E, 0x1F, 0x03, 0xFF, 0xFE, 0x00, 0x00,
    0x00, 0x07, 0x80, 0x81, 0xF0, 0x3E, 0x0F, 0x81, 0xF0, 0xFC, 0x0F, 0x83, 0xFF, 0xFE, 0x00, 0x00,
    0x00, 0x07, 0x80, 0x03, 0xE0, 0x1F, 0x1F, 0x00, 0xF0, 0xF8, 0x07, 0x87, 0xE1, 0xFE, 0x00, 0x00,
    0x00, 0x07, 0x80, 0x03, 0xE0, 0x0F, 0x1E, 0x00, 0x78, 0xF0, 0x03, 0xC7, 0xC0, 0x7E, 0x00, 0x00,
    0x00, 0x07, 0xC0, 0x03, 0xC0, 0x0F, 0x1E, 0x00, 0x79, 0xF0, 0x03, 0xCF, 0x80, 0x7E, 0x00, 0x00,
    0x00, 0x07, 0xFE, 0x03, 0xFF, 0xFF, 0x3F, 0xFF, 0xF9, 0xFF, 0xFF, 0xCF, 0x80, 0x3E, 0x00, 0x00,
    0x00, 0x03, 0xFF, 0x83, 0xFF, 0xFF, 0x3F, 0xFF, 0xF9, 0xFF, 0xFF, 0xCF, 0x00, 0x3E, 0x00, 0x00,
    0x00, 0x03, 0xFF, 0xC3, 0xFF, 0xFF, 0x3F, 0xFF, 0xF9, 0xFF, 0xFF, 0xCF, 0x00, 0x3E, 0x00, 0x00,
    0x00, 0x00, 0xFF, 0xE3, 0xFF, 0xFF, 0x3F, 0xFF, 0xF9, 0xFF, 0xFF, 0xCF, 0x00, 0x3E, 0x00, 0x00,
    0x00, 0x00, 0x1F, 0xE3, 0xC0, 0x01, 0x3E, 0x00, 0x09, 0xF0, 0x00, 0x4F, 0x00, 0x3E, 0x00, 0x00,
    0x00, 0x00, 0x01, 0xF3, 0xC0, 0x00, 0x1E, 0x00, 0x01, 0xF0, 0x00, 0x0F, 0x80, 0x3E, 0x00, 0x00,
    0x00, 0x00, 0x00, 0xF3, 0xE0, 0x00, 0x1F, 0x00, 0x00, 0xF0, 0x00, 0x0F, 0x80, 0x7E, 0x00, 0x00,
    0x00, 0x02, 0x00, 0xF1, 0xF0, 0x00, 0x1F, 0x00, 0x00, 0xF8, 0x00, 0x07, 0xC0, 0x7E, 0x00, 0x00,
    0x00, 0x07, 0x01, 0xE1, 0xF8, 0x0C, 0x0F, 0x80, 0x60, 0x7C, 0x02, 0x07, 0xE1, 0xFE, 0x00, 0x00,
    0x00, 0x07, 0xE7, 0xE0, 0xFC, 0x3E, 0x0F, 0xE1, 0xE0, 0x7F, 0x0F, 0x03, 0xFF, 0xFE, 0x00, 0x00,
    0x00, 0x0F, 0xFF, 0xE0, 0xFF, 0xFE, 0x07, 0xFF, 0xF0, 0x3F, 0xFF, 0x83, 0xFF, 0xFE, 0x00, 0x00,
    0x00, 0x07, 0xFF, 0xC0, 0x7F, 0xFC, 0x03, 0xFF, 0xE0, 0x1F, 0xFF, 0x01, 0xFF, 0xDE, 0x00, 0x00,
    0x00, 0x01, 0xFF, 0x80, 0x1F, 0xF8, 0x00, 0xFF, 0xC0, 0x0F, 0xFE, 0x00, 0xFF, 0x9E, 0x00, 0x00,
    0x00, 0x00, 0x7E, 0x00, 0x07, 0xE0, 0x00, 0x3F, 0x00, 0x01, 0xF0, 0x00, 0x3E, 0x1E, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x40, 0x00, 0x00, 0x00, 0x00, 0x10, 0x00, 0x00, 0x00, 0x00, 0x80, 0x00, 0x00, 0x00,
    0x00, 0x0F, 0x40, 0x04, 0x1F, 0x22, 0x00, 0x10, 0x00, 0x00, 0x38, 0x00, 0x82, 0x00, 0x00, 0x00,
    0x00, 0x02, 0x40, 0x04, 0x04, 0x22, 0x00, 0x10, 0x00, 0x00, 0x20, 0x00, 0x82, 0x00, 0x00, 0x00,
    0x00, 0x02, 0x7B, 0x85, 0xE4, 0x32, 0xA6, 0xF5, 0xAA, 0xEA, 0x21, 0xCE, 0xF2, 0xA6, 0x00, 0x00,
    0x00, 0x02, 0x4A, 0x45, 0x24, 0x3E, 0x34, 0x95, 0xA2, 0xD2, 0x39, 0x62, 0x9A, 0xA4, 0x00, 0x00,
    0x00, 0x02, 0x4B, 0xC5, 0x24, 0x22, 0xF4, 0x95, 0x8A, 0x9E, 0x21, 0x4A, 0x8A, 0xE4, 0x00, 0x00,
    0x00, 0x02, 0x4A, 0x05, 0x24, 0x22, 0x94, 0x92, 0x4A, 0x98, 0x21, 0x5A, 0xD2, 0x84, 0x00, 0x00,
    0x00, 0x02, 0x49, 0xC4, 0xC4, 0x22, 0xF4, 0x72, 0x4E, 0x8E, 0x3D, 0x4E, 0xF2, 0x64, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
]

screen.clearDisplay()
screen.drawBitmap(SeeedLogo128x128, len(SeeedLogo128x128))
