# SOURCE REF: https://tutorial.cytron.io/2021/12/21/
#    display-image-on-the-graphic-lcd-using-maker-nano-rp2040-and-circuitpython/

"""
  Display image on graphic LCD using Maker Nano RP2040 and CircuitPython.

  Items:
  – Maker Pi Pico
    https://my.cytron.io/p-maker-pi-pico
  – Maker Nano RP2040
    https://my.cytron.io/maker-nano-rp2040-simplifying-projects-with-raspberry-pi-rp2040
  – 0.96" 160×80 IPS LCD (ST7735)
    https://my.cytron.io/p-0.96-inch-160×80-ips-lcd-breakout-st7735
  – USB Micro B Cable
    https://my.cytron.io/p-usb-micro-b-cable

  Libraries required from bundle (https://circuitpython.org/libraries):
  – adafruit_st7735r.mpy

  References:
  – https://learn.adafruit.com/circuitpython-display-support-using-displayio/
                                                                    display-a-bitmap

  Last update: 20 Dec 2021
"""

import board
import displayio
import busio
from adafruit_st7735r import ST7735R

# Release any resources currently in use for the displays
displayio.release_displays()

tft_dc = board.GP8
tft_cs = board.GP9  # Dummy
tft_clk = board.GP10  # SCL pin
tft_mosi = board.GP11  # SDA pin
tft_rst = board.GP12

spi = busio.SPI(tft_clk, MOSI=tft_mosi)

display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_rst)
display = ST7735R(
    display_bus, rotation=90, width=160, height=80, rowstart=1, colstart=26, invert=True
)

# Open the file
# with open("/blinka.jpg", "rb") as bitmap_file:
with open("/SpidermanNWH.bmp", "rb") as bitmap_file:

    # Setup the file as the bitmap data source
    bitmap = displayio.OnDiskBitmap(bitmap_file)

    # Create a TileGrid to hold the bitmap
    tile_grid = displayio.TileGrid(
        bitmap,
        pixel_shader=getattr(
            bitmap,
            'pixel_shader',
            displayio.ColorConverter()
        )
    )

    # Create a Group to hold the TileGrid
    group = displayio.Group()

    # Add the TileGrid to the Group
    group.append(tile_grid)

    # Add the Group to the Display
    display.show(group)

    # Loop forever so you can enjoy your image
    while True:
        pass
