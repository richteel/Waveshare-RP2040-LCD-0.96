import board
import displayio
import busio
from adafruit_simple_text_display import SimpleTextDisplay
from adafruit_bitmap_font import bitmap_font
from adafruit_st7735r import ST7735R

tft_dc = board.GP8
tft_cs = board.GP9
tft_clk = board.GP10  # SCL pin
tft_mosi = board.GP11  # SDA pin
tft_rst = board.GP12

# Release any resources currently in use for the displays
displayio.release_displays()

# spi = board.SPI()
spi = busio.SPI(tft_clk, MOSI=tft_mosi)

display_bus = displayio.FourWire(
    spi, command=tft_dc, chip_select=tft_cs, reset=tft_rst
)

display = ST7735R(display_bus, width=160, height=80, rotation=90,
                  rowstart=1, colstart=26, invert=True)

# Make the display context
splash = displayio.Group()
display.show(splash)

font_file = "fonts/neep-24.pcf"
font = bitmap_font.load_font(font_file)

screen = SimpleTextDisplay(
    display=display,
    font=font,
    text_scale=1,
    colors=(
        SimpleTextDisplay.GREEN,
        SimpleTextDisplay.WHITE,
        SimpleTextDisplay.RED,
        SimpleTextDisplay.YELLOW
    ),
)

screen[0].text = "One"
screen[1].text = "Two"
screen[2].text = "Three"
screen.show()

while True:
    pass
